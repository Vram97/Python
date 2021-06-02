import random
n=input()
view=[]

for i in range(3):
    view.append(list(input())
print(view)
walls=[view[0][1],view[1][0],view[1][2],view[2][1]]
moves=["UP","LEFT","RIGHT","DOWN"]
a=0
for i in range(len(walls)):
    if(walls[i]=="e"):
        print(moves[i])
        a=1
        break
if(a==0):
    k=[]
    for i in range(len(walls)):
        for j in range(100):
            x=random.randint(0,3)
            if(x not in k):
                k.append(x)
                break
        if(walls[x]=="-"):
            print(moves[x])
        elif(walls[x]="b" and (for z in walls:z!="-") and len(k)==4):
            print(moves[x])
            
