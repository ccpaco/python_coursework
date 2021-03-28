# Return a list of values for each key
# Create 3+ items

# myGames = "{ 'brand': 'Sony', 'model': 'Playstation 4','title': 'Call of Duty Warzone', 'genre': 'First Person Shooter', 'producer': 'Infinity Ward', 'year': 2020 }"

myGames = {
  "brand": "Sony",
  "model": "Playstation 4",
  "title": "Call of Duty Warzone",
  "genre": "First Person Shooter",
  "producer": "Infinity Ward",
  "year": 2020
}


# From Section 11.5 of: 
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 

def invert_dict(d):
     inverse = dict()
     for key in d:
          val = d[key]
          if val not in inverse:
               inverse[val] = [key]
          else:
               inverse[val].append(key)
     return inverse 


print(myGames)

print(invert_dict(myGames))