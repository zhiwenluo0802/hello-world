import sys
from collections import Counter

def count_words(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    words = text.split()
    word_counts = Counter(words)

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
