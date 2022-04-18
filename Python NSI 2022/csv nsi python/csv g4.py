import csv

tableau= []
fichier = open('exemple_5.csv', 'r', encoding = 'UTF-8')
lecteur = csv.DictReader(fichier,delimiter = ';')

for ligne in lecteur:
    tableau.append(dict(ligne))

print(tableau, '\n')

resultat_1 = [ligne['prénom'] for ligne in tableau]
print(resultat_1, '\n')

resultat_2 = [ligne['NSI'] for ligne in tableau]
print(resultat_2, '\n')
resultat_3=[]
for ligne in tableau:
    if  int(ligne['NSI'])>12:
        resultat_3.append(ligne['prénom'])
print(resultat_3)
        
 
        
resultat_4=[]
for ligne in tableau:
    if  (int(ligne['NSI'])>15 and int(ligne['Maths'])>12):
        resultat_4.append(ligne['prénom'])
print(resultat_4)
        
        
resultat_5 = []
for ligne in tableau:
    if ligne['prénom']=='Zoé':
        print(ligne['NSI'],"/",ligne['Maths'],"/",ligne['Physique'])


  

def moyenne(liste,matière):
    x=0
    for ligne in liste:
        x= int(ligne[matière])+x
    y=x/len(liste)
    return y
print(moyenne(tableau,'NSI'))


moytab=[{'nom', 'prénom', 'NSI', 'Physique', 'Maths'},
            {'Baron', 'Paul', 18, 16, 15},
            {'Tallant', 'Greg', 10, 13, 9},
            {'Goury', 'Zoé', 13, 14, 11}
            {'CMOI';'Arthur';15;16;11}]







headers = tableau[0].keys()

with open('exemple_moyenne.csv', 'w', encoding = 'UTF-8')as f:
    lecteurmoyenne = csv.DictWriter(f, headers, delimiter = ';')
    lecteurmoyenne.writeheader()
    lecteurmoyenne.writerows(tabmoyenne(tableau))




def tabmoyenne():
    moyenne=[]
    
    return 
    
      
        
        





