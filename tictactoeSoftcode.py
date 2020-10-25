n=int(input("Type of cross(eg:3 4 5...): "))
cond=True
while cond:
    if n<3:
       print("Cross starts from 3 ONLY!!!")
       n=int(input("Type of cross(eg:3 4 5...): "))
    else:
        cond=False
matrix=['0' for x in range(n**2)]
def check(player): #Function for checking whether the player has won
    l=0
    m=n-1
    k=0
    p=n*(n-1)
    comp=0
    while l<(n**2)-n+2:
        t=s=r=q=0
        for i in range(l,m): #horizontal check
           if matrix[i]==matrix[i+1] and matrix[i]!='0':
             t+=1
           else:
               break
        for i in range(k,p,n): #vertical check
           if matrix[i]==matrix[i+n] and matrix[i]!='0':
             s+=1
           else:
               break
        for i in range(0,(n**2)-(n+1),n+1): #left diagonal check
            if matrix[i]==matrix[i+(n+1)] and matrix[i]!='0':
               if i==(n**2)-(n+2):
                   r=2
            else:
                break
        for i in range(n-1,((n**2)-n)+1,n-1): #right diagonal check
            if matrix[i]==matrix[i+(n-1)] and matrix[i]!='0':
               if i==(((n**2)-n)+1)-n:
                   q=2
            else:
                break
        if t==n-1 or s==n-1 or r==2 or q==2:
            comp=1
            break
        p+=1
        k+=1
        l+=n
        m+=n
    print(t,s,r,q)
    if comp==1:
       print("PLAYER ***",player,"*** WON ! ! ! !")
       return 1
def display(): #Function to display the moves
    l=0
    m=n  
    for i in range(n):
        for i in matrix[l:m]:
            print(i,end='|')
        print()
        l+=n
        m+=n
num=list(range(0,n**2))
def inputCheck(vari): #Function to check whether the input is valid
    s=1
    for i in num:
        if i==vari:
            s=0
    if s==0:
        return 0
    else:
        return 1
def tie(num): #Function to check tie
    leng=len(num)
    if leng==0:
        print("***MATCH TIED!!!***")
        return 1
#printing pos
li=[int(x) for x in range(0,n**2)]
for i in li:
    if i%n==0:
        print()
    print(i+1,end='|')
print()
#----
while True:  
    x=int(input('Player1:'))
    x=x-1
    inputCheck1=inputCheck(x)
    crct=True
    while crct:
        if x>n**2:
            state="WARNING...The positions are from 1 to ",n**2," ONLY..."
        else:
            state="Space already used"
        if inputCheck1==1:
            print(state)
            x=int(input('player1:'))
            x=x-1
            inputCheck1=inputCheck(x)
        elif inputCheck1==0:
            crct=False
    num.remove(x)
    tie1=tie(num)
    if(tie1==1):
        break
    matrix[x]='1'
    res=check('1')
    display()
    if res==1:
        break   
    y=int(input('player2:'))
    y=y-1
    inputCheck1=inputCheck(y)
    crct=True
    while crct:
        if y>n**2:
            state="WARNING...The positions are from 1 to ",n**2," ONLY..."
        else:
            state="Space already used"
        if inputCheck1==1:
           print(state)
           y=int(input('player2:'))
           y=y-1
           inputCheck1=inputCheck(y)
        elif inputCheck1==0:
            crct=False
    num.remove(y)
    tie1=tie(num)
    if(tie1==1):
        break
    matrix[y]='2'
    res=check('2')
    display()
    if res==1:
        break
