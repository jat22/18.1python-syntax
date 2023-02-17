

def print_upper_words(words, letters):
	"""Pass in list of words and a list of letters.
		Each words that starts with a provided letter will be returned capitalized
	"""
	
	for word in words:
		word = word.upper()
		for letter in letters:
			letter = letter.upper()
			if word.startswith(letter):
				print(word)

