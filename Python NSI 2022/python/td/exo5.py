liste=list()

for i in range(10):
    a=int(input("val +1 : "))
    liste.insert(i, a)
    
print(liste)

def moyenne(b):
    a=0
    for i in range(len(b)):
        a=a+b[i]
    return a/len(b)
    
print(moyenne(liste))



