import sys

myargs = sys.argv
print myargs

if 1 == 1:
	print "yks on yks"


if 1 == 1:
	pass #pass is placeholder

myvar = None

if myvar is not None:
	print "vau"

elif myvar is None:
	print "mynone"

else:
	print "else"

print type(1)