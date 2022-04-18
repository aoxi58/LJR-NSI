// Script formulaire

function Calcul_impot(form) {
    var revenu =parseFloat(form.revenu.value);
    var enf=parseFloat (form.enf.value);
        
    if (!form.Oui.checked && !form.Non.checked)
    {alert("Vous devez cochez une case");
        return false};
    if (form.Oui.checked && form.Non.checked)
    {alert("Vous ne devez cochez qu'une case");
        return false};

    if (form.Oui.checked && enf==0)
    {revenu=revenu/2}
	
	else if (form.Oui.checked && enf==1)
	{revenu=revenu/2.5}
    else if (form.Oui.checked && enf==2)
    {revenu=revenu/3}
    else if (form.Oui.checked && enf==3)
    {revenu=revenu/4}
    else if (form.Non.checked && enf==1)
    {revenu=revenu/1.5}
    else if (form.Non.checked && enf==2)
    {revenu=revenu/2}
    else if (form.Non.checked && enf==3)
    {revenu=revenu/3};

    if (revenu<10064)
    {taux=0}
    else if (revenu>= 10064 && revenu<27794)
    {taux=14}
    else if (revenu>= 27794 && revenu<74517)
    {taux=30}
    else if (revenu>= 74517 && revenu<157806)
    {taux=41}
    else if (revenu>= 157806){taux=45};
	
    document.getElementById("reponse").innerHTML = "Votre taux marginal est :  " +taux +" %";
    }



