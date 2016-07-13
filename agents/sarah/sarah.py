#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import configparser
import os
import zoe
from zoe.deco import Agent, AnyMessage
from actions.mapper import action_map

DB_CONF = os.path.join(os.getenv('ZOE_HOME'), 'etc', 'sarah', 'databases.conf')


@Agent(name='sarah')
class Sarah:

    @AnyMessage()
    def receive(self, parser):
        """Receives all messages and executes actions accordingly.

        Common parser keys:
            sender (str): Unique ID of the sender.
            src (str): Where the message came from.
        """
        action_name = parser.get('action')
        if not action_name:
            # No action?
            return

        action = action_map.get(action_name)
        if not action:
            # No action?
            return

        # Obtain database config
        conf_parser = configparser.ConfigParser()
        conf_parser.read(DB_CONF)

        name_conf = action.get('conf')
        if name_conf and name_conf in conf_parser.sections():
            conf = conf_parser[name_conf]

        # Execute the function
        func = action.get('func')

        if not func:
            # No function defined
            return self.feedback(
                'No function associated to the specified action',
                parser
            )

        result = func(conf, parser)

        return self.feedback(result, parser)

    def feedback(self, msg, parser):
        """Send back a message to an user.

        Args:
            msg (str): Message to send.
            parser (MessageParser): Parsed Zoe message.
        """
        user = parser.get('sender')
        dst = parser.get('src')

        if not user or not dst:
            return

        to_send = {
            'dst': 'relay',
            'relayto': dst,
            'to': user,
            'msg': msg
        }

        return zoe.MessageBuilder(to_send)
