# coding=utf-8

mylist = [1,2,3,4,5]

for number in mylist:

	if number == 3:
		continue	#If term is met it starts loop over from the next value
		break #Stops loop excecution


	print number

print "\n"


#print range(5)

for num in range (1,5):
	print num

num1 = 0

while num1 < 5: 
	print "never gonna give up"
	num1 += 1


mytuple = (1,2,3)
mylist = [1,2,3]

a, b, _ = mytuple #Takes the 3rd value but doesnt use it basicly ignoring it

print a
print b
#print c

mylist = [(1, "Henri"), (2, "Alex"),(False, "Nobody")]

for id, name in mylist:
	print id, name

mydict = {'key': 1, 'somekey': False}

for value in mydict.values():
	print value

for value in mydict.keys():
	print value

for value in mydict.items():
	print value
print "\n"

print mydict.keys()
print mydict.values()
print mydict.items()

for key, value in mydict.iteritems():
	print key, value

