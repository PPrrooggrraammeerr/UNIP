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
  Arquivo inicial da aplicação. Ao executá-lo, o usuário verá uma tela com as opções **Acessar** (login) e **Cadastrar** (novo usuário).

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

> **Atenção:** Este projeto foi desenvolvido para rodar **100% em ambiente Windows**, devido à estrutura de diretórios utilizada (uso de barras invertidas e caminhos absolutos).

1. Clone o repositório ou baixe os arquivos do projeto.

2. Instale as dependências listadas no `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute o arquivo principal para iniciar a aplicação:

   ```bash
   python index.py
   ```

4. Ao abrir o programa, você verá a tela inicial com as opções:

   - **Acessar**: abre a tela de login (`acessar.py`).
   - **Cadastrar**: abre a tela de cadastro de novos usuários (`cadastrar.py`).

5. Após fazer login com sucesso, será criado o arquivo `session.txt` e a aplicação abrirá a tela principal (`main.py`) com as funcionalidades educacionais.

---

## Fluxo da Aplicação

- O usuário inicia a aplicação executando `index.py`.
- Na tela inicial, escolhe entre **Cadastrar** ou **Acessar**.
- Se escolher **Cadastrar**, abre-se a tela para criação de usuário, salvando os dados em `dados/usuarios.json`.
- Se escolher **Acessar**, abre-se a tela de login. Se o login for válido:
  - Cria-se o arquivo `session.txt` para manter a sessão.
  - Abre a tela principal `main.py`.
- A tela principal (`main.py`) permite acesso a outras ações e componentes da plataforma.

---

## Observações

- As senhas dos usuários são armazenadas utilizando hash (via biblioteca Werkzeug) para segurança.
- A interface gráfica é feita com Tkinter.
- As imagens usadas no programa devem estar nas pastas `logo` e `imagens` conforme esperado pelo código.
- O sistema depende da estrutura de pastas estar correta para funcionar (ex: `dados/usuarios.json` e imagens).
