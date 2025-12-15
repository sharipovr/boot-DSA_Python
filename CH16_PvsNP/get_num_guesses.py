def get_num_guesses(length):
    """
    Calculates the total number of possible passwords of a given length and shorter.
    Only 26 lowercase English letters can be used.
    
    For example, for length 3:
    26 + 26^2 + 26^3 = 26 + 676 + 17576 = 18278
    
    Args:
        length: The password length
    
    Returns:
        The total number of possible passwords of that length and shorter
    """
    total = 0
    
    # Sum all possibilities from length 1 to the given length
    # For each length i, there are 26^i possible passwords
    for i in range(1, length + 1):
        total += 26 ** i
    
    return total
