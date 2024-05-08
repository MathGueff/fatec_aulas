let adicionais=0;
let entrega = 0;
let pedilanchedo = 0;

function totalPagar(){
    let total = 0
    verifCliente();
    nome_cli = document.getElementById("nome").value
    if(nome_cli == ""){
        nome_cli = "Informe o seu nome"
    }
    telefone_cli = document.getElementById("telefone").value
    if(telefone_cli == ""){
        telefone_cli = "Nenhum telefone foi informado"
    }
    calcularPedido();
    calcularAdicionais();
    calcularEntrega();

    mostra_total = document.getElementById("total");
    descricao = document.getElementById("descricao");

    total = adicionais + lanche + entrega;
    //alert("O total a pagar é "+ total)
    resultado = document.getElementById("total").value;
    if(total != 0){
        resultado = total;
        mostra_total.value = `O total a pagar é ${total} reais`
        descricao.innerHTML = `Nome do Cliente: ${nome_cli}\nTelefone de Contato: ${telefone_cli}\nLanche: ${lanche} reais \nAdicionais: ${adicionais} reais \nMétodo de Entrega ${entrega} reais`
    }else{
        resultado = "Nenhum valor foi adicionado!";
        mostra_total.value = resultado;
        descricao.innerHTML = ``
    }
}

function verifCliente(){
    nome_cli = document.getElementById("nome").value
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
}

function calcularEntrega(){
    let radioEntrega = document.querySelectorAll("input[name='escolha_entrega']");
    let qtd = radioEntrega.length;

    for(i=0;i<qtd;i++){
        if(radioEntrega[i].checked){
            entrega = Number(radioEntrega[i].value);
            break;
        }
    }
}

function calcularPedido(){
    lanche = Number(document.getElementById("combos").value);
}

function imprimir(){
    window.print();
}

function clock(){
    let Hora = new Date()
    let mensagem = Hora.getHours() + ":" + Hora.getMinutes() +":" + Hora.getSeconds();
    document.getElementById("relogio").innerHTML = mensagem;
} setInterval(clock,1000)