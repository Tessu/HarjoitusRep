# coding=utf-8 sallii skandit
mylist = [1, 2, 3, 4]
print mylist

print mylist[3]
print mylist[0]
print mylist.insert(1, False)
print mylist.pop(2)#Poistaa halutusta paikasta tai postaa listan viimeisen arvon ilman maaritysta
mylist.append(True)
print mylist

print [1]

print (1,) #(1,) tuple ilman pilkkua ei ole tuple
#ääääää

listlen = len(mylist)
print listlen

print "Listan pituus: {}".format(listlen)

print "henri rules"[:5] #printing 0-5 memoryslot

print "henri rules"[2:3] #printing memoryslots 2 and 3

mydict = {'mykey': 12, 'totuus': False}

print mydict['mykey'] #Print value or string behind key 'mykey'
print mydict.get('key', 'ei loydy') #Trying to print value or string behind key 'key, if not found print "ei loydy"'

#How to Delete from lists

del mydict['mykey']
print mydict
del mylist[1]
print mylist