import re 

with open('row.txt', 'r') as file:
    text = file.read()

#text=input()
tx = re.findall(r"[a-z][_][a-z]", text)
print(tx)