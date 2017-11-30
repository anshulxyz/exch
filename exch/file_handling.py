""" Functions related to default rates file. """

import json

def set_default_base(new_base, default_rates_filepath):
    """ set new default base currency """
    with open(default_rates_filepath) as json_file:
        json_data = json.load(json_file)

    json_data['base'] = new_base

    with open(default_rates_filepath, 'w') as json_file:
        json.dump(json_data, json_file)

def set_default_target(new_target, default_rates_filepath):
    """ set new default arget currency """
    with open(default_rates_filepath) as json_file:
        json_data = json.load(json_file)

    json_data['target'] = new_target

    with open(default_rates_filepath, 'w') as json_file:
        json.dump(json_data, json_file)

def get_default_base(default_rates_filepath):
    """ get the currenct default base currency """
    with open(default_rates_filepath) as json_file:
        json_data = json.load(json_file)
    return json_data['base']

def get_default_target(default_rates_filepath):
    """ get the current default target currency """
    with open(default_rates_filepath) as json_file:
        json_data = json.load(json_file)
    return json_data['target']
