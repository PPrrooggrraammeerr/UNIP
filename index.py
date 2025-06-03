
# coding: UTF-8

# index.py

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from werkzeug.security import generate_password_hash, check_password_hash
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os
from tkinter import ttk

get_cwd = os.getcwd ()

def call_login_function ():
    
    os.system ('python3 acessar.py')

def call_cadastrar_function ():
    
    os.system ('python3 cadastrar.py')

root = tk.Tk()
root.title("EDS - Educação Digital Segura")
root.geometry("904x470")
root.configure(bg="white")

logo_image = Image.open(f"{get_cwd}\\logo\\eds.png")
logo_image = logo_image.resize((104, 79))

logo_image_tk = ImageTk.PhotoImage(logo_image)

header_frame = tk.Frame(root, bg="white")
header_frame.pack(side="top", pady=4, anchor="w")

logo_label = tk.Label(header_frame, image=logo_image_tk, bg="white")
logo_label.pack(side="left", padx=10)

label_title = tk.Label(header_frame, text="EDS - Educação Digital Segura", font=("Comic Sans MS", 16, "bold"), fg="#4F7086", bg="white")
label_title.pack(side="left", padx=(0, 124))

style = ttk.Style()
style.theme_use("default")

style = ttk.Style()
style.theme_use("default")

style.configure("Custom.TButton", foreground="#4F7086", background="#E0E0E0", font=("Comic Sans MS", 14, "bold"), padding=6, borderwidth=0, relief="flat", focuscolor="none")

style.map("Custom.TButton", foreground=[("pressed", "#F0F0F0"), ("active", "#F0F0F0")], background=[("pressed", "#4F7086"), ("active", "#4F7086")])

button_login = ttk.Button(header_frame, text="Acessar", command=call_login_function, style="Custom.TButton", takefocus=False)
button_login.pack(side="left", padx=6, ipadx=12, ipady=6)

button_register = ttk.Button(header_frame, text="Cadastrar", command=call_cadastrar_function, style="Custom.TButton", takefocus=False)
button_register.pack(side="left", padx=6, ipadx=12, ipady=6)

label_catalogo = tk.Label(root, text="Categorias e Exibição de Cursos da Plataforma:", font=("Comic Sans MS", 17, "bold"), fg="#4F7086", bg="white")
label_catalogo.pack(pady=(20, 10))

catalogo_frame = tk.Frame(root, bg="white")
catalogo_frame.pack()

curso_imagens_paths = [f"{get_cwd}\\imagens\\pensamento_logico_computacional.png", f"{get_cwd}\\imagens\\programacao_em_python.png", f"{get_cwd}\\imagens\\seguranca_digital.png",]
curso_nomes = ["Lógica Computacional", "Programação em Python", "Segurança Digital"]
curso_imagens_tk = []

for path, nome in zip(curso_imagens_paths, curso_nomes):
    
    frame_curso = tk.Frame(catalogo_frame, bg="white")
    frame_curso.pack(side="left", padx=10)

    img = Image.open(path)
    img = img.resize((194, 194))
    img_tk = ImageTk.PhotoImage(img)
    curso_imagens_tk.append(img_tk)

    img_label = tk.Label(frame_curso, image=img_tk, bg="white")
    img_label.pack()

    nome_label = tk.Label(frame_curso, text=nome, font=("Comic Sans MS", 14, "bold"), fg="#4F7086", bg="white")
    nome_label.pack(pady=(6, 0))
    
root.mainloop()
