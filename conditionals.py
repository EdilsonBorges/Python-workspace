x = 7

if x < 6:
	print('This is tue')

if x < 6:
	print('This is true')
else:
	print('This is false')

color = 'red'

if color == 'red':
	print('color is red')
elif color == 'blue':
	print('color is blue')
else:
	print('color is not red and blue')

if color == 'red':
	if x < 10:
		print('Color is red and x is less than 10')

if color == 'red' and x < 10:
	print('Color is red and x is less than 10')