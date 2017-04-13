import sys

#myargs = sys.argv

#word=list(myargs[1])
#wordlen = len(word)

#print word
#print wordlen

vowels_list = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "Y", "y"]
#n=0
#vowels_amount = 0

def is_vowel(character):
	if character in vowels_list:
		return True
	else:
		return False

def get_vowels_amount():
	n=0
	vowels_amount = 0
	word = get_word()
	wordlen = get_wordlength()
	while n < wordlen:
		if is_vowel(word[n]) == True:
			vowels_amount += 1
			n += 1
		else:
			n += 1
	print "Amount of vowels in the given word is: {}".format(vowels_amount)


def get_word():
	myargs = sys.argv
	word = list(myargs[1])
	return word

def get_wordlength():
	wordlen = len(get_word())
	return wordlen


def get_vowel_ascii(character):
		asc = ord(character)
		return asc

def sum_vowel_ascii():
	ascii_sum = 0
	word = get_word()
	for character in word:
		if is_vowel(character) == True:
			ascii_sum += get_vowel_ascii(character)
		else:
			pass
	print "Ascii value of vowels is: {}".format(ascii_sum)

if __name__ == "__main__":
	get_vowels_amount()
	sum_vowel_ascii()
