numbers = [float(i) for i in input('Input numbers divided by commas: ').split(',')]

numbers = list(map(lambda x: x*3, numbers))
print (numbers)
