import random

lettura = open('words.txt',"r")
scrittura = open('risultato.txt',"w")

stringa = lettura.read()
myList  = stringa.split()


while len(myList)!=0:
    seed=random.randint(0, len(myList)-1)
    if myList[seed]:
        result=myList[seed]
        scrittura.write(result+"\n")
        myList.remove(result)