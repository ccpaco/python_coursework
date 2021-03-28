# importing the module
import ast
  
# reading the data from the file
with open('input.txt') as f:
    data = f.read()
  
print("Data type before reconstruction : ", type(data))
      
# reconstructing the data as a dictionary
d = ast.literal_eval(data)
  
print("Data type after reconstruction : ", type(d))
print(" ")
print(d)

def invert_dict(d):
     inverse = dict()
     for key in d:
          val = d[key]
          if val not in inverse:
               inverse[val] = [key]
          else:
               inverse[val].append(key)
     return inverse 

redone = str(invert_dict(d))

print(" ")
print(redone)

fout = open('output.txt','w')
fout.write(redone)

f.close()
fout.close()