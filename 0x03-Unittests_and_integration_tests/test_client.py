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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Define the known payload."""
        payload = [{'name': 'repo1'}, {'name': 'repo2'}, {'name': 'repo3'}]
        with patch(
                'client.GithubOrgClient._public_repos_url',
                return_value="https://api.github.com/orgs/testorg/repos"):
            mock_get_json.return_value = payload
            client = GithubOrgClient("testorg")
            repos = client.public_repos()
            expected_result = ["repo1", "repo2", "repo3"]
            self.assertEqual(repos, expected_result)
        mock_get_json.assert_called_once()


if __name__ == '__main__':
    unittest.main()
