#TODO: Download the deny list from the internet and check if the given hash is in the deny list

def check_deny_list(hash: str) -> bool:
    """Check if the given hash is in the deny list."""
    with open("deny_list.txt", "r") as file:
        deny_list = file.read().splitlines()
    if hash in deny_list:
        return True
    else:
        return False

