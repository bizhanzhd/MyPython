text=open('words.txt').read()

def palindrome(parola):
    parola=parola.strip()
    lung=len(parola)
    meta=int(lung/2)

    for i in range(meta):
        if parola[i]!=parola[lung-1-i]:
            flag= False
            break
        else:
            flag=True
            continue
    if flag== True:
        print(parola)

words=text.split()
for word in words:
    palindrome(word)