#!/usr/bin/env python3
"""Parameterize a unit test module."""
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function. """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Tests `access_nested_map`'s output."""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """exception message testing."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """a class defines TestGetJson."""
    @patch('requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Create a Mock object to simulate the response from requests.get.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('requests.get', return_value=mock_response) as mock_get:
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
