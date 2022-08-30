fh =open("new.text.txt",mode= "r")
word=input("Enter the word to search:")
s=""
count =1

while(fh):
    
    s=fh.readline()
    #print(s)
    L=s.split()
    if word in L:
        print("Line Number:",count,":",s)

    count+=1