#!/usr/bin/env python3
"""Parameterize a unit test module."""
import unittest
from parameterized import parameterized
from utils import access_nested_map


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

    parameterized.expand([
        ({}, ("a",), "a not found in nested_map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in dictionary")
    ])

    def test_access_nested_map_exception(
            self,
            nested_map, path,
            expected_exception_message):
        """exception message testing."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_exception_message)


if __name__ == '__main__':
    unittest.main()
