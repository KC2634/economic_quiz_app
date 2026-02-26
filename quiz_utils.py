import re  # used to check the name does not contain numbers

def clean_name(name):
    """
    Cleans the name by removing whitespace and converting to title case.
    That is a PURE function.
    """
    return name.strip().title()

def presence_check(name: str) -> bool:
    
    """
    Checks that a name has been provided.
    Pure. Returns True if the name is not empty.
    """
    return bool(name)

def length_check(name: str) -> bool:
    
    """
    Checks that the name length is within an acceptable range.
    Pure. Returns True if the name length is between 2 and 50 characters.
    """
    return 2 <= len(name) <= 50

def character_check(name: str) -> bool:
    
    """
    Checks that the name contains only valid characters.
    Pure. Returns True if the name has no numbers.
    """
    return not re.search(r"\d", name)

def pattern_check(name):
    return bool(re.fullmatch(r'[a-zA-Z-\s]+', name))

    """
    Checks that the name contains only letters, spaces or hyphens.
    """
