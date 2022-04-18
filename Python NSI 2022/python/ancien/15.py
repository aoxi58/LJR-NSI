
L1 = ['A' , 'B', 'C', 'D']

L2 = [10, 11, 12]




L1.append('D')
print(L1)

L1.append(13)
print(L1)

L1.insert(1, 'E')
print(L1)

L1.insert(len(L1), 'F')
print(L1)

L1[1]='G'
print(L1)

L1.extend(L2)
print(L1)

print(L1)
print(len(L1))

del(L1[0])
print(L1)

x = L1.pop(0)
print(L1)
print(x)

y = L1.index(10)
print(y)

compteur= L1.count('D')
print(compteur)

L1.remove('D')
print(L1)



















