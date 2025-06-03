
# coding: UTF-8

# user_manager.py

import json
import os
from tkinter import messagebox

get_cwd = os.getcwd ()

CAMINHO_USUARIOS = f"{get_cwd}\\dados\\usuarios.json"

def atualizar_usuario (usuario_atualizado):

    if not os.path.exists(CAMINHO_USUARIOS):

        messagebox.showerror("404 - Not Found", "Arquivo de usuários não encontrado.")
        return False

    with open(CAMINHO_USUARIOS, "r", encoding="utf-8") as f:
    
        try:
        
            usuarios = json.load(f)
        
        except json.JSONDecodeError:
            
            messagebox.showerror("404 - Not Found", "Erro ao ler usuários.")
            return False

    atualizado = False
    
    for i, u in enumerate(usuarios):
        
        if u["id"] == usuario_atualizado["id"]:

            if "cursos_iniciados" not in usuario_atualizado:
                
                usuario_atualizado["cursos_iniciados"] = []

            if "cursos_finalizados" not in usuario_atualizado:
                
                usuario_atualizado["cursos_finalizados"] = []
                
            usuarios[i].update(usuario_atualizado)
            atualizado = True
            break

    if not atualizado:
        
        messagebox.showerror("404 - Not Found", "Usuário logado não encontrado para atualização.")
        return False

    try:
        
        with open(CAMINHO_USUARIOS, "w", encoding="utf-8") as f:
            
            json.dump(usuarios, f, indent=4, ensure_ascii=False)
            
        return True
        
    except Exception as e:
        
        messagebox.showerror("404 - Not Found", f"Falha ao salvar usuário atualizado:\n{e}")
        return False