import re
testo=input("Scriva il testo qui: ")
letters=re.findall("[A-Za-z]",testo)
digits=re.findall("[1-9]",testo)

print("number of letters: ", len(letters))
print("number of digits: ", len(digits))