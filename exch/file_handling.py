""" Functions related to file(JSON) handling. """

import json

def set_default_base(new_base, filepath):
    """ set new default base currency """
    with open(filepath) as json_file:
        json_data = json.load(json_file)

    json_data['base'] = new_base

    with open(filepath, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

def set_default_target(new_target, filepath):
    """ set new default arget currency """
    with open(filepath) as json_file:
        json_data = json.load(json_file)

    json_data['target'] = new_target

    with open(filepath, 'w') as json_file:
        json.dump(json_data, json_file)

def get_default_base(filepath):
    """ get the currenct default base currency """
    with open(filepath) as json_file:
        json_data = json.load(json_file)
    return json_data['base']

def get_default_target(filepath):
    """ get the current default target currency """
    with open(filepath) as json_file:
        json_data = json.load(json_file)
    return json_data['target']
