import pyperclip
import re

#Open file and declare empty list and variable
#x = open("logs.txt","r")

x = pyperclip.paste()
#print(x)
y = []
z = ""

#Regex for "host", strip blankspace, add to empty list
for line in x.splitlines():
    if re.match("(H|h)ost", line):
        line.rstrip().lstrip()
        y.append(line)

#Deduplicate
y = set(y)

#Remove "Hosts: " and transfer from list to variable
for i in y:
    i = re.sub("Host: ", "", i)
    z += i + "\r\n"

#Send your sweet new list to the clipboard

#print(z)
pyperclip.copy(z)
#print("Copied the list to clipboard.")




#x.close()