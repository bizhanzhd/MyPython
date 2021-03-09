testo=input("Scriva il testo qui: ")
def play(test):
    A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a="abcdefghijklmnopqrstuvwxyz"
    n="123456789"
    digitcont=0
    lettercont=0
    for i in range(len(test)):
        if (test[i] in A) or (test[i] in a):
            lettercont+=1
        elif (test[i] in n):
            digitcont+=1
        else: continue
    return (lettercont,digitcont)
numbers=play(testo)
print("number of letters: ", numbers[0])
print("number of digits: ", numbers[1])