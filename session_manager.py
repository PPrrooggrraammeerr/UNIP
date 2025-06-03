
# coding: UTF-8

# session_manager.py

import json
import os
from tkinter import messagebox

get_cwd = os.getcwd ()

CAMINHO_USUARIOS = f"{get_cwd}\\dados\\usuarios.json"
CAMINHO_SESSAO = "session.txt"

def carregar_sessao ():

    if not os.path.exists(CAMINHO_SESSAO):

        messagebox.showerror("404 - Not Found", "Nenhum usuário está logado.")
        exit()

    with open(CAMINHO_SESSAO, "r", encoding="utf-8") as f:
        
        sessao = json.load(f)

    with open(CAMINHO_USUARIOS, "r", encoding="utf-8") as f:
        
        usuarios = json.load(f)

    usuario = next((u for u in usuarios if u["id"] == sessao["usuario_id"] and u["email"] == sessao["email"]), None)

    if not usuario:
        
        messagebox.showerror("404 - Not Found", "Usuário da sessão não encontrado.")
        exit()

    return usuario

def remover_sessao ():

    if os.path.exists(CAMINHO_SESSAO):
        
        os.remove(CAMINHO_SESSAO)