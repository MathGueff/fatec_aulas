div = document.getElementById("mudar_medidas");
mostra_height = document.getElementById("mostra_height");
mostra_width = document.getElementById("mostra_width");

function mudarUnidade(unidade, cor){
    div.style.width = "25"+unidade;
    div.style.height = "25"+unidade;
    if(unidade == "rem"){
        div.style.background = "#5eff00";
        div.innerHTML = "REM"
        div.style.padding = "0px 12px"
    }
    else if(unidade == "em"){
        div.style.background = "#8d8dd1"
        div.innerHTML = "EM"
        div.style.padding = "0px 12px"
    }
    else if(unidade == "px"){
        div.style.background = "#00ffff"
        div.style.padding = "0px"
        div.innerHTML = "PX"
    }
    else if(unidade == "%"){
        div.style.background = "#ffff00"
        div.innerHTML = "%"
        div.style.padding = "0px 12px"
    }
    else if(unidade == "vw"){
        div.style.background = "#86c7c7"
        div.innerHTML = "VW"
        div.style.padding = "0px 12px"
    }
    else if(unidade == "vh"){
        div.style.background = "#ffc0cb"
        div.innerHTML = "VH"
        div.style.padding = "0px 12px"
    }
    mostra_height.innerHTML = "height="+div.style.height
    mostra_width.innerHTML = "width="+div.style.width
}