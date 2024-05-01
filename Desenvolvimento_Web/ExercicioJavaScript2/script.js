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
    x = window.prompt("Digite o valor para X: ");
    y = window.prompt("Digite o valor para Y: ");
    resultado_ex2 = Math.pow(x,y);
    console.log(`O resultado para ${x} elevado a ${y} é igual a ${resultado_ex2}`);
}

//Exercício 3
function menorValor(){
    resultado_ex3 = Math.min(1,2,3);
    alert(`O menor valor é: ${resultado_ex3}`);
}

//Exercício 4

function array(){
    x = [15,25]
    y = [12,15,23,43]

    for(i=0;i<2;i++){
        console.log(x[i]*5)
    }
}




