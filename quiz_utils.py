import re  # used to check the name does not contain numbers

def clean_name(name):
    """
    Cleans the name.
    
    Cleans the name by removing whitespace and converting to title case.
    That is a Pure function.

    Parameters:
    name(str): The user's name inputed in the messagebox.

    Returns:
    clean_name: Returns 'name' without whitespace and converts to title case

    """
    return name.strip().title()

def presence_check(name: str) -> bool:
    
    """
    Checks that a name has been provided.

    This functions checks the name box is not blank.
    This function is Pure. 

    Parameters:
    name(str): The user's name inputed in the messagebox.
    
    Returns:
    bool: True if the name is not empty, False if the name is empty

    """
    return bool(name)

def length_check(name: str) -> bool:
    
    """
    Checks that the name length is within an acceptable range.

    This function checks that the name length is between 2 and 50 characters.
    This is a Pure function. 
    
    Parameters:
    name(str): The user's name inputed in the messagebox.
    
    Returns:
    bool: True if the name length is between 2 and 50 characters, False if the name is 1 character or more than 50 characters.

    """
    return 2 <= len(name) <= 50

def character_check(name: str) -> bool:
    
    """
    Checks that the name contains only valid characters.

    This function checks that the name does not contain any numbers.
    This is a Pure function. 
    
    Parameters:
    name(str): The user's name inputed in the messagebox.

    Returns:
    bool: True if the name has no numbers, False if the name contains any numbers.
    """
    return not re.search(r"\d", name)

def pattern_check(name):
    """
    Checks that the name contains no invalid punctuation.

    This function checks the name does not contain any other punctuation other than hyphens.

    Parameters:
    name(str): The user's name inputed in the messagebox.

    Returns:
    bool: Returns True if the function does not contain any punctuation other than hyphens, False if the name contains other punctuation.

    """
    return bool(re.fullmatch(r'[a-zA-Z-\s]+', name))

    
