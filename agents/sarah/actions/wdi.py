# -*- coding: utf-8 -*-

"""This file contains the implementation for working with the WDI CSV file."""

import csv
import os

#Indices
INDEX_COUNTRY = 0
INDEX_GINI = 3
INDEX_YEAR = 4 # Starts at 1960

FIRST_YEAR = 1960


def _get_avg(config, key, year):
    """Obtain average of values for a key in a year.

    Args:
        config (ConfigParser): Information about datafile to use.
        key (str): Key to search.
        year (int): Year to obtain (from parser).

    Returns:
        Tuple: Boolean, Value (usually float), Error string
    """
    # Check datafile
    datafile = config.get('path')

    if not os.path.isfile(datafile):
        return False, None, 'No encuentro la base de datos %s' % datafile


    # Get year
    try:
        year = int(year)

    except:
        return False, None, '¿Cuándo dices?'

    print('Obtaining average of %s for year %d' % (key, year))

    # Obtain value
    value = 0.0
    countries = 0

    with open(datafile, 'r', encoding='mac_roman', newline='') as f:
        reader = csv.reader(f)

        # Read line by line
        for line in reader:

            # Check key
            if not key in line:
                continue

            # Get specific column
            col = INDEX_YEAR + (year - FIRST_YEAR)

            try:
                col_val = float(line[col])

                if col_val > 0:
                    # Must be positive
                    value += col_val
                    countries += 1

            except:
                # Not a number
                pass


    # Didn't find key
    if not value:
        print('Did not find value')
        return False, None, None

    # Obtain average
    result = value / float(countries)
    print('Found value: %f for %d countries (%f)' % (value, countries, result))

    return True, result, None


def _get_count(config, key, year):
    """Obtain number of countries that have a value for a key in a year.

    Args:
        config (ConfigParser): Information about datafile to use.
        key (str): Key to search.
        year (int): Year to obtain (from parser).

    Returns:
        Tuple: Boolean, Value (usually float), Error string
    """
    # Check datafile
    datafile = config.get('path')

    if not os.path.isfile(datafile):
        return False, None, 'No encuentro la base de datos %s' % datafile


    # Get year
    try:
        year = int(year)

    except:
        return False, None, '¿Cuándo dices?'

    print('Obtaining count of %s for year %d' % (key, year))

    # Obtain value
    value = 0

    with open(datafile, 'r', encoding='mac_roman', newline='') as f:
        reader = csv.reader(f)

        # Read line by line
        for line in reader:

            # Check key
            if not key in line:
                continue

            # Get specific column
            col = INDEX_YEAR + (year - FIRST_YEAR)

            try:
                float(line[col])
                value += 1

            except:
                # Not a number
                pass


    # Always return value
    return True, value, None


def _get_latest(config, key, country):
    """Obtain latest value for a given country.

    Args:
        config (ConfigParser): Information about datafile to use.
        key (str): Key to search.
        country (str): Country to search (from parser).

    Returns:
        Tuple: Boolean, Value (usually float), Error string
    """
    # Check datafile
    datafile = config.get('path')

    if not os.path.isfile(datafile):
        return False, None, 'No encuentro la base de datos %s' % datafile


    # Get country
    if not country:
        return False, None, '¿Qué país es ese?'

    print('Obtaining latest %s for country %s' % (key, country))

    # Obtain value
    value = None

    with open(datafile, 'r', encoding='mac_roman', newline='') as f:
        reader = csv.reader(f)

        # Read line by line
        for line in reader:

            # Check key
            if not key in line:
                continue

            # Check country
            if line[INDEX_COUNTRY] != country:
                continue

            # Start from the end and stop when a numerical value is reached
            for col in reversed(line):
                print(col)
                if col:
                    try:
                        value = float(col)

                        print('Value found for %s: %f' % (country, value))
                        return True, value, None

                    except:
                        # Not a number
                        pass

    # # Found key
    # if value:
    #     print('Value found for %s: %f' % (country, value))
    #     return True, value, None

    # Didn't find key
    print('Did not find value')
    return False, None, None


