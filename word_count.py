import sys
from collections import Counter

def read_file(file_path):
    """Read the contents of a text file and return as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def calculate_word_frequency(text):
    """Calculate the frequency of each word in the given text."""
    words = text.split()
    return Counter(words)

def count_words(input_file, output_file):
    text = read_file(input_file)
    word_counts = calculate_word_frequency(text)

    with open(output_file, 'w') as file:
        for word, count in word_counts.items():
            file.write(f"{word}: {count}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python word_count.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        count_words(input_file, output_file)
