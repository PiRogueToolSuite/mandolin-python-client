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

from mandolin_python_client.api.analyzers_api import AnalyzersApi


class TestAnalyzersApi(unittest.TestCase):
    """AnalyzersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AnalyzersApi()

    def tearDown(self) -> None:
        pass

    def test_analyze_with_tika_analyzer_tika_post(self) -> None:
        """Test case for analyze_with_tika_analyzer_tika_post

        Analyze With Tika
        """
        pass

    def test_analyze_with_yara_analyzer_yara_post(self) -> None:
        """Test case for analyze_with_yara_analyzer_yara_post

        Analyze With Yara
        """
        pass


if __name__ == '__main__':
    unittest.main()
