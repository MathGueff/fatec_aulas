let adicionais=0;
let entrega = 0;

function totalPagar(){
    let total = 0
   
    calcularAdicionais();
    total = adicionais + entrega
    //alert("O total a pagar é "+ total)
    resultado = document.getElementById("total").value
    if(total != 0){
        resultado = total
        document.getElementById("total").value = resultado+" reais"
    }else{
        resultado = "Nenhum valor foi adicionado!"
        document.getElementById("total").value = resultado
    }
    
}

function calcularAdicionais(){
    let selecionados = document.querySelectorAll("input[name='adicionais']");
    adicionais = 0
    let qtd = selecionados.length;

    for(i=0;i<qtd;i++){
        if(selecionados[i].checked){
            console.log(selecionados[i].value)
            adicionais += parseInt(selecionados[i].value)
        }
    }
    if(adicionais == 0){
        //alert("Nenhum adicional foi adicionado")
    }else{
         //alert(adicionais)
    }
}

function calcularEntrega(){
    
}