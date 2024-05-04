//Exercício 1
function calcularMedia(){
    let valor1 = Number(document.getElementById("valor1").value);
    let valor2 = Number(document.getElementById("valor2").value);
    
    media = (valor1 + valor2)/2;

    let resultado_ex1 = document.getElementById("resultado_ex1");
    resultado_ex1.innerHTML = `Resultado: ${media}`;
}

//Exercício 2
function calcularExponencial(){
    let valor_x = window.prompt("Digite o valor para X: ");
    let valor_y = window.prompt("Digite o valor para Y: ");
    resultado_ex2 = Math.pow(valor_x,valor_y);
    console.log(`O resultado para ${valor_x} elevado a ${valor_y} é igual a ${resultado_ex2}`);
}

//Exercício 3
function menorValor(){
    arrayValores = [];
    for(i=0;i<3;i++){
        valor = window.prompt(`Digite o valor ${i+1}:`);
        arrayValores.push(valor);
    }
    alert(`O menor valor da array é: ${Math.min(arrayValores[0], arrayValores[1], arrayValores[2])}`);
}

//Exercício 4

function multiplicarElementos(){
    x = [15,25];
    y = [12,15,23,43];

    for(i=0;i<x.length;i++){
        console.log(`O valor ${x[i]} multiplicado por 5: ${x[i]*5}`);
    }
}


//Exercício 5

function calcularPonderada(){
    let n1 = document.getElementById("nota1").value;
    let n2 = document.getElementById("nota2").value;

    ponderada = (n1*0,3)+(n2*0,7)

    let resultado_ex5 = document.getElementById("resultado_ex5");
    resultado_ex5.innerHTML = `Resultado: ${ponderada}`;   
}

//Exercício 6

function empresa(){
    salario = document.getElementById("salario").value;
    horas = document.getElementById("horas").value;
    refeicao = document.getElementById("refeicao").value;
    bruto = 0;
    liquido = 0;
    total_refeicao = 0;
    for(i=1;i<horas;i++){
        bruto = bruto + salario;
        if(i>40){
            bruto = bruto + 3*salario;
        }
    }
    liquido = bruto;
    for(i=0;i<refeicao;i++){
        liquido = liquido - 1.50;
        total_refeicao = total_refeicao + 1.50;
    }
    document.getElementById("sal_bruto").innerHTML = "Salário bruto: "+bruto;
    document.getElementById("refeicao_valor").innerHTML = "Valor das refeições: "+total_refeicao;
    document.getElementById("sal_liquido").innerHTML = "Salário líquido: "+ liquido;
}

