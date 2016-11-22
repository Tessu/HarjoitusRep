import os
import sys

myargs = sys.argv

print myargs
argslen = len(myargs)

if argslen < 2:
	for file in os.listdir('.'):
		print file
elif argslen == 2:
	for file in os.listdir(myargs[1]):
		print file
else:
	print "Give only 1 argument"

