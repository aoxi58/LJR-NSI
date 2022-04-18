function demarage(){
	alert("BONJOUR !"); 

}
function FoncRouge(){
	document.querySelector("#monPara").classList.remove("vert");
	document.querySelector("#monPara").classList.add("rouge");
}

function FoncVert(){
	document.querySelector("#monPara").classList.remove("rouge");
	document.querySelector("#monPara").classList.add("vert");
}

