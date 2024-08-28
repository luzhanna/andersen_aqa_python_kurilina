def main():
	numbers = input('Input numbers divided by commas: ').split(',')
	try:
		numbers = [float(s.strip()) for s in numbers]
		numbers = list(map(lambda x: x*3, numbers))
		print (numbers)
	except:
		exit()


if __name__ == '__main__':
	main()