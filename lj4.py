import math
#Original Function - Commented out. Used temp. variable ans to track output
#def hypotenuse(a,b):
  #ans = (a**2) + (b**2)
  #c = math.sqrt(ans)
  #return c
#Version 2 - Cleaned up to one line
def hypotenuse(a,b):
  c = math.sqrt((a**2) + (b**2))
  return c
#test 
print(hypotenuse(3,4)) #Returns 5.0
print(hypotenuse(6,8)) #Returns 10.0
print(hypotenuse(5,12)) #Returns 13.0

#part 2 
#Original Function
#String Reverse function with for loop. Test for i.
#Doesn't work, Python .length is diff from JavaScript, so this gave an error. 
# def stringRev(myString):
#  for i in range(myString.length):
#    return i
#Wanted to experiment with string manipulation in Python so changed approach.
#Taken code from the Exercise 6.3 on Palindromes(Downey, 2015, p.61)
#Simple function to abbreviate a string to 3 letters
def stringShort(myString):
 return myString[0: 3]
print(stringShort("Sentence")) #prints Sen
print(stringShort("Alphabet")) #prints Alp
print(stringShort("Python")) #prints Pyt
#REFERENCES
#Downey, A. (2015). Think Python: How to think like a computer scientist.