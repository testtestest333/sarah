# -*- coding: utf-8 -*-

"""This file contains the implementation for working with the WDI CSV file."""

import csv
import os

#Indices
INDEX_COUNTRY = 0
INDEX_GINI = 3
INDEX_YEAR = 4 # Starts at 1960

FIRST_YEAR = 1960


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
                if col:
                    try:
                        value = float(col)
                        return True, value, None

                    except:
                        # Not a number
                        # pass
                        return False, None, None

    # Found key
    # if value:
    #     return True, value, None

    # Didn't find key
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
            col = INDEX_YEAR + (year - 1960)

            try:
                value = float(line[col])
                return True, value, None

            except:
                # Not a number
                # pass
                return False, None, None


    # Found key
    # if value:
    #     return True, value, None

    # Didn't find key
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
        return 'El Gini para %s en %d es %.4f' % (country, year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No hay valor de Gini para %s en %d' % (country, year)


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
        return 'El PIB en %s en %d es de %.2f Millones de $' % (
            country, year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No hay PIB en %s en %d' % (country, year)


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
        return 'El PIB per Cápita de %s en %d es $ %.2f' % (
            country, year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No hay PIB per Cápita para %s en %d' % (country, year)


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
        return 'El Desempleo en %s en %d es del %.4f %%' % (
            country, year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No hay tasa de Desempleo en %s en %d' % (country, year)
