CREATE DATABASE IF NOT EXISTS devbg;
USE devbg;

CREATE TABLE IF NOT EXISTS produtos (
    codigo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    produto VARCHAR(200),
    descr VARCHAR(500),
    preco DECIMAL(10,2),
    foto VARCHAR(500)
);

CREATE TABLE IF NOT EXISTS usuarios (
    usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    senha VARCHAR(200),
    nome VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS carrinhos (
    cod_car INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(100),
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP, 
    finalizado TINYINT(1),
    CONSTRAINT fk_carrinho_usuario FOREIGN KEY (usuario) REFERENCES usuarios (usuario)
);

CREATE TABLE IF NOT EXISTS itens_carrinhos (
    cod_item_car INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cod_car INT,
    cod_produto INT,
    quantidade INT DEFAULT 1,
    CONSTRAINT fk_itenscarrinhos_carrinhos FOREIGN KEY (cod_car) REFERENCES carrinhos(cod_car),
    CONSTRAINT fk_itenscarrinhos_produtos FOREIGN KEY (cod_produto) REFERENCES produtos(codigo)
);

SELECT carrinhos.cod_carrinho, usuarios.usuario, carrinhos.data_criacao, carrinhos.finalizado, produto, quantidade, produtos.preco, produtos.foto FROM carrinhos
INNER JOIN itens_carrinhos ON carrinhos.cod_car = itens_carrinhos.cod_car
INNER JOIN produtos ON produtos.codigo = itens_carrinhos-carrinhos.cod_produto WHERE usuarios.usuario = "Gabriela";








