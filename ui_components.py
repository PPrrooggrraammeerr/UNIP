
# coding: UTF-8

# ui_components.py

import tkinter as tk
from tkinter import messagebox

def criar_frame_rolagem (container):

    frame_scroll = tk.Frame(container, bg="white")
    frame_scroll.pack(expand=True, fill="both", padx=5, pady=(5, 10))

    canvas = tk.Canvas(frame_scroll, bg="white", highlightthickness=0)
    scrollbar = tk.Scrollbar(frame_scroll, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    conteudo_frame = tk.Frame(canvas, bg="white")
    canvas.create_window((0, 0), window=conteudo_frame, anchor="nw")

    def configurar_scroll (event):
        
        canvas.configure(scrollregion=canvas.bbox("all"))

    conteudo_frame.bind("<Configure>", configurar_scroll)

    def rolar_com_mouse (event):
        
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", rolar_com_mouse)

    return conteudo_frame, canvas

def criar_card_curso (container, curso, bg_color="#ecf0f1", btn_text="Iniciar", btn_color="#3498db", comando=None):
    
    frame = tk.Frame(container, bg=bg_color, padx=20, pady=10, bd=1, relief="solid")
    frame.pack(fill="x", pady=5)

    texto_frame = tk.Frame(frame, bg=bg_color)
    texto_frame.grid(row=0, column=0, sticky="w")

    tk.Label(texto_frame, text=curso["titulo"], font=("Comic Sans MS", 14, "bold"), bg=bg_color, fg="#4F7086").pack(anchor="w")
    tk.Label(texto_frame, text=curso["descricao"], font=("Comic Sans MS", 12), bg=bg_color, fg="#4F7086").pack(anchor="w", pady=(0, 5))

    botao = tk.Button(frame, text=btn_text, bg=btn_color, fg="white", font=("Comic Sans MS", 11, "bold"), padx=10, pady=5, activebackground=btn_color, activeforeground="white", relief="flat", bd=0, cursor="hand2")

    if comando:
        
        botao.config(command=lambda: comando(curso, botao))

    botao.grid(row=0, column=1, sticky="e", padx=10)
    frame.grid_columnconfigure(0, weight=1)

    return botao

def atualizar_conteudo (label_titulo, label_conteudo, titulo, conteudo):

    label_titulo['text'] = titulo
    label_conteudo['text'] = conteudo

def limpar_area_conteudo (area_principal, excecoes=[]):

    for widget in area_principal.winfo_children():
        
        if widget not in excecoes:
            
            widget.destroy()