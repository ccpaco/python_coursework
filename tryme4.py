def new_line():
  print('.')

def three_lines():
  new_line()
  new_line()
  new_line()

def nine_lines():
  three_lines()
  three_lines()
  three_lines()

def clear_screen():
  nine_lines() #line count 9
  nine_lines() #line count 18
  three_lines() #line count 21
  three_lines() # line count24
  new_line() #line count 25

nine_lines()
print("now calling clear_screen")
clear_screen()
