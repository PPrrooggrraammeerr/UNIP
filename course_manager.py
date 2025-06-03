
# coding: UTF-8

# couse_manager.py

import json
import os
from tkinter import messagebox

get_cwd = os.getcwd ()

CAMINHO_CURSOS = f"{get_cwd}\\dados\\cursos.json"

def carregar_cursos ():

    if not os.path.exists(CAMINHO_CURSOS):
        
        messagebox.showwarning("404 - Not Found", f"Arquivo não encontrado:\n{CAMINHO_CURSOS}")
        return []

    with open(CAMINHO_CURSOS, "r", encoding="utf-8") as arquivo:
        
        try:
            
            return json.load(arquivo)
            
        except json.JSONDecodeError as e:
            
            messagebox.showerror("404 - Not Found", f"Erro ao ler cursos.json:\n{e}")
            return []

def iniciar_curso (usuario, curso):

    if "cursos_iniciados" not in usuario:
        
        usuario["cursos_iniciados"] = []

    if curso["id"] not in usuario["cursos_iniciados"]:
        
        usuario["cursos_iniciados"].append(curso["id"])
        return True
        
    return False

def finalizar_curso (usuario, curso):

    if "cursos_finalizados" not in usuario:

        usuario["cursos_finalizados"] = []

    if curso["id"] not in usuario["cursos_finalizados"]:
        
        usuario["cursos_finalizados"].append(curso["id"])
        return True
        
    return False

def obter_cursos_iniciados (usuario, todos_cursos):

    ids_iniciados = usuario.get("cursos_iniciados", [])
    return [curso for curso in todos_cursos if curso["id"] in ids_iniciados]

def obter_cursos_finalizados (usuario, todos_cursos):

    ids_finalizados = usuario.get("cursos_finalizados", [])
    return [curso for curso in todos_cursos if curso["id"] in ids_finalizados]