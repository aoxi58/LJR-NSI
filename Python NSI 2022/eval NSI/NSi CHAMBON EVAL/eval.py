import csv

# ouverture du fichier
tableau = []
fichier = open('titanic.csv', 'r', encoding = 'UTF-8', newline='')
lecteur= csv.DictReader(fichier,delimiter = ',')
# transformation en liste de dictionnaire
for ligne in lecteur:
    tableau.append(dict(ligne))
    
print(tableau, '\n')
# Question 3 , recherche du passager 53
print('il y a',len(tableau), 'passagés')
for i in tableau:
    if i['PassengerId'] == '53':
        print('passager n°53 :','\n', 'Nom : ', i['Name'] ,'\n',
              'âge : ', i['Age'] ,'\n',
              'sexe : ', i['Sex'])
        if i['Survived']== 1:
            print('rescapé : oui')
        else:
            print(' rescapé : non')
            
            
# Question 4, recherche des survivants           
surivants=0       
for j in tableau:
    if j['Survived'] == '1':
        surivants= surivants +1
print('Il y a',surivants,'survivants.')

# Question 5, recherche des survivants embarqués à Cherbourg

surivants_Cherbourg=0
for h in tableau:
    if h['Survived'] == '1' and h['Embarked']=='C' :
        surivants_Cherbourg= surivants_Cherbourg +1
print('Il y a',surivants_Cherbourg,'des survivants qui ont embarqués à Cherbourg.')






        
        

