
# coding: UTF-8

# cadastrar.py

import tkinter as tk
from tkinter import ttk, messagebox
from werkzeug.security import generate_password_hash
from PIL import Image, ImageTk
import json
import os
import sys

get_cwd = os.getcwd ()

CAMINHO_USUARIOS = f"{get_cwd}\\dados\\usuarios.json"

def carregar_usuarios():
    
    if not os.path.exists(CAMINHO_USUARIOS):
    
        with open(CAMINHO_USUARIOS, "w") as f:

            json.dump([], f)

    try:
        
        with open(CAMINHO_USUARIOS, "r") as f:
            
            return json.load(f)
            
    except json.JSONDecodeError:
        
        with open(CAMINHO_USUARIOS, "w") as f:
            
            json.dump([], f)
            
        return []

def salvar_usuarios (lista_usuarios):
    
    with open(CAMINHO_USUARIOS, "w") as f:
        
        json.dump(lista_usuarios, f, indent=4)

def on_register_click ():
    
    nome = entry_name.get()
    sobrenome = entry_sobrenome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    senha = entry_password.get()

    if not nome or not sobrenome or not idade or not email or not senha:
        
        messagebox.showerror("Error 404 - Not Found", "Todos os Campos devem ser Preenchidos!")
        return

    if not idade.isdigit() or int(idade) <= 0:
        
        messagebox.showerror("Error 404 - Not Found", "Idade deve ser um Número Válido!")
        return

    usuarios = carregar_usuarios()
    
    for usuario in usuarios:
        
        if usuario["email"].lower() == email.lower():
            
            messagebox.showerror("Error 404 - Not Found", "E-mail já está registrado!")
            return

    novo_id = max([u["id"] for u in usuarios], default=0) + 1

    novo_usuario = {
        "id": novo_id,
        "nome": nome,
        "sobrenome": sobrenome,
        "idade": int(idade),
        "email": email,
        "senha": generate_password_hash(senha),
        "cursos_iniciados": [],
        "cursos_finalizados": []
    }

    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)

    messagebox.showinfo("200 - OK", "Cadastro feito com sucesso!")
    entry_name.delete(0, tk.END)
    entry_sobrenome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    
    root.destroy()
    sys.exit()

root = tk.Tk()
root.title("EDS - Cadastrar")
root.geometry("394x484")
root.configure(bg="white")

info_frame = tk.Frame(root, bg="white")
info_frame.pack(pady=(20, 10))

logo_image = Image.open(f"{get_cwd}\\logo\\eds.png")
logo_image = logo_image.resize((94, 69))
icon_tk = ImageTk.PhotoImage(logo_image)

icon_label = tk.Label(info_frame, image=icon_tk, bg="white")
icon_label.pack(side="left", padx=(0, 10))

text_label = tk.Label(info_frame, text="Bem-vindo(a) à EDS", font=("Comic Sans MS", 14, "bold"), fg="#4F7086", bg="white")
text_label.pack(side="left")

LABEL_FONT = ("Helvetica", 12, "bold")
ENTRY_FONT = ("Helvetica", 12)
COR_TEXTO = "#4F7086"

frame_nome = tk.Frame(root, bg="white")
frame_nome.pack(pady=(10, 10))
tk.Label(frame_nome, text="Nome:", font=LABEL_FONT, fg=COR_TEXTO, bg="white").pack(side="left", padx=(0, 14))
entry_name = tk.Entry(frame_nome, font=ENTRY_FONT, fg=COR_TEXTO, width=28, relief="solid", bd=1)
entry_name.pack(side="left", ipady=5)

frame_sobrenome = tk.Frame(root, bg="white")
frame_sobrenome.pack(pady=(10, 10))
tk.Label(frame_sobrenome, text="Sobre:", font=LABEL_FONT, fg=COR_TEXTO, bg="white").pack(side="left", padx=(0, 12))
entry_sobrenome = tk.Entry(frame_sobrenome, font=ENTRY_FONT, fg=COR_TEXTO, width=28, relief="solid", bd=1)
entry_sobrenome.pack(side="left", ipady=5)

frame_idade = tk.Frame(root, bg="white")
frame_idade.pack(pady=(10, 10))
tk.Label(frame_idade, text="Idade:", font=LABEL_FONT, fg=COR_TEXTO, bg="white").pack(side="left", padx=(0, 16))
entry_idade = tk.Entry(frame_idade, font=ENTRY_FONT, fg=COR_TEXTO, width=28, relief="solid", bd=1)
entry_idade.pack(side="left", ipady=5)

frame_email = tk.Frame(root, bg="white")
frame_email.pack(pady=(10, 10))
tk.Label(frame_email, text="E-mail:", font=LABEL_FONT, fg=COR_TEXTO, bg="white").pack(side="left", padx=(0, 11))
entry_email = tk.Entry(frame_email, font=ENTRY_FONT, fg=COR_TEXTO, width=28, relief="solid", bd=1)
entry_email.pack(side="left", ipady=5)

frame_senha = tk.Frame(root, bg="white")
frame_senha.pack(pady=(10, 10))
tk.Label(frame_senha, text="Senha:", font=LABEL_FONT, fg=COR_TEXTO, bg="white").pack(side="left", padx=(0, 9))
entry_password = tk.Entry(frame_senha, show="*", font=ENTRY_FONT, fg=COR_TEXTO, width=28, relief="solid", bd=1)
entry_password.pack(side="left", ipady=5)

style = ttk.Style()
style.theme_use("default")
style.configure("Custom.TButton", foreground="#4F7086", background="#E0E0E0", font=("Comic Sans MS", 14, "bold"), padding=4, borderwidth=0, relief="flat", focuscolor="none", width=19)
style.map("Custom.TButton", foreground=[("pressed", "#F0F0F0"), ("active", "#F0F0F0")], background=[("pressed", "#4F7086"), ("active", "#4F7086")])

button_register = ttk.Button(root, text="Cadastrar", command=on_register_click, style="Custom.TButton", takefocus=False)
button_register.pack(pady=30, ipadx=20, ipady=4)

root.mainloop()
