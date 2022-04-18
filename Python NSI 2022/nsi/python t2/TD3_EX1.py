a=input("entrez un octet")
b=input("entrez un 2eme octet")

def add_bin(a,b):
    res=""
    ret="false"
    for i in range(7,-1,-1):
        if a[i]=="0" and b[i]=="1":
            if ret=="true":
                res="0"+res
            else :
                res="1"+res
        elif a[i]=="1" and b[i]=="1":
            res="0"+res
            ret="true"
        elif a[i]=="0" and b[i]=="0":
            if ret=="true":
                res="1"+res
                ret="false"
            else :
                res="0"+res
        elif a[i]=="1" and b[i]=="0":
            if ret=="true":
                res="0"+res
            else :
                res="1"+res            
            
    return res
    

print(add_bin(a,b))
