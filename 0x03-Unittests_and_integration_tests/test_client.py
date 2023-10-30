#!/usr/bin/env python3
"""GithubOrgClient class's org modules."""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """GithubOrgClient class's."""
    @patch('client.GithubOrgClient.get_json')
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    def test_org(self, org, expected_result, mock_get_json):
        """GithubOrgClient class's org method."""
        client = GithubOrgClient(org)
        mock_get_json.return_value = expected_result

        self.assertEqual(client.org, expected_result)
        mock_get_json.assert_called_once_with(
                f'https://api.github.com/orgs/{org}')

    def test_public_repos_url(self, mock_org):
        """Define the known payload."""
        payload = [{'name': 'repo1'}, {'name': 'repo2'}, {'name': 'repo3'}]
        mock_org.return_value = payload
        client = GithubOrgClient("org_name")
        public_repos_url = client._public_repos_url
        expected_result = ["repo1", "repo2", "repo3"]
        self.assertEqual(public_repos_url, expected_result)


if __name__ == '__main__':
    unittest.main()
