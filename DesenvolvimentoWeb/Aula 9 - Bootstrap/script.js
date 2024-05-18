let lampada = document.getElementById("lampada");

function ligar(){
    if(lampada.getAttribute("src") == "img/luzDesligada.gif" && lampada.hidden == false){
        //console.log("Ligou");
        lampada.setAttribute("src","img/luzLigada.gif")
    }
}

function desligar(){
    if(lampada.getAttribute("src") == "img/luzLigada.gif" && lampada.hidden == false){
        //console.log("Desligou");
        lampada.setAttribute("src","img/luzDesligada.gif")
    }
}

function sumir(){
    //sole.log("Sumiu");
    lampada.hidden = true
}

function aparecer(){
    //console.log("Apareceu");
    lampada.hidden = false
}

function piscar(){
    if(lampada.getAttribute("src") == "img/luzLigada.gif" && lampada.hidden == false){
        desligar()
        //console.log("Piscou");
    }
    else if(lampada.getAttribute("src") == "img/luzDesligada.gif" && lampada.hidden == false){
        ligar();
        //console.log("Piscou");
    }
}

function magica(){
    // setInterval(() => {
    //     piscar();
    // }, 500);
    setInterval(piscar,500);
}