#!/usr/bin/env python3

# Style for the commands.json file located in etc/sarah/commands.json:
#
# (Standard regular expression syntax)
#
# {
#     "^gini (\\w+)$": "action=gini&country=$0",
#     "^average gini (\\d+)$": "action=avg-gini&year=$0"
# }
#
# In the first example, the regular expression (\w+) will match any character
# (at least one character), and replace the word in the country tag ($0).
#
# In the second example, the regular expression (\d+) will match any digit
# (at least one), and replace the number in the year tag ($0).
#
# Note that replacing $0, $1, etc., occur in the same order they appear in.
#
# The "\" symbol needs to be escaped (add another \ symbol before it)

import argparse
import json
import os
import re

BASE_CMD = '^(.+)$'
# CMD_FILE = os.path.join(os.getenv['ZOE_HOME'], 'etc', 'sarah', 'commands.json')
CMD_FILE = './commands.json'


def get():
    """Return list of commands available."""
    print('sarah help')
    print('/%s/' % BASE_CMD, end='')

def run(args):
    """Execute an action based on the arguments parsed."""
    if not os.path.isfile(CMD_FILE):
        # File does not exist
        return

    # Parse the commands
    with open(CMD_FILE) as f:
        commands = json.load(f)

    for key in commands:
        print(key)
        match = re.findall(key, args.original)

        # Found matching command
        if match:
            cmd = commands.get(key)
            break

    if not match or not cmd:
        return

    # Get command args (single group)
    cmd_args = match[0]

    # Replace args in the command
    if type(cmd_args) is tuple:
        # Tuple
        for index, value in enumerate(cmd_args):
            cmd = cmd.replace('$%d' % index, value)

    elif type(cmd_args) is str:
        # Single string
        cmd = cmd.replace('$0', cmd_args)

    # Append additional info to the message
    special = 'dst=sarah&sender=%s&src=%s' % (args.sender, args.src)
    cmd = 'message %s&%s' % (special, cmd)

    # Send message
    print(cmd)


    # Help command
    # if args.original == 'sarah help':

def main():
    """Main function that manages the parsing of arguments.

        get: indicates that available commands must be returned
        run: indicates that a specific command should be executed
        original: original parsed command
        msg-sender-uniqueid: unique ID of the sender
        msg-src: where the message came from
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--get', action='store_true')
    parser.add_argument('--run', action='store_true')
    parser.add_argument('--original', action='store')
    parser.add_argument("--msg-sender-uniqueid", action='store', dest='sender')
    parser.add_argument("--msg-src", action='store', dest='src')

    args, unknown = parser.parse_known_args()

    # Get list of commands
    if args.get:
        get()

    elif args.run:
        run(args)

if __name__ == '__main__':
    main()
