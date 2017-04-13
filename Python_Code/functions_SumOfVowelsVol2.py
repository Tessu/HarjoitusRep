import sys

#myargs = sys.argv

#word=list(myargs[1])
#wordlen = len(word)

#print word
#print wordlen

vowels_list =["a","e","i","o","u","y"]
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
	while n<wordlen:
		if is_vowel(word[n]) == True:
			vowels_amount +=1
			n+=1
		else:
			n+=1
	return vowels_amount


def get_word():
	myargs=sys.argv
	word=list(myargs[1])
	return word

def get_wordlength():
	wordlen = len(get_word())
	return wordlen




if __name__ == "__main__":
	vowels_amount = get_vowels_amount()
	print "Amount of vowels in the given word is: {}".format(vowels_amount)

