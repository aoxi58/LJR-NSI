import csv

fichier1 = open ('tableMembre.csv', mode = 'r', encoding='UTF-8')
lecteur1 = csv.DictReader(fichier1, delimiter = ',')
    
fichier2 = open ('tablePret.csv', mode = 'r', encoding='UTF-8') 
lecteur2 = csv.DictReader(fichier2, delimiter = ',')
    
fichier3 = open ('tableLivre.csv', mode = 'r', encoding='UTF-8') 
lecteur3 = csv.DictReader(fichier3, delimiter = ',')

Liste1=[]
Liste2=[]
Liste3=[]

for ligne in lecteur1:
        Liste1.append(dict(ligne))
for ligne in lecteur2:
        Liste2.append(dict(ligne))
for ligne in lecteur3:
        Liste3.append(dict(ligne))



def fusion(table_1,table_2,cle) :
    table_fusion=[]
    for ligne_1 in table_1:
        for ligne_2 in table_2:
            if ligne_1[cle] == ligne_2[cle] :
                new_ligne = ligne_1
                for key in ligne_2:
                    if key !=cle:
                        new_ligne[key] = ligne_2[key]
                table_fusion.append(new_ligne)
    print(table_fusion)
    return table_fusion
table_fusion = fusion(Liste1, Liste2, "idm")

table_fusion =fusion(table_fusion, Liste3, "idl")
with open ('finalTD.csv', 'w', encoding='UTF-8') as f:
    f_csv = csv.writer(f, delimiter = ',')
    f_csv.writerows(table_fusion)










