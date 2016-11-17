#Some of the prints are worng, initial idea was to search ints and string from the list
#but since it inserts all values as a string the point was a bit lost.
#Could do with conversion but would need loops and error management which i havent learned yet


import sys

myargs = sys.argv

#Excercise 1
print "Print all"
print myargs

argslen=len(myargs)
#Excercise 6
#Code did not work without arguments, here is the fix
if argslen > 1:

	#Excercise 2
	print "Print everything but filename"
	print myargs[1:]

	#Excercise 3
	print "Print only first value"
	print myargs[1]

	#Excercise 4
	if type(myargs[1]) == str:
		print "Print the first value only if it is of type int"
		print myargs[1]

	#Excercise 5
	
	if type(myargs[1]) == str:
		print "Print the first value only if it is of type int"
		print myargs[1]

	if type(myargs[2]) == str:
		print "Also prints 2nd value if it is a string"
		print myargs[2]
else:
	print "No Arguments"
