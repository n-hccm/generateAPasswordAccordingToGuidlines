import convert_to_sha1

def check_deny_list(password: str) -> bool:
    """Check if the given hash is in the deny list."""
    hash = convert_to_sha1(password)
    with open("deny_list.txt", "r") as file:
        deny_list = file.read().splitlines()
    if hash in deny_list:
        return True
    else:
        return False

