# -*- coding: utf-8 -*-
"""This is the only file imported by sarah to execute the actions.

Ideally, this one should import additional libraries and map the functions
with a given name.

All functions must receive the parser and additional parameters such as
database connector to use.
"""

from actions import wdi

action_map = {
    'gini' : {
        'conf': 'wdi_csv',
        'func': wdi.gini
    },

    'gini-avg' : {
        'conf': 'wdi_csv',
        'func': wdi.gini_avg
    },

    'gini-count' : {
        'conf': 'wdi_csv',
        'func': wdi.gini_count
    },

    'gini-year': {
        'conf': 'wdi_csv',
        'func': wdi.gini_year
    },

    'gini-max': {
        'conf': 'wdi_csv',
        'func': wdi.gini_max
    },

    'gini-min': {
        'conf': 'wdi_csv',
        'func': wdi.gini_min
    },

    'pib' : {
        'conf': 'wdi_csv',
        'func': wdi.pib
    },

    'pib-avg' : {
        'conf': 'wdi_csv',
        'func': wdi.pib_avg
    },

    'pib-year': {
        'conf': 'wdi_csv',
        'func': wdi.pib_year
    },

    'pib-max': {
        'conf': 'wdi_csv',
        'func': wdi.pib_max
    },

    'pib-min': {
        'conf': 'wdi_csv',
        'func': wdi.pib_min
    },

    'pibpc': {
        'conf': 'wdi_csv',
        'func': wdi.pibpc
    },

    'pibpc-avg': {
        'conf': 'wdi_csv',
        'func': wdi.pibpc_avg
    },

    'pibpc-year': {
        'conf': 'wdi_csv',
        'func': wdi.pibpc_year
    },

    'pibpc-max': {
        'conf': 'wdi_csv',
        'func': wdi.pibpc_max
    },

    'pibpc-min': {
        'conf': 'wdi_csv',
        'func': wdi.pibpc_min
    },

    'unemp' : {
        'conf': 'wdi_csv',
        'func': wdi.unemp
    },

    'unemp-avg' : {
        'conf': 'wdi_csv',
        'func': wdi.unemp_avg
    },

    'unemp-year' : {
        'conf': 'wdi_csv',
        'func': wdi.unemp_year
    },

    'unemp-max': {
        'conf': 'wdi_csv',
        'func': wdi.unemp_max
    },

    'unemp-min': {
        'conf': 'wdi_csv',
        'func': wdi.unemp_min
    }
}
