import unittest
from unittest.mock import patch
from get_repo import connect


class TesttestApi(unittest.TestCase):
    @patch('GitHubApi.requests.get')
    def testNumberofRepo(self, mock):
        mock.get('https://api.github.com/users/sbahala/repos', text='success')
        self.assertEqual(connect('https://api.github.com/users/sbahala/repos'), 'success')

    def testCommit(self):
        commits = connect('sbahala', 'Triangle567_2A')
        self.assertNotEquals(commits, 4)


if __name__ == '__main__':
    unittest.main()
