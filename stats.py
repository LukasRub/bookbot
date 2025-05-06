from collections import Counter


def get_word_count(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())


def get_alphabetic_char_counts(text):
    """
    Counts the frequency of alphabetic characters in a given text.
    
    Args:
        text (str): The text to count characters in.
        
    Returns:
        Counter: A Counter object with character frequencies.
    """
    char_frequencies = Counter(char for char in text.lower() if char.isalpha())
    return {char: count for char, count in char_frequencies.most_common()}

