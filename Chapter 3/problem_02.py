"""Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
''' """
name = input("Enter name: ")
date = input("Enter date: ")

# using f string
print(f'''Dear {name},
You are selected!
{date}''') 

# using replace function
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
''' 
print(letter.replace("<|Name|>", name).replace("<|Date|>", date)) 
