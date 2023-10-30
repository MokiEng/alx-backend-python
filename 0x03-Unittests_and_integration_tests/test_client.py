#!/usr/bin/env python3
"""GithubOrgClient class's org modules."""

import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from unittest.mock import Mock
from unittest.mock import PropertyMock
from parameterized import parameterized,  parameterized_class
from typing import Dict
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from requests import HTTPError


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Mock the public_repos method to return a known payload."""
        with patch('client.GithubOrgClient.public_repos') as mock_public_repos:
            mock_public_repos.return_value = [repo]
            client = GithubOrgClient("testorg")
            result = client.has_license(license_key)
            self.assertEqual(result, expected_result)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """integration tests for the `GithubOrgClient` class."""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            """ to return http errot"""
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
