import os
import sys

myargs = sys.argv

argslen=len(myargs)

print myargs

print "print"

print myargs[1:]
print argslen

palindrome = str(myargs[1])

print palindrome

list(palindrome)

listlen = len(palindrome)

print listlen


revpalindrome = list(reversed(palindrome))
n=int(0)
while n < listlen:
	if palindrome[n] == revpalindrome[n]:
		n+=1
		continue
	else:
		break

if n==listlen:
	print "Word is a palindrome"

else:
	print "Word is not a palindrome"