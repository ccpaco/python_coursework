#PART 1 
fruits = 'apple banana mango pineapple pear blueberry strawberry blackberry'
print(' ')
print('-- PART 1 --')
print(' ')
#split
ans1 = fruits.split()
print('0 - ',ans1)

#delete 1st way
ans2 = ans1.pop()
print('1 - ', ans1)  

#delete 2nd way 
ans3 = ans1[1:-1]
print('2 - ',ans3)

#delete 3rd way
del ans3[0]
ans4 = ans3
print('3 - ',ans4)

#sort
ans4.sort()
print('4 - ',ans4)

#add 1st way
ans4[-1] = 'magic apple'
ans5 = ans4
print('5 - ',ans5)

#add 2nd way
ans5.append('magic strawberry')
ans6 =ans5
print('6 - ',ans6)

#add 3rd way
ans7 = ans6 + ['magic banana']
print('7 - ',ans7)

#join and print string
joiner = ' ~ '
ans8 = joiner.join(ans7)
print('8 - ',ans8)

#PART 2
print(' ')
print('-- PART 2 --')
print(' ')

#nestedList
baseList = [1,2]
nestedList = [baseList, 3, 4]
print(nestedList)

# the * operator
print(baseList * 2)

#list slices
print(nestedList[1:])

# += operator
nestedList += [5,6]
print(nestedList)

# filter
cleanList = [0,2,4,6,8,10]
def myFilt(a):
  blank = []
  for i in a:
    if i > 5:
      blank.append(i)
  return blank

print(myFilt(cleanList))

#legal but wrong
s = cleanList.sort()
print(s) 
#no error but prints none