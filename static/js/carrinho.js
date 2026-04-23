async 
function MostrarCarrinho() {
    const resposta = await fetch("http://10.110.134.2:8080/api/get/carrinho")

    if (!resposta.ok) {
        alert("ERRO AO EXECUTAR")

    } else {
        const dados = await resposta.json()

        const carrinho = document.getElementById("carrinho")

        carrinho.innerHTML = "";


        for (let dado of dados) {

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
        }
        document.querySelector(".cart-item__price").textContent = "R$" + total
    }
}

MostrarCarrinho()