name=input("Please enter your name: ")
namelen=len(name)

l=int((namelen+6)/2)

line=""
for i in range(l-1):
    line=line+" -"
if namelen%2==1: line=line+" "
l1= "+" + line + "+"

l2="|  "+name+"  |"

print(l1)
print(l2)
print(l1)
