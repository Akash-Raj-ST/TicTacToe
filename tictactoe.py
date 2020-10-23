matrix=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
def check(player): #Function for checking whether the player has won
    l=0
    m=2
    k=0
    p=6
    cond=True
    while l<=7 and cond:
        t=s=r=q=0
        for i in range(l,m): #horizontal check
           if matrix[i]==matrix[i+1] and matrix[i]!=' ':
             t+=1
           else:
               break
        for i in range(k,p,3): #vertical check
           if matrix[i]==matrix[i+3] and matrix[i]!=' ':
             s+=1
           else:
               break
        for i in range(0,5,4): #left diagonal check
            if matrix[i]==matrix[i+4] and matrix[i]!=' ':
               if i==4:
                   r=2
            else:
                break
        for i in range(2,5,2): #right diagonal check
            if matrix[i]==matrix[i+2] and matrix[i]!=' ':
               if i==4:
                   q=2
            else:
                break
        if t==2 or s==2 or r==2 or q==2:
            break
        p+=1
        k+=1
        l+=3
        m+=3
    if t==2 or s==2 or r==2 or q==2:
       print(t,s,r,2)
       print("PLAYER ***",player,"*** WON ! ! ! !")
       return 1
def display(): #Function to display the moves
    l=0
    m=3   
    for i in range(3):
        for i in matrix[l:m]:
            print(i,end='|')
        print()
        l+=3
        m+=3
num=[0,1,2,3,4,5,6,7,8]
def inputCheck(vari): #Function to check whether the input is valid
    s=1
    for i in num:
        if i==vari:
            s=0
    if s==0:
        return 0
    else:
        return 1
def tie(num): #Function to check draw
    leng=len(num)
    if leng==0:
        print("***MATCH TIED!!!***")
        return 1
print("1|2|3|")
print("4|5|6|")
print("7|8|9|")
while True:  
    x=int(input('PlayerX:'))
    x=x-1
    inputCheck1=inputCheck(x)
    crct=True
    while crct:
        if x>8:
            state="WARNING...The positions are from 1 to 9 ONLY..."
        else:
            state="Space already used"
        if inputCheck1==1:
            print(state)
            x=int(input('playerX:'))
            x=x-1
            inputCheck1=inputCheck(x)
        elif inputCheck1==0:
            crct=False
    num.remove(x)
    tie1=tie(num)
    if(tie1==1):
        break
    matrix[x]='x'
    res=check('x')
    display()
    if res==1:
        break   
    y=int(input('playerY:'))
    y=y-1
    inputCheck1=inputCheck(y)
    crct=True
    while crct:
        if y>8:
            state="WARNING...The positions are from 1 to 9 ONLY..."
        else:
            state="Space already used"
        if inputCheck1==1:
           print(state)
           y=int(input('playerY:'))
           y=y-1
           inputCheck1=inputCheck(y)
        elif inputCheck1==0:
            crct=False
    num.remove(y)
    tie1=tie(num)
    if(tie1==1):
        break
    matrix[y]='y'
    res=check('y')
    display()
    if res==1:
        break
