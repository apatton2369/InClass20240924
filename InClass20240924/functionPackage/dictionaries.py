# dictionaries.py

def demo():
    """
    demonstrate basic dictionary stuff
    """
myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
print(myDictionary)

#iterate over the dictionary by key
for key in myDictionary.keys():
    print(key)

#Iterate by key/value
for item in myDictionary.items():

#Iterate by value
 for value in myDictionary.values():
    print(value)

#Add a key/value pair to the dictionary
myDictionary["Michigan State"] = "Spartans"

print(len(myDictionary))

#cause an exception
# add try / except logic to handle this
try:
    print(myDictionary["Ohio State"])
except:
    print("Ohio State is an invalid key")

#remove Xavier by key and print the entire dictionary
myDictionary.pop('Xavier' , None)
print(myDictionary)

# create another dictionary called newTeams
# add several key/value pairs
# combine that with myDictionary and print results
newTeams = {"Ohio":"Bobcats", "Bowling Green" : "Falcons", "West Virginia": "Mountaineers"}
myDictionary.update(newTeams)
print(myDictionary)