# good morning sumanth gowda

str=input("enter the string")
new_str = ''
for char in range (0,len(str)):
    if(str[char]=='o'):
        new_str += 'z'
    else:
        new_str += str[char]

print("new string:")
print(new_str)