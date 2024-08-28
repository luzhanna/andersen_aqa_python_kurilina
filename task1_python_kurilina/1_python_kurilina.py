number = input('Input the number: ')

try:
  number = float(number)
except:
  exit()

if number > 7:
  print('Hello')