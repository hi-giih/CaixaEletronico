# 🏧 Caixa Eletrônico
![Static Badge](https://img.shields.io/badge/status-Active-gren?style=for-the-badge)


## 📋 Descrição
Este é um sistema simples de caixa eletrônico desenvolvido em Python. O projeto permite criar contas bancárias, realizar depósitos, saques e consultas de saldo. O sistema também permite visualizar as contas existentes e as informações de cada uma delas. 
O projeto segue princípios de **Paradigmas de Programação Orientada a Objetos (POO)**, utilizando atributos privados e encapsulamento para garantir maior controle e segurança dos dados das contas.

## ☘️ Funcionalidades

- **Criar uma nova conta**: O usuário pode criar uma nova conta fornecendo seu nome. O número da conta é gerado automaticamente.
- **Depositar valor na conta**: O usuário pode realizar depósitos em qualquer conta existente, inserindo o valor desejado.
- **Sacar valor da conta**: O sistema permite realizar saques, desde que o saldo seja suficiente para a transação.
- **Consultar saldo**: O usuário pode consultar o saldo de uma conta específica, fornecendo o número da conta.
- **Consultar todas as contas**: O sistema pode listar todas as contas existentes, mostrando o número da conta e o nome do titular.
- **Trato de erros**: O sistema possui validações para garantir que as operações de depósito, saque e consulta sejam feitas corretamente.

## 💻 Tecnologias utilizadas

- **Python 3.11**: Linguagem utilizada para o desenvolvimento do sistema.
- **Paradigmas de Programação Orientada a Objetos (POO)**: Utilização de classes e objetos, com atributos privados e métodos de acesso, encapsulando dados sensíveis.

## 🛠️ Instalando e Rodando

1. Clone este repositório: `git@github.com:hi-giih/CaixaEletronico.git`

2. Acesse o diretório do projeto: `cd desafio3 - POO - Caixa Eletronico`

3. Execute o script principal:: `python CaixaEletronico.py`


##  📌 Futuras Melhorias

 - Verificação de números de conta duplicados: Atualmente, as contas são criadas com números aleatórios, o que pode gerar duplicações. A melhoria seria implementar uma verificação para garantir que os números de contas sejam únicos.
 - Validação de entrada de dados: Adicionar validações para garantir que o usuário insira os valores corretamente, evitando erros de formato (ex: texto quando deveria ser número).
 - Interface Gráfica: Para tornar o sistema mais amigável, uma interface gráfica poderia ser desenvolvida utilizando bibliotecas como Tkinter ou PyQt.
 - Armazenamento Persistente: Implementar um banco de dados para armazenar os dados das contas, permitindo que as informações sejam mantidas entre sessões do programa.
 - Segurança: Adicionar autenticação para garantir que apenas usuários autorizados possam acessar e realizar operações nas contas.

## 📜 Licença 

Este projeto não está sob nenhuma licença.
