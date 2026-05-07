async function mostrarCarrinho(){
    const resposta = await fetch("http://10.110.134.2:8080/api/get/carrinho")
    if (!resposta.ok){
        alert("ERRO AO EXECUTAR")
    }else{
        const dados = await resposta.json()
        const carrinho = document.getElementById("carrinho")
        carrinho.innerHTML = "";
        let total = 0;
        for (let dado of dados){
            total = total + dado.preco
            let linha = `
            <aside class="cart">
  <label for="toggle-cart" class="close-cart">✕</label>
  <h2>Seu Carrinho</h2>
  <div class="cart-items">${dado.nome}</div>
  <div class="cart-footer">
    <strong>Total: ${dado.preco}</strong>
    <button>Finalizar</button>
  </div>
</aside>
            `
            carrinho.innerHTML += linha
        }}}

mostrarCarrinho()

async function inserirItemCarrinho(cod_produto, quantidade = 1) {
    const resposta = await fetch(URL = "/api/post/item_carrinho", {method: "POST", headers:{"content-type" : "application/json"}, body: JSON.stringify({"cod_produto": cod_produto, "quantidade":quantidade})}
    )
    if (!resposta.ok){alert("Erro ao inserir item.")}
    mostrarCarrinho() 
}