from random import*

L1=[randint(1,100) for i in range(20)]
pair=[]
impair=[]

for i in range(20):
    if L1[i]%2==1:
        pair.append(L1[i])
    elif L1[i]%2==0:
        impair.append(L1[i])
        
print(impair)
print(pair)