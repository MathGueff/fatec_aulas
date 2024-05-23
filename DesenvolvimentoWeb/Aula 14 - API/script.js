let cep = document.querySelector("input[name='cep']");
let api = "https://viacep.com.br/ws/01001000/json/";
let button = document.getElementById("buscar_cep");
let imagem = document.getElementById("imagem_api");
button.addEventListener('click', async function buscarCep(){
    api = `https://viacep.com.br/ws/${cep.value}/json/`;
    let dados = await fetch(api);
    let dadosFormat = await dados.json();
    alert(`${dadosFormat.bairro}, ${dadosFormat.localidade}, ${dadosFormat.uf}`);
    link = `https://source.unsplash.com/1600x900/?${dadosFormat.localidade}`
    imagem.setAttribute("src", link)
});