# A page meant to practice with various forms of pulling keys and values from created python dictionaries.
# This page led me to create the second practice page (where I changed the dictionary format according to my program
# requirements, DictionaryTwoPractice.py.
# In the DictionaryTwoPractice.py, I successfully pulled only a value from a specified key in the dictionary.

# Libraries
import pandas as pd

locationDict = {"country1":{"name" : "China", "binary": 418464229443},
                "country2":{"name":"USA","binary" : 4281173},
                "country3":{"name":"Russia","binary" : 107105536406866},
                "region1":{"name":"Asia","binary" : 1634300737},
                "region2":{"name":"Europe","binary" : 111533580514629},}


pdDict = pd.DataFrame(locationDict)
pd.set_option('display.max_rows', 1000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

print('\n')
print("locationDict: \n" )
print(locationDict)
print("\n\n")
# output:
# locationDict:
#
# {'country1': {'name': 'China', 'binary': 418464229443}, 'country2': {'name': 'USA', 'binary': 4281173}, 'country3': {'name': 'Russia', 'binary': 107105536406866}, 'region1': {'name': 'Asia', 'binary': 1634300737}, 'region2': {'name': 'Europe', 'binary': 111533580514629}}

print("pdDict: \n")
print(pdDict)
print("\n\n")
# output:
# pdDict:
#
#             country1 country2         country3     region1          region2
# name           China      USA           Russia        Asia           Europe
# binary  418464229443  4281173  107105536406866  1634300737  111533580514629

print("Values: \n")
print(locationDict.values())
print("\n")
# output:
# Values:
#
# dict_values([{'name': 'China', 'binary': 418464229443}, {'name': 'USA', 'binary': 4281173}, {'name': 'Russia', 'binary': 107105536406866}, {'name': 'Asia', 'binary': 1634300737}, {'name': 'Europe', 'binary': 111533580514629}])

print("Keys: \n")
print(locationDict.keys())
print("\n")

# output:
# Keys:
#
# dict_keys(['country1', 'country2', 'country3', 'region1', 'region2'])

print("Items: \n")
print(locationDict.items())
print("\n")

# output:
# Items:
#
# dict_items([('country1', {'name': 'China', 'binary': 418464229443}), ('country2', {'name': 'USA', 'binary': 4281173}), ('country3', {'name': 'Russia', 'binary': 107105536406866}), ('region1', {'name': 'Asia', 'binary': 1634300737}), ('region2', {'name': 'Europe', 'binary': 111533580514629})])


# reference: https://stackoverflow.com/questions/48006690/python-how-to-print-dictionary-key-and-its-values-in-each-line
print(locationDict.get("country1"))
country1list = locationDict.get("country1")
for k, v in country1list.items():
    print("{}".format(v))

print("\n")
    
# output:
# {'name': 'China', 'binary': 418464229443}
# China
# 418464229443


for k, v in country1list.items():
    print("{}".format(v))

# output:
# China
# 418464229443