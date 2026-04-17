CREATE DATABASE IF NOT EXISTS devbg;
USE devbg;

CREATE TABLE IF NOT EXISTS produtos (
codigo INT NOT NULL PRIMARY KEY auto_increment,
produto VARCHAR (200),
descr VARCHAR (500),
preco FLOAT,
foto VARCHAR (500)
);

CREATE TABLE IF NOT EXISTS devbg.usuarios (
usuario VARCHAR(100),
senha VARCHAR(200),
nome VARCHAR (100)
);

