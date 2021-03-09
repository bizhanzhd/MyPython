# Sudoku
import random

# Consideriamo tutta la tabella come una linea dei numeri:
#sudoku sarebbe una lista con contenuto dei numeri randomici
#stampando sudoku puoi dimostrare la tabella
sudoku=list()

#gli indici delle celle di ogni riga: Lines=dict()
#gli indici delle celle di ogni colonna: columns=dict()
#gli indici delle celle di ogni casella: cells=dict()
lines={1:[0,1,2,3,4,5,6,7,8],
       2:[9,10,11,12,13,14,15,16,17],
       3:[18,19,20,21,22,23,24,25,26],
       4:[27,28,29,30,31,32,33,34,35],
       5:[36,37,38,39,40,41,42,43,44],
       6:[45,46,47,48,49,50,51,52,53],
       7:[54,55,56,57,58,59,60,61,62],
       8:[63,64,65,66,67,68,69,70,71],
       9:[72,73,74,75,76,77,78,79,80]}
columns={1:[0,9,18,27,36,45,54,63,72],
         2:[1,10,19,28,37,46,55,64,73],
         3:[2,11,20,29,38,47,56,65,74],
         4:[3,12,21,30,39,48,57,66,75],
         5:[4,13,22,31,40,49,58,67,76],
         6:[5,14,23,32,41,50,59,68,77],
         7:[6,15,24,33,42,51,60,69,78],
         8:[7,16,25,34,43,52,61,70,79],
         9:[8,17,26,35,44,53,62,71,80]}
cells={1:[0,1,2,9,10,11,18,19,20],
       2:[3,4,5,12,13,14,21,22,23],
       3:[6,7,8,15,16,17,24,25,26],
       4:[27,28,29,36,37,38,45,46,47],
       5:[30,31,32,39,40,41,48,49,50],
       6:[33,34,35,42,43,44,51,52,53],
       7:[54,55,56,63,64,65,72,73,74],
       8:[57,58,59,66,67,68,75,76,77],
       9:[60,61,62,69,70,71,78,79,80]}

index=0
row=1
col=1

while True:
    #siamo in una cella (numero=index)
    #rand sarebbe tot possibilita che abbiamo in questa cella
    #dopo avremo 3 controlli per elliminare i valori non desiderati
    rand=[1,2,3,4,5,6,7,8,9]
    # print("*******index = ",index)
    row = ((index+row)//10)+1
    col = (index+row)%10
    # print("******row= ",row)
    # print("********column= ",col)
    if (row in [1,2,3]) & (col in [1,2,3]):
        cel=1
    elif (row in [1,2,3]) & (col in [4,5,6]):
        cel=2
    elif (row in [1,2,3]) & (col in [7,8,9]):
        cel=3
    elif (row in [4,5,6]) & (col in [1,2,3]):
        cel=4
    elif (row in [4,5,6]) & (col in [4,5,6]):
        cel=5
    elif (row in [4,5,6]) & (col in [7,8,9]):
        cel=6
    elif (row in [7,8,9]) & (col in [1,2,3]):
        cel=7
    elif (row in [7,8,9]) & (col in [4,5,6]):
        cel=8
    elif (row in [7,8,9]) & (col in [7,8,9]):
        cel=9

    # print("*************** Cell=",cel)
    #Comparazione del rand con gli elementi gia messi nella stessa casella:
    indcel=cells[cel]
    indcel2=list()

    # print('************possibilities: ',rand)

    for ind in indcel:
        if ind<index:
            indcel2.append(ind)
    if indcel2 !=[]:
        for ind in indcel2:
            if sudoku[ind] in rand:
                rand.remove(sudoku[ind])
    # print('************After cell check: ',rand)

    #comparazione del rand con gli elementi gia messi nella stessa riga:
    indlin=lines[row]
    indlin2=list()
    for ind in indlin:
        if ind<index:
            indlin2.append(ind)
    if indlin2 !=[]:
        for ind in indlin2:
            if sudoku[ind] in rand:
                rand.remove(sudoku[ind])
    # print('************After line check: ',rand)

    #comparazione del rand con gli elementi gia messi nella stessa colonna:
    indcol=columns[col]
    indcol2=list()
    for ind in indcol:
        if ind<index:
            indcol2.append(ind)
    if indcol2 !=[]:
        for ind in indcol2:
            if sudoku[ind] in rand:
                rand.remove(sudoku[ind])
    # print('************After column check: ',rand)

    # finalizzazione:
    # [2,5,8] sono le caselle in mezzo
    # per queste caselle faremo un controllo di piu
    # nel caso in cui abbiamo un contenuto nella prossima casella
    # che potremo ancora utilizzare (esiste in rand)
    # abbiamo la tendenza di utilizzarlo
    # per non affrontare problemi quando arriviamo nella prossima casella
    # r sarebbe il valore finale il quale appendiamo a sudoku
    r=0
    nexcellindex=list()
    nextcellindex2=list()
    nextcell=list()
    if cel in [2,5,8]:
        nextcellindex=cells[cel+1]
        for item in nextcellindex:
            if item<index:
                nextcellindex2.append(item)
        for item in nextcellindex2:
            nextcell.append(sudoku[item])
        for elem in rand:
            if elem in nextcell:
                r=elem
    # a questo punto se rand è vuota: vuol dire non abbiamo altre possibilita logicamente
    # dovremo iniziare da capo
    if rand==[]:
        sudoku=[]
        index=0
        row=1
        col=1
        continue
    else:
        if r==0:
            r=random.choice(rand)
        #print("*******chosen number is******** =",r)
        sudoku.append(r)
        index=index+1
        #print("********************************************************************")
    if index==81:
        #print(sudoku)
        break
# fin qua avremo per esempio sodoku= [7 , , , , , , , , , , , , , , , , ...]
print("********************************************************************")
print(sudoku[0:9])
print(sudoku[9:18])
print(sudoku[18:27])
print(sudoku[27:36])
print(sudoku[36:45])
print(sudoku[45:54])
print(sudoku[54:63])
print(sudoku[63:72])
print(sudoku[72:81])
print("********************************************************************")
fhand=open("sudoku.txt","w")
fhand.write("[ ")
for num in sudoku:
    fhand.write(str(num)+", ")
fhand.write("]")
