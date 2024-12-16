import json

# Open and load the JSON file
with open('./PokeTCG.json', 'r',  encoding='utf-8-sig') as file:
    data = json.load(file)

# Print the loaded data (optional)
#print the name of all fighting type pokemon

#print all cards from the set "HeartGold & SoulSilver"
for pokemon in data:
    try:
       if "Fighting" in pokemon["types"]:
          print("Fighting type found!")
          


#print all cards where the averageSellPrice is greater than 1.5
