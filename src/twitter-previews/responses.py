def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    return lowered

def validate_twitter_url(url: str) -> bool:
    return True # TBD: check if url is a valid twitter url (can be twitter.com or t.co or x.com or others?)