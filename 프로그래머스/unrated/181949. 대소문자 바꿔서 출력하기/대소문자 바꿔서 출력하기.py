str = input()
output = ''

for c in str:
    if c.islower():
        output += c.upper()
    else:
        output += c.lower()
        
print(output)