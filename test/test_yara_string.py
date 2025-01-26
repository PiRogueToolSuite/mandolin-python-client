# coding: utf-8

"""
    Mandolin

    Micro-service to analyze and convert files

    The version of the OpenAPI document: 1.0.0
    Contact: contact@defensive-lab.agency
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from mandolin_python_client.models.yara_string import YaraString

class TestYaraString(unittest.TestCase):
    """YaraString unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> YaraString:
        """Test YaraString
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `YaraString`
        """
        model = YaraString()
        if include_optional:
            return YaraString(
                identifier = '',
                instances = [
                    mandolin_python_client.models.yara_string_instance.YaraStringInstance(
                        matched_length = 56, 
                        offset = 56, 
                        plaintext = '', )
                    ]
            )
        else:
            return YaraString(
                identifier = '',
        )
        """

    def testYaraString(self):
        """Test YaraString"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
