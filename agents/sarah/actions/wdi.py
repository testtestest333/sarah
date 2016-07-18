# -*- coding: utf-8 -*-

"""This file contains the implementation for working with the WDI CSV file."""

import csv
import os

#Indices
INDEX_COUNTRY = 0
INDEX_ID = 1
INDEX_GINI = 3
INDEX_YEAR = 4 # Starts at 1960

FIRST_YEAR = 1960

# Groups to skip in some cases
GROUPS = [
    'LDC', 'LIC', 'LMC', 'LMY', 'LTE', 'MEA', 'MIC', 'MNA', 'OED', 'OSS',
    'PRE', 'PST', 'SSA', 'SSF', 'SST', 'TEA', 'TEC', 'TLA', 'TMN', 'TSA',
    'TSS', 'UMC', 'WLD'
]

def _get_max(config, key, year, skip_list=GROUPS):
    """Obtain max of values for a key in a year.

    Args:
        config (ConfigParser): Information about datafile to use.
        key (str): Key to search.
        year (int): Year to obtain (from parser).
        skip_list (list[str]): IDs to skip.

    Returns:
        Tuple: Boolean, Value (usually float), Error string
    """
    # Check datafile
    datafile = config.get('path')

    if not os.path.isfile(datafile):
        return False, None, 'Cant find the database %s' % datafile


    # Get year
    try:
        year = int(year)

    except:
        return False, None, 'When do you say?'

    print('Obtaining max of %s for year %d' % (key, year))

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

            # Check if it has to be skipped
            if line[INDEX_ID] in skip_list:
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

    # Obtain max
    result = value / float(countries)
    print('Found value: %f for %d countries (%f)' % (value, countries, result))

    return True, result, None

def _get_min(config, key, year, skip_list=GROUPS):
    """Obtain min of values for a key in a year.

    Args:
        config (ConfigParser): Information about datafile to use.
        key (str): Key to search.
        year (int): Year to obtain (from parser).
        skip_list (list[str]): IDs to skip.

    Returns:
        Tuple: Boolean, Value (usually float), Error string
    """
    # Check datafile
    datafile = config.get('path')

    if not os.path.isfile(datafile):
        return False, None, 'Cant find the database %s' % datafile


    # Get year
    try:
        year = int(year)

    except:
        return False, None, 'When do you say?'

    print('Obtaining min of %s for year %d' % (key, year))

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

            # Check if it has to be skipped
            if line[INDEX_ID] in skip_list:
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

    # Obtain min
    result = value / float(countries)
    print('Found value: %f for %d countries (%f)' % (value, countries, result))

    return True, result, None

def _get_avg(config, key, year, skip_list=GROUPS):
    """Obtain average of values for a key in a year.

    Args:
        config (ConfigParser): Information about datafile to use.
        key (str): Key to search.
        year (int): Year to obtain (from parser).
        skip_list (list[str]): IDs to skip.

    Returns:
        Tuple: Boolean, Value (usually float), Error string
    """
    # Check datafile
    datafile = config.get('path')

    if not os.path.isfile(datafile):
        return False, None, 'Cant find the database %s' % datafile


    # Get year
    try:
        year = int(year)

    except:
        return False, None, 'When do you say?'

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

            # Check if it has to be skipped
            if line[INDEX_ID] in skip_list:
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


def _get_count(config, key, year, skip_list=GROUPS):
    """Obtain number of countries that have a value for a key in a year.

    Args:
        config (ConfigParser): Information about datafile to use.
        key (str): Key to search.
        year (int): Year to obtain (from parser).
        skip_list (list[str]): IDs to skip.

    Returns:
        Tuple: Boolean, Value (usually float), Error string
    """
    # Check datafile
    datafile = config.get('path')

    if not os.path.isfile(datafile):
        return False, None, 'Cant find the database %s' % datafile


    # Get year
    try:
        year = int(year)

    except:
        return False, None, 'When do you say?'

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

            # Check if it has to be skipped
            if line[INDEX_ID] in skip_list:
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
        return False, None, 'Cant find the database %s' % datafile


    # Get country
    if not country:
        return False, None, 'Which country?'

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
        return False, None, 'Cant find the database %s' % datafile


    # Get country
    if not country:
        return False, None, 'Which country?'

    # Get year
    try:
        year = int(year)

    except:
        return False, None, 'When do you say?'

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
        return 'The Gini index in %s is %.4f' % (country, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No Gini index value for %s' % country


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
        return 'Average Gini in %s is %.4f' % (year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No Gini index value in %s' % year


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
        return 'The Gini index for %s in %s is %.4f' % (country, year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No Gini index value for %s in %s' % (country, year)


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
        return 'GDP in %s is %.2f Million $' % (country, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No GDP in %s' % country


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
        return 'Average GDP in %s is %.2f Million $' % (year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No GDP in %s' % year


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
        return 'GDP in %s on %s is %.2f Million $' % (
            country, year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No GDP in %s on %s' % (country, year)


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
        return 'GDP per Cápita in %s is $ %.2f' % (country, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No GDP per Cápita in %s' % country


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
        return 'Average GDP per Cápita in %s is $ %.2f' % (year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No average GDP per Cápita in %s' % year


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
        return 'GDP per Cápita of %s in %s is $ %.2f' % (
            country, year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No GDP per Cápita for %s in %s' % (country, year)


def unemp(config, parser):
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
        return 'The unemployment rate in %s is %.2f %%' % (country, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No unemployment rate in %s' % country


def unemp_avg(config, parser):
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
        return 'The average unemployment rate in %s is %.2f %%' % (year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No average unemployment rate in %s' % year


def unemp_year(config, parser):
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
        return 'The unemployment rate in %s in %s is %.2f %%' % (
            country, year, value)

    # No value
    if errmsg:
        # Something happened before finding the key
        return errmsg

    else:
        # Didn't find value for the specified country
        return 'No unemployment rate in %s in %s' % (country, year)
