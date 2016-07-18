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

    'gini-year': {
        'conf': 'wdi_csv',
        'func': wdi.gini_year
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

    'desemp' : {
        'conf': 'wdi_csv',
        'func': wdi.desemp
    },

    'desemp-avg' : {
        'conf': 'wdi_csv',
        'func': wdi.desemp_avg
    },

    'desemp-year' : {
        'conf': 'wdi_csv',
        'func': wdi.desemp_year
    }
}
