""" test the JSON file handling """

import pkg_resources
import json
from exch import file_handling

class TestFileHandling:
    """
    tests for reading/writing default currency to JSON file.
    The tests have to be run in the order they are, because in the first two
    tests we are setting the default values. In the next two we are getting the
    default values which were set by the first two sets.
    """
    new_base = 'PHP'
    new_target = 'CAD'
    filepath = pkg_resources.resource_filename('exch', 'data/defaults.json')

    def test_set_default_base(self):
        file_handling.set_default_base(self.new_base, self.filepath)
        with open(self.filepath) as json_file:
            json_data = json.load(json_file)
        assert json_data['base'] == self.new_base

    def test_set_default_target(self):
        file_handling.set_default_target(self.new_target, self.filepath)
        with open(self.filepath) as json_file:
            json_data = json.load(json_file)
        assert json_data['target'] == self.new_target

    def test_get_default_base(self):
        assert self.new_base == file_handling.get_default_base(self.filepath)

    def test_get_default_target(self):
        assert self.new_target == file_handling.get_default_target(self.filepath)
