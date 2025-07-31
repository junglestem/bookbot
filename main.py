from stats import get_book_words, get_book_text, get_book_characters, sort_book_characters
import sys

def main():
	if len(sys.argv) == 2:
		book_path = sys.argv[1]
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	print ("============ BOOKBOT ============")
	print (f"Analyzing book found at {book_path}...")
	print ("----------- Word Count ----------")
	print (f"Found {get_book_words(get_book_text(book_path))} total words")
	print ("--------- Character Count -------")
	sorted_book_characters = sort_book_characters(get_book_characters(get_book_text(book_path)))
	for key, value in sorted_book_characters.items():
		print (f"{key}: {value}")
	print ("============= END ===============")

main()
