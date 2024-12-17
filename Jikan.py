import json
from tabnanny import check

# Open and load the JSON file
with open('Jikan.json', 'r',  encoding='utf-8-sig') as file:
    data = json.load(file)

# Print the loaded data (optional)
print(data)

#print all anime whose synopsis has more than 50 characters in it
for synopsis in data['data']:
   try:    
      if len(synopsis) => 50:
    except synopsis < 50:
         print(synopsis)

## Print all anime that stopped airing before 2015
for airing in data['data']:
    try:
        if airing = False
            print["it stopped airing"]
        else: 
