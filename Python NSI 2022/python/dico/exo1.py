listFR=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
listEN=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]


def intdico(listFR,listEN):
    dico={}
    for i in range(len(listFR)):
        dico[listFR[i]]=listEN[i]
    return dico
        
        
print(intdico(listFR,listEN))
    