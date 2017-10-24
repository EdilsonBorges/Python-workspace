def sayHello(name = 'Guest'):
	print('Hello', name)

sayHello('Guest One')

num1 = 5

def getSum(num1, num2):
	num1 = num1 + 1
	return num1 + num2
print(getSum(6,3))

myList = [1,2,3,4]

def addOneToList(myList):
	myList.append(5)
	return

addOneToList(myList)
print(myList)