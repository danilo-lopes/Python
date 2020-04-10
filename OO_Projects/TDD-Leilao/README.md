# Test unitário com Python

## Projeto

```
├── README.md
├── src
│   ├── app_leilao
│   │   ├── excessao_leilao.py
│   │   ├── __init__.py
│   │   ├── lance.py
│   │   ├── leilao.py
│   │   └── usuario.py
└── tests
    ├── __init__.py
    ├── leilao_test.py
    └── usuario_test.py
```

# Imitando uma aplicação de leilão

## Classes

#### Usuario

* Deve conter nome, `str`
* Deve conter um valor em carteira, `int` ou `float`

Ex: `joao = Usuario('joao', 500)`

#### Lance

* Deve conter um `Usuario`
* Deve conter o valor de lance do usuário, `int` ou `float`

Ex: `lance_joao = Lance(joao, 100)`

#### Leilao

* Deve ser inicializada com uma descrição, `str`

#### Excessao

* Classe que utiliza a classe `Exception` built-in do Python para gerenciarmos as excessões da nossa aplicação

## Regra De Negócio

> Um usuário deve ser capaz de dar um lance com algum valor

> Um usuário deve ser capaz de visualizar o valor dos seus lances

> Um usuário não pode entrar no leilão com a carteira vazia

> Um usuário não pode dar um valor de um lance maior do que o valor que possui em sua carteira

> Um usuário não pode dar dois lances seguidos

> O valor de um lance não pode ser inferior a um valor de lance anterior

## Exemplos de utilização

`=>` danilo = Usuario('Danilo', 500)

`=>` joao = Usuario('Joao', 500)

`=>` leilaoCelular = Leilao('Xiaomi Mi 10 PRO')

`=>` danilo.propoe_lance(leilaoCelular, 100)

`=>` joao.propoe_lance(leilaoCelular, 110)

`=>` danilo.meusLances(leilaoCelular)

`100`

`=>` joao.meusLances(leilaoCelular)

`110`

`=>` leilaoCelular.menor_lance

`100`

`=>` leilaoCelular.maior_lance

`110`

---
`=>` danilo.propoe_lance(leilaoCelular, 100)

`src.app_leilao.excessao_leilao.LanceInvalido: O valor do lance tem que ser maior do que o anterior`

`=>` joao.propoe_lance(leilaoCelular, 120)

`src.app_leilao.excessao_leilao.LanceInvalido: O mesmo usuario não é permitido`

---

`=>` pedro = Usuario('Pedro', 0)

`src.app_leilao.excessao_leilao.CarteiraInvalida: O usuario não pode iniciar com a sua carteira vazia`