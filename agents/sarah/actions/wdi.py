# -*- coding: utf-8 -*-

"""This file contains the implementation for working with the WDI CSV file."""

import csv
import os

#Indices
INDEX_COUNTRY = 0
INDEX_GINI = 3
INDEX_YEAR = 4 # Starts at 1960

FIRST_YEAR = 1960

def gini(config, parser):
    """Obtain latest GINI for a given country.

    Args:
        config (ConfigParser): Information about datafile to use.
        country (str): Country to search (from parser).
    """
    datafile = config.get('path')

    if not os.path.isfile(datafile):
        return 'Could not read data file'

    # Get country
    country = parser.get('country')

    if not country:
        return 'Failed to parse country name'


    # Obtain value
    value = ''

    with open(datafile, 'r', encoding='mac_roman', newline='') as f:
        reader = csv.reader(f)

        # Read line by line
        for line in reader:

            # Check country
            if line[INDEX_COUNTRY] != country:
                continue

            # Check GINI
            if not 'SI.POV.GINI' in line:
                continue

            # Start from the end and stop when a numerical value is reached
            for col in reversed(line):
                if col:
                    try:
                        value = float(col) / 100

                    except:
                        # Not a number
                        pass

                    break

    if value:
        return 'GINI %s: %.4f' % (country, value)

    return 'Could not find GINI for %s' % country

def gini_year(config, parser):
    """Obtain GINI for a given country in a specific year.

    Args:
        config (ConfigParser): Information about datafile to use.
        country (str): Country to search (from parser).
    """
    datafile = config.get('path')

    if not os.path.isfile(datafile):
        return 'Could not read data file'

    # Get country
    country = parser.get('country')

    if not country:
        return 'Failed to parse country name'

    # Get year
    try:
        year = int(parser.get('year'))

    except:
        return 'Invalid year'


    # Obtain value
    value = ''

    with open(datafile, 'r', encoding='mac_roman', newline='') as f:
        reader = csv.reader(f)

        # Read line by line
        for line in reader:

            # Check country
            if line[INDEX_COUNTRY] != country:
                continue

            # Check GINI
            if not 'SI.POV.GINI' in line:
                continue

            # Get specific column
            col = INDEX_YEAR + (year - 1960)

            try:
                value = float(line[col]) / 100

            except:
                # Not a number
                pass

    if value:
        return 'GINI %s (%d): %.4f' % (country, year, value)

    return 'Could not find GINI for %s in %d' % (country, year)
