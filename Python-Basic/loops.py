people = ['John', 'Sarah', 'Tim', 'Bob']

for person in people:
	print('Current person: ', person)

print()

# iterate by seq index
for i in range(len(people)):
	print('Current person: ', people[i])

for i in range(0, 10):
	print(i)

# while loop
count = 0
while count < 10:
	print('Count: ', count)
	count += 1
	if count == 5:
		break