import csv
Liste = []
with open ('exemple_nsi.csv', mode = 'r', encoding='UTF-8') as fichier_csv:
    lecteur = csv.DictReader(fichier_csv, delimiter = ',')
    
    for ligne in lecteur:
        Liste.append(ligne)
    print(Liste)