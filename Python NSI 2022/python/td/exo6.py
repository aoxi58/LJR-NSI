from random import*
L1=[randint(1,100) for i in range(6)]
#print(L1)
L2=[i*3 for i in range(-6,24)]
#print(L2)
L3=[2*(i**3) for i in range(-3,15) if i%2==1]
#print(L3)


    
L4=list()  

print(L4.append(input("val 1 : ")))
print(L4.append(input("val 2 : ")))
print(L4.append(input("val 3 : ")))
print(L4.append(input("val 4 : ")))
print(L4.append(input("val 5 : ")))
print(L4)

i=input("i")
j=input("i")

def echange(L,i,j):
    L[i]=L[j]
    
    
print(echange(L4,i,j))
    