# Open a file
fo = open('text.txt', 'w') # write mode
# Get some info
print('Name: ', fo.name)
print('Is Closed: ', fo.closed)
print('Opening Mode:', fo.mode)
fo.write('I <3 Python')
fo.write(' and JavaScript')
fo.close()

fo = open('text.txt', 'a') # append mode
fo.write('I also like PHP')
fo.close()

fo = open('text.txt', 'r+')
print(fo.read(10))
fo.close()

fo = open('text2.txt', 'w+')
fo.write('This is my new file')
fo.close()