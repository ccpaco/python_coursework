Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
#part 1
import math
def my_sqrt(a):
  x = 3
  while True:
     y = (x + a/x) / 2.0
     if y == x:
          break
     x = y
  return y

#part 2
def test_sqrt(a):
  #run our function for square roots
  y = my_sqrt(a)
  #save the argument to a variable. Just to keep clean
  passA = a
  #save what Python computes to another variable
  b = math.sqrt(a)
  #absolute value of the differences between ours and Python's
  diff = abs(y-b)
  #finally print out everything 
  print('a = ',passA,' | my_sqrt(a)=',y,' | math.sqrt = ',b,' | diff= ',diff)

#wrote a function to test numbers 1-25. Separating functions keeps code focused.
def im_lazy():
  i=1
  #while loop to run a=1 through a=25. Here we assign "a" using "i"
  while i<=25:
    test_sqrt(i)
    i+=1

#calls this function to call other functions
im_lazy()
