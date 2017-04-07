import os
import sys


input1 = raw_input("Enter amount: ")
input1 = float(input1)
print "1.From Euro to US Dollar\n2.From US Dollar to Euro"


input2 = raw_input("Choose Conversion: ")
input2 = float(input2)
while input2<1 or input2>2:
	print"please input correct option"
	input2 = raw_input("Choose Currency: ")

if input2 == 1:
	input1*=1.06
	print"Conversion is {}Dollars".format(input1)

elif input2 == 2:
	input1*=0.94
	print"Conversion is {}Euros".format(input1)