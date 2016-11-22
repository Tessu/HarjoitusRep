# coding=utf-8

for num in range (101):
	if num % 3 == 0 and num > 0:
		print num
		print "Fizz"
	if num % 5 == 0 and num > 0:
		print num
		print "Buzz"
	if num % 3 == 0 and num % 5 == 0 and num >0:
		print num
		print "Fizz Buzz"


