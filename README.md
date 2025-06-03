# EDS - Educação Digital Segura

Projeto de uma aplicação desktop em Python para cadastro e login de usuários, com gerenciamento de sessões e navegação entre componentes de ações educacionais.

---

## Visão Geral

Este projeto consiste em uma plataforma educativa chamada **EDS - Educação Digital Segura**, onde o usuário pode:

- **Cadastrar-se** (criar conta)
- **Acessar** (login)
- Após login, acessar a tela principal (`main.py`) com diversos componentes de ações educacionais.

Os dados dos usuários são armazenados localmente em JSON, e uma sessão é mantida em um arquivo `session.txt` enquanto o usuário está logado.

---

## Estrutura do Projeto

- `index.py`  
  Arquivo inicial da aplicação. Apresenta a tela inicial com opções para acessar (login) ou cadastrar usuário.

- `cadastrar.py`  
  Tela para cadastro de novos usuários. Salva os dados no arquivo `dados/usuarios.json`.  
  As senhas são armazenadas com hash para maior segurança.

- `acessar.py`  
  Tela de login que verifica o e-mail e senha, cria o arquivo de sessão `session.txt` e redireciona para `main.py`.

- `main.py`  
  Tela principal do sistema após login, onde outras ações e componentes podem ser acessados.

- `dados/usuarios.json`  
  Arquivo JSON onde os dados dos usuários são salvos.

- `session.txt`  
  Arquivo criado durante o login para manter a sessão do usuário ativa.

---

## Requisitos

Bibliotecas Python utilizadas e listadas no arquivo `requirements.txt`:

- Pillow  
- Werkzeug  
- reportlab

---

## Como Executar

1. Clone o repositório ou baixe os arquivos do projeto.

2. Instale as dependências via pip:

   ```bash
   pip install -r requirements.txt
