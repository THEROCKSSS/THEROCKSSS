import unittest

from scripts import generate_repos


class RecentRepositoriesTests(unittest.TestCase):
    def test_originals_and_forks_are_labeled_and_old_repos_excluded(self):
        repos = [
            {"name": "fresh", "html_url": "https://github.com/THEROCKSSS/fresh", "created_at": "2026-09-21T00:00:00Z", "fork": False, "private": False, "description": "<b>New</b>"},
            {"name": "forked", "html_url": "https://github.com/THEROCKSSS/forked", "created_at": "2026-09-22T00:00:00Z", "fork": True, "private": False, "description": "A fork"},
            {"name": "old", "html_url": "https://github.com/THEROCKSSS/old", "created_at": "2026-09-20T00:00:00Z", "fork": False, "private": False},
        ]
        result = generate_repos.render(repos)
        self.assertIn("[fresh](https://github.com/THEROCKSSS/fresh) | Original", result)
        self.assertIn("[forked](https://github.com/THEROCKSSS/forked) | Fork", result)
        self.assertNotIn("[old]", result)
        self.assertNotIn("<b>", result)
        self.assertIn("2 public repositories", result)


if __name__ == "__main__":
    unittest.main()
