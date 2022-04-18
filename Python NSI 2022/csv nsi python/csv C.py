#exemple C

table_1= [{'nom':'Baron', 'prénom':'Paul', 'NSI':'18', 'Physique':'16','Maths': '15'},
        {'nom':'Tallant', 'prénom':'Greg','NSI': '10', 'Physique':'13','Maths': '9'},
        {'nom':'Goury', 'prénom':'Zoé', 'NSI':'13','Physique':'14', 'Maths':'11'}]

table_2 = [{'nom':'Baron','Age': '16','Anglais':'12' },
        {'nom':'Tallant','Age': '17','Anglais':'13' },
        {'nom':'Goury', 'Age': '15','Anglais':'11'}]

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
fusion(table_1, table_2, "nom")