def _get_year(config, key, country, year):
    """Obtain latest value for a given country.

    Args:
        config (ConfigParser): Information about datafile to use.
        key (str): Key to search.
        country (str): Country to search (from parser).
        year (int): Year to obtain (from parser).

    Returns:
        Tuple: Boolean, Value (usually float), Error string
    """
    # Check datafile
    datafile = config.get('path')

    if not os.path.isfile(datafile):
        return False, None, 'No encuentro la base de datos %s' % datafile


    # Get country
    if not country:
        return False, None, '¿Qué país es ese?'

    # Get year
    try:
        year = int(year)

    except:
        return False, None, '¿Cuándo dices?'

    print('Obtaining %s for country %s in year %d' % (key, country, year))


    # Obtain value
    value = None

    with open(datafile, 'r', encoding='mac_roman', newline='') as f:
        reader = csv.reader(f)

        # Read line by line
        for line in reader:

            # Check key
            if not key in line:
                continue

            # Check country
            if line[INDEX_COUNTRY] != country:
                continue

            # Get specific column
            col = INDEX_YEAR + (year - FIRST_YEAR)

            try:
                value = float(line[col])

                print('Value found for %s in %d: %f' % (country, year, value))
                return True, value, None

            except:
                # Not a number
                # pass
                print('Did not find value')
                return False, None, None


    # Found key
    # if value:
    #     return True, value, None

    # Didn't find key
    print('Did not find value')
    return False, None, None


