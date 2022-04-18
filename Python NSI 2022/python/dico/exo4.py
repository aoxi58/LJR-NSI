listFR=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
listEN=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
listDE=["montag","dienstag","mittwoch","donnerstag","freitag","samstag","sonntag"]

def intdico(listFR,listEN,listDE):
    dico={}
    for i in range(len(listFR)):
        dico[listFR[i]]=[listEN[i]]+[listDE[i]]
    return dico
        
        
def traduc_fr_en(dico):
    b=int(input("en=0 ou de=1 : "))
    a=input("mot fr : ")
    cond="false"
    while cond!="true":
        if a in dico:
            cond="true"
            return dico[a][b]
        else :
            a=input("erreur, reesayez, mot fr en miniscule : ")


print(traduc_fr_en(intdico(listFR,listEN,listDE)))