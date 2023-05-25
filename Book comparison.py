import requests 
import string

def count_unique_words(book_url):
    # Download the book from Project Gutenberg
    response = requests.get(book_url)
    book_text = response.text

    # Remove punctuation and convert to lowercase
    translator = str.maketrans("", "", string.punctuation)
    book_text = book_text.translate(translator).lower()

    # Split the text into words
    words = book_text.split()

    # Count the number of unique words
    unique_words = set(words)
    num_unique_words = len(unique_words)

    # Return the number of unique words
    return num_unique_words, len(words)

# URLs of the books from Project Gutenberg
book1_url = "https://www.gutenberg.org/cache/epub/345/pg345.txt"
book2_url = "https://www.gutenberg.org/cache/epub/70856/pg70856.txt"

# Count unique words and total words for each book
book1_unique_words, book1_total_words = count_unique_words(book1_url)
book2_unique_words, book2_total_words = count_unique_words(book2_url)

# Compare the number of unique words
if book1_unique_words > book2_unique_words:
    print("Book 1 has more unique words.")
elif book2_unique_words > book1_unique_words:
    print("Book 2 has more unique words.")
else:
    print("Both books have the same number of unique words.")

# Compare the ratio of unique to total words
book1_ratio = book1_unique_words / book1_total_words
book2_ratio = book2_unique_words / book2_total_words

if book1_ratio > book2_ratio:
    print("Book 1 has a higher ratio of unique to total words.")
elif book2_ratio > book1_ratio:
    print("Book 2 has a higher ratio of unique to total words.")
else:
    print("Both books have the same ratio of unique to total words.")