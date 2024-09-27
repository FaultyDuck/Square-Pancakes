with open('text.txt', 'r') as file:
    content = file.read()
    print(content)

'''
with open('text.txt', 'w') as file: #this overide
    file.write('')

with open('text.txt', 'a') as file: #this adds text
    file.write('')

with open('text.txt', 'r') as file: #this reads text
    content = file.read()
    print(content)
'''