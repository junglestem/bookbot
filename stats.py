def get_book_text(path_to_file):
        with open(path_to_file) as f:
                file_contents = f.read()
        return file_contents

def get_book_words(book_text):
        return len(book_text.split())

def get_book_characters(book_text):
	book_characters = {}
	temp_book_text = book_text.lower()
	for i in range(0, len(temp_book_text)):
		if temp_book_text[i].isalpha() and temp_book_text[i] not in book_characters:
			book_characters[temp_book_text[i]] = 1
		elif temp_book_text[i].isalpha():
			book_characters[temp_book_text[i]] += 1
	return book_characters

def sort_book_characters(book_characters):
	sorted_book_items = sorted(book_characters.items(), key=lambda item: item[1], reverse=True)
	return dict(sorted_book_items)
