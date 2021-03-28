#is_divisible
def is_divisible(x, y):
  return x % y == 0

#is_power
def is_power(a,b):
  #base if second argument being "1" and first is not
  if a != 1 and b==1:
    return False
  #base case for equality
  if a==b:
    return True 
  #passes base case, check is_divisible, recurse
  elif is_divisible(a,b):
    newSmall = int(a/b)
    #recursion call
    return is_power(newSmall,b)
  #if not divisible return False
  else: 
    return False
  
print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))

