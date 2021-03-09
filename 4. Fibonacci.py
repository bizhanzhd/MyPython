def fibonacci(n):
    fhand=list()
    fhand.append(0)
    fhand.append(1)

    l=range(n)
    l=l[2:]

    for j in l:
        x=fhand[j-1]+fhand[j-2]
        fhand.append(x)
    print(fhand)

i=input("please insert the length of the serie: ")
i=int(i)
fibonacci(i)