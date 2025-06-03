
# coding: UTF-8

# acessar.py

import tkinter as tk
from tkinter import ttk, messagebox
from werkzeug.security import check_password_hash
from PIL import Image, ImageTk
import json
import os
import sys

get_cwd = os.getcwd ()

CAMINHO_USUARIOS = f"{get_cwd}\\dados\\usuarios.json"

def carregar_usuarios ():
    
    if not os.path.exists(CAMINHO_USUARIOS):
        
        return []
    
    try:
    
        with open(CAMINHO_USUARIOS, "r") as f:
    
            return json.load(f)
    
    except json.JSONDecodeError:
    
        with open(CAMINHO_USUARIOS, "w") as f:
    
            json.dump([], f)
        
        return []

def on_login_click ():
    
    email = entry_email.get()
    password = entry_password.get()

    if not email or not password:
        
        messagebox.showerror("404 - Not Found", "E-mail e Senha são obrigatórios!")
        return

    usuarios = carregar_usuarios()
    usuario = next((u for u in usuarios if u["email"].lower() == email.lower()), None)

    if usuario:
        
        if check_password_hash(usuario["senha"], password):

            with open("session.txt", "w") as f:
                
                json.dump({"usuario_id": usuario["id"], "email": usuario["email"]}, f)

            root.destroy()
            os.system("python3 main.py")
            sys.exit()
            
        else:
            
            messagebox.showerror("404 - Not Found", "E-mail ou Senha estão incorretos!")
            
    else:
        
        messagebox.showerror("404 - Not Found", "E-mail ou Senha estão incorretos!")

root = tk.Tk()
root.title("EDS - Acessar")
root.geometry("394x344")
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

frame_email = tk.Frame(root, bg="white")
frame_email.pack(pady=(30, 10))
label_email = tk.Label(frame_email, text="E-mail:", font=LABEL_FONT, fg=COR_TEXTO, bg="white")
label_email.pack(side="left", padx=(0, 10))
entry_email = tk.Entry(frame_email, font=ENTRY_FONT, fg=COR_TEXTO, width=28, relief="solid", bd=1)
entry_email.pack(side="left", ipady=5)

frame_senha = tk.Frame(root, bg="white")
frame_senha.pack(pady=(10, 10))
label_password = tk.Label(frame_senha, text="Senha:", font=LABEL_FONT, fg=COR_TEXTO, bg="white")
label_password.pack(side="left", padx=(0, 7))
entry_password = tk.Entry(frame_senha, show="*", font=ENTRY_FONT, fg=COR_TEXTO, width=28, relief="solid", bd=1)
entry_password.pack(side="left", ipady=5)

style = ttk.Style()
style.theme_use("default")
style.configure("Custom.TButton", foreground=COR_TEXTO, background="#E0E0E0", font=("Comic Sans MS", 14, "bold"), padding=4, borderwidth=0, relief="flat", focuscolor="none", width=19)
style.map("Custom.TButton", foreground=[("pressed", "#F0F0F0"), ("active", "#F0F0F0")], background=[("pressed", "#4F7086"), ("active", "#4F7086")])

button_login = ttk.Button(root, text="Acessar", command=on_login_click, style="Custom.TButton", takefocus=False)
button_login.pack(pady=30, ipadx=20, ipady=4)

root.mainloop()
