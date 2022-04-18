listFR=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
listEN=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]


def intdico(listFR,listEN):
    dico={}
    for i in range(len(listFR)):
        dico[listFR[i]]=listEN[i]
    return dico
        
        
def traduc_fr_en(dico):
    a=input("mot fr : ")
    cond="false"
    while cond!="true":
        if a in dico:
            cond="true"
            return dico[a]
        else :
            a=input("erreur, reesayez, mot fr en miniscule : ")


print(traduc_fr_en(intdico(listFR,listEN)))