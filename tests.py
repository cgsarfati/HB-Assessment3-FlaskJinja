"""Tests for UberMelon's Flask app."""

import unittest
import server


class UberMelonTests(unittest.TestCase):
    """Tests for the UberMelon site."""

    def setUp(self):
        """Code to run before every test."""

        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_homepage(self):
        """To make sure homepage is accessible."""

        result = self.client.get("/")
        self.assertIn("UberMelon's Most Loved Melons", result.data)


if __name__ == "__main__":
    unittest.main()
