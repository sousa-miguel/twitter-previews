import unittest
from src.responses import validate_twitter_url, get_response, validate_vxtwitter_url


class TestTwitterPreviews(unittest.TestCase):
    def setUp(self):
        self.valid_twitter_urls = [
            "https://twitter.com/username/status/1234567890",
            "https://t.co/username/status/1234567890",
            "https://x.com/username/status/1234567890",
        ]

        self.invalid_twitter_urls = [
            "https://not_twitter.com/username/status/1234567890",
            "https://twitter.com/username/status/not_a_number",
            "https://twitter.com/username/no_status/1234567890",
            "https://twitter.com/username/status/",
        ]

        self.get_response_test_cases = [
            (
                "https://twitter.com/username/status/1234567890",
                "https://vxtwitter.com/username/status/1234567890",
            ),
            (
                "https://t.co/username/status/1234567890",
                "https://vxtwitter.com/username/status/1234567890",
            ),
            (
                "https://x.com/username/status/1234567890",
                "https://vxtwitter.com/username/status/1234567890",
            ),
        ]

        self.valid_vxtwitter_urls = [
            "https://vxtwitter.com/username/status/1234567890",
            "https://vxtwitter.com/username/status/0987654321",
        ]

        self.invalid_vxtwitter_urls = self.valid_twitter_urls

    def test_validate_twitter_url_with_valid_urls(self):
        for url in self.valid_twitter_urls:
            self.assertTrue(validate_twitter_url(url))

    def test_validate_twitter_url_with_invalid_urls(self):
        for url in self.invalid_twitter_urls:
            self.assertFalse(validate_twitter_url(url))

    def test_get_response(self):
        for input_str, expected_output in self.get_response_test_cases:
            self.assertEqual(get_response(input_str), expected_output)

    def test_validate_vxtwitter_url_with_valid_urls(self):
        for url in self.valid_vxtwitter_urls:
            self.assertTrue(validate_vxtwitter_url(url))

    def test_validate_vxtwitter_url_with_invalid_urls(self):
        for url in self.invalid_vxtwitter_urls:
            self.assertFalse(validate_vxtwitter_url(url))


if __name__ == "__main__":
    unittest.main()
