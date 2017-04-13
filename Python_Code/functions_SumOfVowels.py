import sys

myargs = sys.argv

word=list(myargs[1])
wordlen = len(word)

print word
print wordlen

vowels_list =["a","e","i","o","u","y"]
n=0
vowels_amount = 0

def is_vowel(character):
	if character in vowels_list:
		return True
	else:
		return False




if __name__ == "__main__":
	while n<wordlen:
		if is_vowel(word[n]) == True:
			vowels_amount +=1
			n+=1
		else:
			n+=1

	print "Amount of vowels in the given word is: {}".format(vowels_amount)


