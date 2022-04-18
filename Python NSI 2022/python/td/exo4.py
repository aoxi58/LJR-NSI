liste=list()


for i in range(5):
    a=int(input("val +1 : "))
    liste.insert(i, a)
    
liste.append(48)
print(liste)

del(liste[3])
print(liste)

liste.remove(48)
print(liste)

liste.insert(1, 888)
print(liste)