#function nimessä käytetään verbiä, funktio tekee jotain

def get_name():
	return "Jim"


if True == True:
	print "trolololo"



name=get_name()


def sum_point(x, y): #muuttujien olla kuvaavie esim x_coord
	print x + y

sum_point(14, 15)

def sum_point(x_coord, y_coord=1):	#y default arvo on 1 jos ei anneta y:n arvoa, default arvo voi olla vain jälkimmäinen
	return x_coord + y_coord

print sum_point(5)

def sum_all(*numbers):
	sum=0
	for number in numbers:
		sum+= number
	return sum

print sum_all(4, 3, 2, 6)


def sum_for_me(num, name):
	print name 
	return num

print sum_for_me(name="Jim", num=5)
print sum_for_me(5, name="Jim")


def sum_for_me(num, **kwargs):
	print names['name']
	return num

print sum_for_me(5, name="Jim", lastname="Toddler")

def sum_for_me(*args, **kwargs):
	print args, kwargs

print sum_for_me(5,name="jim", lastname="toddler")



def next_function(num1, num2):
	print num1, num2


def sum_for_me(*args, **kwargs):
	return next_function(*args)


if __name__ == "__main__":
	print sum_for_me(5, 7, name="Jim", last_name="toddler")












