from random import*

L1=[randint(1,100) for i in range(20)]
print(L1)
maxi=L1[0]
for i in range(20):
    if maxi<L1[i]:
        maxi=L1[i]
print(maxi)
mini=L1[0]
for i in range(20):
    if mini>L1[i]:
        mini=L1[i]
print(mini)