IntList = [2,5,2,8]

IntList.append(4)

IntList.pop(2)

StrList = ["henri", "antti", "kaisa"]

IntList.extend(StrList)

print "Prints combined Int and Str lists"
print IntList


harjdict = {"etunimi": 'Henri', 'sukunimi': 'thessler', 'paikkakunta': 'rovaniemi'}
harjdict['inception'] = [1]
print "\n Prints Dict and list inserted to that dict.\n"
print harjdict

dictlist = [2,3,"list"]

harjdict2 = {"keyword": "Key"}

dictlist.append(harjdict2)

harjdict3 = {"anotherkey": "Another key"}

dictlist.append(harjdict3)

print "\n Prints List where i have added two dictionarys to that list:\n"
print dictlist

print "\nPrinting 1 from there first list"
print harjdict['inception'][0]


