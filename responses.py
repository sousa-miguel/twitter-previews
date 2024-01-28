import re

# Constants
TWITTER_URLS = ["twitter.com", "t.co", "x.com"]
VXTWITTER_URL = "vxtwitter.com"

def get_response(user_input: str) -> str:
    """Replaces 'twitter.com', 't.co', or 'x.com' in the input str with 'vxtwitter.com'."""
    lowered: str = user_input.lower()
    for url in TWITTER_URLS:
        lowered = lowered.replace(url, VXTWITTER_URL)
    return lowered

def validate_twitter_url(url: str) -> bool:
    """
    Check if the url is a "valid" twitter url.
    A valid twitter url in this context contains "twitter.com", "t.co", or "x.com" followed by "/${username}/status/${tweet_number}/*".
    """
    pattern = r'(' + '|'.join(['//' + url for url in TWITTER_URLS]) + r')\/[^\/]+\/status\/\d+\/?.*'
    return bool(re.search(pattern, url))

def validate_vxtwitter_url(url: str) -> bool:
    """Checks if the url is already a vxtwitter url."""
    return VXTWITTER_URL in url