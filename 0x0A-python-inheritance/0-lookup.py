#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    
    Args:
    - obj: Any object
    
    Returns:
    - List of strings: Names of attributes and methods
    """
    return dir(obj)
