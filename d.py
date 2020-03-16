import impor
#To show results based on partial search
def search(t):
    b=[]
    t=t.upper()
    if len(t)!=0:
        for i,j in impor.d.items():
            for k in j:
                if i.startswith(t):
                    r=(k,j[k])
                    b.append(r)
        print("The words that start with ",t,"are;",b)
#to find the meaning of a word 
def fun(w):
    c=[]
    w=w.upper()
    count=0
    for i,j in impor.d.items():
        for k in j:
            if k == w:
                print(k,"is",j[k])
                count=1
                break
    if count==1:
        n=input("Would you like to search another word? ")
        n=n.upper()
        if n=='YES':
            h=input("Enter a word ")
            fun(h)
        else:
            print("Thank you for using our dictionary. ")
    else:
        print("word doesn't exist....")
        v=input("Would you like to add it to our dictionary?(1)Would you like to generate the partial search result?(2) ")
        if int(v)==1:
            fun3()
        elif int(v)==2:
            t=w[0:2]
            search(t)
        s=input("Would you like to look up another word? ")
        s=s.upper()
        if s=='YES':
            h=input("Enter a word ")
            fun(h)
        else:
            print("Thank you for using our dictionary. ")
#TO FIND THE WORDS HAVING THE SAME MEANING
v=[]
f=[]
def fun2():
    c=[]
    for i, j in impor.d.items():
        for k in j:
            c.append(j[k])
    c.sort()
    l=[]
    for i in range(len(c)-1):
        if c[i]==c[i+1]:
            l.append(c[i])
    for s in l:
        for i, j in impor.d.items():
            for k in j:
                if j[k]== s:
                    v.append(k)
    t=len(v)
    for i in range(0,t,2):
        r=(v[i],v[i+1])
        f.append(r)
    print('The words containing the same meaning are ',f)
#FOR the USER TO INPUT NEW WORDS
def fun3():
    word=input("Enter a word you like to add ")
    word=word.upper()
    for i,j in impor.d.items():
        for k in j:
            if word==k:
                print("Word already exists. Please try with another word ")
            break
    t=word[0:2]
    mean=input("Enter the meaning of the word ")
    for i,j in d.items():
        if i==t:
            for k in list(j):
                j[word]=mean
    print(impor.d)
#MAIN PART
print("Welcome to Finddit dictionary.\n")
m=input("Enter\n 1 if you want to check a meaning of a word.\n 2 if you want to generate results based on partial search'\n 3 if you want to find the words having the same meaning.\n 4 if you want to contribute to our Dictionary\n\t")
if int(m)==1:
    w=input("Enter a word to get its meaning ")
    fun(w)
elif int(m)==2:
    w=input("Enter the first two letters to generate the partial search ")
    search(w)
elif int(m)==3:
    fun2()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
elif int(m)==4:
    fun3()
else:
    print("Invalid input. Please enter a valid input ")
