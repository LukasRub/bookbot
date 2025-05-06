from stats import (
    get_word_count,
    get_alphabetic_char_counts
)
import sys


def get_book_text(path_str):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        path_str (str): The path to the book file.
        
    Returns:
        str: The content of the book file.
    """
    with open(path_str, "r", encoding="utf-8") as fp:
        return fp.read()
    

def generate_report(path_str, word_count, char_counts: dict):
    """
    Generates a report of the word count and character counts.
    
    Args:
        path_str (str): The path to the book file.
        word_count (int): The number of words in the book.
        char_counts (dict): A dictionary where keys are characters (str) and values are their frequencies (int).
        
    Returns:
        str: A formatted report string.
    """
    output = [
        "============ BOOKBOT ============",
        f"Analyzing book found at {path_str}...",
        f"Found {word_count} total words",
        "--------- Character Count -------"
    ]
    for char, count in char_counts.items():
        output.append(f"{char}: {count}")
    output.append("============= END ===============")
    return "\n".join(output)


def main(path_str):
    """
    Main function to execute the script.
    """  
    # Get the text from the book file
    book_text = get_book_text(path_str)

    # Gather relevant statistics
    word_count = get_word_count(book_text)
    char_frequencies = get_alphabetic_char_counts(book_text)

    # Generate the report
    report_str = generate_report(path_str, word_count, char_frequencies)
    print(report_str)


if __name__ == "__main__":
    # Check if the correct number of command line arguments are provided
    # If not, exit the program with a non-zero status
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the path to the book file from command line arguments
    # and run the main function
    path_str = sys.argv[1] 
    main(path_str)