def gini(config, parser):
    """Obtain latest GINI for a given country.

    Args:
        config (ConfigParser): Information about datafile to use.
        country (str): Country to search (from parser).
    """
    key = 'SI.POV.GINI'
    country = parser.get('country')

    status, value, errmsg = _get_latest(config, key, country)

    if status:
        # Found value
        value = value / 100
        return 'El Gini para %s es %.4f' % (country, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No hay valor de Gini para %s' % country


def gini_avg(config, parser):
    """Obtain average GINI for a given year.

    Args:
        config (ConfigParser): Information about datafile to use.
        year (int): Year to obtain (from parser).
    """
    key = 'SI.POV.GINI'
    year = parser.get('year')

    status, value, errmsg = _get_avg(config, key, year)

    if status:
        # Found value
        value = value / 100
        return 'El Gini medio en %s es %.4f' % (year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No hay valor medio de Gini para %s' % year


def gini_year(config, parser):
    """Obtain GINI for a given country in a specific year.

    Args:
        config (ConfigParser): Information about datafile to use.
        country (str): Country to search (from parser).
        year (int): Year to obtain (from parser).
    """
    key = 'SI.POV.GINI'
    country = parser.get('country')
    year = parser.get('year')

    status, value, errmsg = _get_year(config, key, country, year)

    if status:
        # Found value
        value = value / 100
        return 'El Gini para %s en %s es %.4f' % (country, year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No hay valor de Gini para %s en %s' % (country, year)


def pib(config, parser):
    """Obtain latest PIB for a given country.

    Args:
        config (ConfigParser): Information about datafile to use.
        country (str): Country to search (from parser).
    """
    key = 'NY.GDP.MKTP.CD'
    country = parser.get('country')

    status, value, errmsg = _get_latest(config, key, country)

    if status:
        # Found value
        value = value / 1000000
        return 'El PIB en %s es de %.2f Millones de $' % (country, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No hay PIB en %s' % country


def pib_avg(config, parser):
    """Obtain average PIB in a specific year.

    Args:
        config (ConfigParser): Information about datafile to use.
        year (int): Year to obtain (from parser).
    """
    key = 'NY.GDP.MKTP.CD'
    year = parser.get('year')

    status, value, errmsg = _get_avg(config, key, year)

    if status:
        # Found value
        value = value / 1000000
        return 'El PIB medio en %s es de %.2f Millones de $' % (year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No hay PIB medio en %s' % year


def pib_year(config, parser):
    """Obtain PIB for a given country in a specific year.

    Args:
        config (ConfigParser): Information about datafile to use.
        country (str): Country to search (from parser).
        year (int): Year to obtain (from parser).
    """
    key = 'NY.GDP.MKTP.CD'
    country = parser.get('country')
    year = parser.get('year')

    status, value, errmsg = _get_year(config, key, country, year)

    if status:
        # Found value
        value = value / 1000000
        return 'El PIB en %s en %s es de %.2f Millones de $' % (
            country, year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No hay PIB en %s en %s' % (country, year)


def pibpc(config, parser):
    """Obtain latest PIBpc for a given country.

    Args:
        config (ConfigParser): Information about datafile to use.
        country (str): Country to search (from parser).
    """
    key = 'NY.GDP.PCAP.CD'
    country = parser.get('country')

    status, value, errmsg = _get_latest(config, key, country)

    if status:
        # Found value
        return 'El PIB per Cápita de %s es $ %.2f' % (country, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No hay PIB per Cápita de %s' % country


def pibpc_avg(config, parser):
    """Obtain average PIBpc in a specific year.

    Args:
        config (ConfigParser): Information about datafile to use.
        year (int): Year to obtain (from parser).
    """
    key = 'NY.GDP.PCAP.CD'
    year = parser.get('year')

    status, value, errmsg = _get_avg(config, key, year)

    if status:
        # Found value
        return 'El PIB per Cápita medio en %s es $ %.2f' % (year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No hay PIB per Cápita medio en %s' % year


def pibpc_year(config, parser):
    """Obtain PIBpc for a given country in a specific year.

    Args:
        config (ConfigParser): Information about datafile to use.
        country (str): Country to search (from parser).
        year (int): Year to obtain (from parser).
    """
    key = 'NY.GDP.PCAP.CD'
    country = parser.get('country')
    year = parser.get('year')

    status, value, errmsg = _get_year(config, key, country, year)

    if status:
        # Found value
        return 'El PIB per Cápita de %s en %s es $ %.2f' % (
            country, year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No hay PIB per Cápita para %s en %s' % (country, year)


def desemp(config, parser):
    """Obtain latest Unenployment for a given country.

    Args:
        config (ConfigParser): Information about datafile to use.
        country (str): Country to search (from parser).
    """
    key = 'SL.UEM.TOTL.NE.ZS'
    country = parser.get('country')

    status, value, errmsg = _get_latest(config, key, country)

    if status:
        # Found value
        return 'El Desempleo en %s es del %.4f %%' % (country, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No hay tasa de Desempleo en %s' % country


def desemp_avg(config, parser):
    """Obtain average Unemployment in a specific year.

    Args:
        config (ConfigParser): Information about datafile to use.
        year (int): Year to obtain (from parser).
    """
    key = 'SL.UEM.TOTL.NE.ZS'
    year = parser.get('year')

    status, value, errmsg = _get_avg(config, key, year)

    if status:
        # Found value
        return 'El Desempleo medio en %s es del %.4f %%' % (year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No hay Desempleo medio en %s' % year


def desemp_year(config, parser):
    """Obtain Unemployment for a given country in a specific year.

    Args:
        config (ConfigParser): Information about datafile to use.
        country (str): Country to search (from parser).
        year (int): Year to obtain (from parser).
    """
    key = 'SL.UEM.TOTL.NE.ZS'
    country = parser.get('country')
    year = parser.get('year')

    status, value, errmsg = _get_year(config, key, country, year)

    if status:
        # Found value
        return 'El Desempleo en %s en %s es del %.4f %%' % (
            country, year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No hay tasa de Desempleo en %s en %s' % (country, year)
