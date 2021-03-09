# TRIS
def vincitore(mosse):
    flag=0
#horizontal winning
    if mosse['1']== "X" and mosse['2']== "X" and mosse['3']== "X" : flag=1
    elif mosse['1']== "O" and mosse['2']== "O" and mosse['3']== "O" : flag=2

    elif mosse['4']== "X" and mosse['5']== "X" and mosse['6']== "X" : flag=1
    elif mosse['4']== "O" and mosse['5']== "O" and mosse['6']== "O" : flag=2

    elif mosse['7']== "X" and mosse['8']== "X" and mosse['9']== "X" : flag=1
    elif mosse['7']== "O" and mosse['8']== "O" and mosse['9']== "O" : flag=2
#vertical winning
    elif mosse['1']== "X" and mosse['4']== "X" and mosse['7']== "X" : flag=1
    elif mosse['1']== "O" and mosse['4']== "O" and mosse['7']== "O" : flag=2

    elif mosse['2']== "X" and mosse['5']== "X" and mosse['8']== "X" : flag=1
    elif mosse['2']== "O" and mosse['5']== "O" and mosse['8']== "O" : flag=2

    elif mosse['3']== "X" and mosse['6']== "X" and mosse['9']== "X" : flag=1
    elif mosse['3']== "O" and mosse['6']== "O" and mosse['9']== "O" : flag=2
#diagonal winning
    elif mosse['1']== "X" and mosse['5']== "X" and mosse['9']== "X" : flag=1
    elif mosse['1']== "O" and mosse['5']== "O" and mosse['9']== "O" : flag=2

    elif mosse['3']== "X" and mosse['5']== "X" and mosse['7']== "X" : flag=1
    elif mosse['3']== "O" and mosse['5']== "O" and mosse['7']== "O" : flag=2

    return flag

def partita():
    while True:
        for giocatore in giocatori:
            g=input(f"{giocatore}: Please enter a box number: ")
            if (int(g)>9):
                print("Enter the numbers in range")
                g=input(f"{giocatore}: Please enter a box number: ")
            if g in controllist:
                print("You can not choose same boxes")
                g=input(f"{giocatore}: Please enter a box number: ")
            controllist.append(g)
            #print(controllist)
            if giocatore==giocatore1: mos[g]="X"
            if giocatore==giocatore2: mos[g]="O"
            show=str()
            for key in mos:
                show=show + mos[key]+" "
                #print(show)
            print("          "+show[0:6])
            print("          "+show[6:12])
            print("          "+show[12:18])

            if vincitore(mos)==1:
                print(f"{giocatore1} has won! ")
                break
            elif vincitore(mos)==2:
                print(f"{giocatore2} has won! ")
                break
        if len(controllist)==8:
            print("You both suck!")
            newgame=input("to play again press enter: ")
            if newgame=="enter": continue

giocatore1=input("First Player: ")
giocatore2=input("First Player: ")
giocatori=[giocatore1,giocatore2]
print("1 2 3\n4 5 6\n7 8 9")
controllist=list()
mos={'1': "#",
     '2': "#",
     '3': "#",
     '4': "#",
     '5': "#",
     '6': "#",
     '7': "#",
     '8': "#",
     '9': "#"}

partita()
