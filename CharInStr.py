
string=input("please enter your text here: ")
character= input("please enter the character you want to search for: ")
def find(str,char):
    n=0
    for i in range(len(str)):
        if str[i]==char: n=n+1
    print("there are ",n,"same characters")
find(string,character)
