import csv

with open ('tableMembre.csv', mode = 'r', encoding='UTF-8') as fichier_csv:
    lecteur1 = csv.DictReader(fichier_csv, delimiter = ',')
    
with open ('tablePret.csv', mode = 'r', encoding='UTF-8') as fichier_csv:
    lecteur2 = csv.DictReader(fichier_csv, delimiter = ',')
    
with open ('tableLivre.csv', mode = 'r', encoding='UTF-8') as fichier_csv:
    lecteur3 = csv.DictReader(fichier_csv, delimiter = ',')

for ligne in lecteur1:
        Liste1.append(ligne)
for ligne in lecteur2:
        Liste2.append(ligne)
for ligne in lecteur3:
        Liste3.append(ligne)



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
    return table_fusion1
fusion(table_1, table_2, "nom")

fusion(table_fusion1, liste3, "idl")










