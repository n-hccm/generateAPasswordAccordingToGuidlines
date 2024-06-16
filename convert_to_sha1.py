import hashlib

#todo: Check sha1 hash actually works. oh it do
def convert_to_sha1(text: str) -> str:
    """Converts a string to a sha1 hash."""
    return hashlib.sha1(text.encode()).hexdigest()

