let viacep = "https://viacep.com.br/ws/01001000/json/";

//Verificar Cidade
let cidade = document.getElementById("cidade");
let cep = document.getElementById("cep");
let rua = document.getElementById("rua");
let buscarCidade = document.getElementById("buscarCidade");
let limparDados = document.getElementById("btn-limpar");

//Verificar Clima
let verClima = document.getElementById("btn-clima");
let det_tmp = document.querySelector("p[class='detalhes_tmp']");

//Outros
let dadosPais = document.querySelector("p[class='dados_pais']");
let imagem_cidade = document.getElementById("img_cidade");
let imagem_bandeira = document.getElementById("img_bandeira")
let nomeCidade = document.getElementById("nome_cidade");

buscarCidade.addEventListener('click', async function buscarCidade(){
    if(cep.value == ""){
        alert("Digite um CEP válido!")
    }else{
        viacep = `https://viacep.com.br/ws/${cep.value}/json/`;
        let res_viacep = await fetch(viacep);
        res_viacep = await res_viacep.json();
    
        // unsplash = `https://source.unsplash.com/1600x100/?${res_viacep.localidade}`;
        // imagem_cidade.setAttribute("src", unsplash);
    
        cidade.value =  res_viacep.localidade;
        nomeCidade.innerHTML = res_viacep.localidade;
        rua.value = `${res_viacep.logradouro} - ${res_viacep.bairro} - ${res_viacep.localidade} - ${res_viacep.uf}`
    }
});

limparDados.addEventListener('click', function limparDados(){
    cidade.value = "";
    cep.value = "";
    rua.value = "";
    imagem_bandeira.setAttribute('src', "");
    // imagem_cidade.setAttribute('src', "");
    nomeCidade.innerHTML = "Cidade: ";
    det_tmp.innerHTML = "Temperatura: ";
});

verClima.addEventListener('click', async function verClima(){
    if(cidade.value == ""){
        alert("Digite ou encontre sua cidade primeiro!");
    } else{
        let cidade_pesquisa = document.getElementById("cidade").value;

        weather_api = `https://api.openweathermap.org/data/2.5/weather?q=${cidade_pesquisa}&appid=9d65d48347c294741542e384942c2704`
        temperatura = await fetch(weather_api);
        temperatura = await temperatura.json();
    
        flags = `https://flagsapi.com/${temperatura.sys.country}/flat/64.png`;
        imagem_bandeira.setAttribute('src',flags);
        det_tmp.innerHTML = `Temperatura: ${parseInt(temperatura.main.temp-273.15)}ºC, Umidade: ${temperatura.main.humidity}%, Vento: ${temperatura.wind.speed}km/h, Tempo: ${temperatura.weather[0].main}`
    }
});