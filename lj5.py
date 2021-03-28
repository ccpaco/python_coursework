prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter[0]=="O" or letter[0]=="Q":
      print(letter+"u"+suffix)
    else:
      print(letter + suffix)

drink = 'mango armaggedon'
def derp(word):
  mySlice = word
  for letter in mySlice:
    if letter[0]==' ': #just an attempt to understand empty chars in Py
      return drink + ' smoothie '
print(drink[-1:]) #last letter slice
print(drink[:]) #whole string
print(derp(drink)) #string concat via function