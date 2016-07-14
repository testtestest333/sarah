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
        return 'No encuentro la base de datos'

    # Get country
    country = parser.get('country')

    if not country:
        return '¿Qué país es ese?'


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
        return 'El Gini para %s es %.4f' % (country, value)

    return 'No hay Gini para %s' % country

def gini_year(config, parser):
    """Obtain GINI for a given country in a specific year.

    Args:
        config (ConfigParser): Information about datafile to use.
        country (str): Country to search (from parser).
    """
    datafile = config.get('path')

    if not os.path.isfile(datafile):
        return 'No encuentro la base de datos'

    # Get country
    country = parser.get('country')

    if not country:
        return '¿Qué país es ese?'

    # Get year
    try:
        year = int(parser.get('year'))

    except:
        return '¿Cuándo dices?'


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
        return 'El Gini para %s en %d es %.4f' % (country, year, value)

    return 'No hay GINI para %s en %d' % (country, year)

def pib(config, parser):
    """Obtain latest PIB for a given country.

    Args:
        config (ConfigParser): Information about datafile to use.
        country (str): Country to search (from parser).
    """
    datafile = config.get('path')

    if not os.path.isfile(datafile):
        return 'No encuentro la base de datos'

    # Get country
    country = parser.get('country')

    if not country:
        return '¿Qué país es ese?'


    # Obtain value
    value = ''

    with open(datafile, 'r', encoding='mac_roman', newline='') as f:
        reader = csv.reader(f)

        # Read line by line
        for line in reader:

            # Check country
            if line[INDEX_COUNTRY] != country:
                continue

            # Check PIB
            if not 'NY.GDP.MKTP.CD' in line:
                continue

            # Start from the end and stop when a numerical value is reached
            for col in reversed(line):
                if col:
                    try:
                        value = float(col) / 1000000

                    except:
                        # Not a number
                        pass

                    break

    if value:
        return 'El PIB en %s es de %.2f Millones de $' % (country, value)

    return 'No hay PIB en %s' % country

def pib_year(config, parser):
    """Obtain PIB for a given country in a specific year.

    Args:
        config (ConfigParser): Information about datafile to use.
        country (str): Country to search (from parser).
    """
    datafile = config.get('path')

    if not os.path.isfile(datafile):
        return 'No encuentro la base de datos'

    # Get country
    country = parser.get('country')

    if not country:
        return '¿Qué país es ese?'

    # Get year
    try:
        year = int(parser.get('year'))

    except:
        return '¿Cuándo dices?'


    # Obtain value
    value = ''

    with open(datafile, 'r', encoding='mac_roman', newline='') as f:
        reader = csv.reader(f)

        # Read line by line
        for line in reader:

            # Check country
            if line[INDEX_COUNTRY] != country:
                continue

            # Check PIB
            if not 'NY.GDP.MKTP.CD' in line:
                continue

            # Get specific column
            col = INDEX_YEAR + (year - 1960)

            try:
                value = float(line[col]) / 1000000

            except:
                # Not a number
                pass

    if value:
        return 'El PIB de %s en %d es de %.2f Millones de $' % (country, year, value)

    return 'No hay PIB de %s en %d' % (country, year)

def pibpc(config, parser):
    """Obtain latest PIBpc for a given country.

    Args:
        config (ConfigParser): Information about datafile to use.
        country (str): Country to search (from parser).
    """
    datafile = config.get('path')

    if not os.path.isfile(datafile):
        return 'No encuentro la base de datos'

    # Get country
    country = parser.get('country')

    if not country:
        return '¿Qué país es ese?'


    # Obtain value
    value = ''

    with open(datafile, 'r', encoding='mac_roman', newline='') as f:
        reader = csv.reader(f)

        # Read line by line
        for line in reader:

            # Check country
            if line[INDEX_COUNTRY] != country:
                continue

            # Check PIB
            if not 'NY.GDP.PCAP.CD' in line:
                continue

            # Start from the end and stop when a numerical value is reached
            for col in reversed(line):
                if col:
                    try:
                        value = float(col)

                    except:
                        # Not a number
                        pass

                    break

    if value:
        return 'El PIB per Cápita de %s es $ %.2f' % (country, value)

    return 'No hay PIB per Cápita de %s' % country

def pibpc_year(config, parser):
    """Obtain PIBpc for a given country in a specific year.

    Args:
        config (ConfigParser): Information about datafile to use.
        country (str): Country to search (from parser).
    """
    datafile = config.get('path')

    if not os.path.isfile(datafile):
        return 'No encuentro la base de datos'

    # Get country
    country = parser.get('country')

    if not country:
        return '¿Qué país es ese?'

    # Get year
    try:
        year = int(parser.get('year'))

    except:
        return '¿Cuándo dices?'


    # Obtain value
    value = ''

    with open(datafile, 'r', encoding='mac_roman', newline='') as f:
        reader = csv.reader(f)

        # Read line by line
        for line in reader:

            # Check country
            if line[INDEX_COUNTRY] != country:
                continue

            # Check PIB
            if not 'NY.GDP.PCAP.CD' in line:
                continue

            # Get specific column
            col = INDEX_YEAR + (year - 1960)

            try:
                value = float(line[col])

            except:
                # Not a number
                pass

    if value:
        return 'El PIB per Cápita de %s en %d es $ %.2f' % (country, year, value)

    return 'No hay PIB per Cápita para %s en %d' % (country, year)
