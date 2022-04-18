import csv
liste = [['nom', 'prénom', 'NSI', 'Physique', 'Maths'],
            ['Baron', 'Paul', 18, 16, 15],
            ['Tallant', 'Greg', 10, 13, 9],
            ['Goury', 'Zoé', 13, 14, 11]]

with open ('exemple_5.csv', 'w', encoding='UTF-8') as f:
    f_csv = csv.writer(f, delimiter = ';')
    f_csv.writerows(liste)