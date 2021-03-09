def factoriel(x):
    result=1
    while x>1:
        result=result*x
        x=x-1
    return result

def pascals_triangle(n):
    diz=dict()
    lista=list()
    rows=range(n) #[0,1,2,3] 4rows
    posinrow=[]

    for row in rows:
        posinrow.append(row)
        print(posinrow)
        for k in posinrow: #k= 1
            o =int(factoriel(row)/(factoriel(k)*factoriel(row-k)))
            #print (o)
            lista.append(o)
        diz[row]= lista
        lista=[]

    return diz

rownumbers= int(input("Please enter number of Rows: "))
dixx=pascals_triangle(rownumbers)
print(dixx)