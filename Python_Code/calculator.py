import sys

myargs = sys.argv

argslen = len(myargs)




if argslen > 3:
	num1=float(myargs[1])
	num2=float(myargs[2])
	operation=int(myargs[3])

	if operation == 1:
		add=num1 + num2
		print "Result from Add operation is {}".format(add)
	if operation == 2:
		substract = num1 - num2
		print "Result from substract operation is {}".format(substract)
	if operation == 3:
		multiply= num1 * num2
		print "Result from multiply operation is {}".format(multiply)
	if operation == 4:
		divide = num1 / num2
		print "Result from divide operation is {}".format(divide)
	if operation == 5:
		modulo = num1 % num2
		print "Result from modulo operation is {}".format(modulo)
	else:
		print "Give propper operation number"
else:
	print "Give 2 numbers and operation number from 1-5 to excecute mathematical" \
	 "operations\n1:Add\n2:Substract\n3:Multiply\n4:Divide\n5:Modulo"
