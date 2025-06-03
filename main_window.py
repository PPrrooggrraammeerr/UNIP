
# coding: UTF-8

# main_window.py

import tkinter as tk
from tkinter import messagebox
import user_manager
import course_manager
import session_manager
import certificate_generator
import ui_components

class MainWindow:
    
    def __init__ (self, root, usuario_logado):
        
        self.root = root
        self.usuario_logado = usuario_logado
        self.setup_ui()

    def setup_ui (self):

        self.root.title("Educação Digital Segura - Home")
        self.root.geometry("870x600")
        self.root.configure(bg="#f2f2f2")

        self.menu = tk.Frame(self.root, bg="#2c3e50", width=200)
        self.menu.pack(side="left", fill="y")

        tk.Label(self.menu, text="MENU", bg="#2c3e50", fg="white", font=("Comic Sans MS", 14, "bold")).pack(pady=10)

        botoes = [("Meus Cursos", self.meus_cursos), ("Explorar Cursos", self.explorar_cursos), ("Certificados", self.certificados), ("Sair", self.sair)]

        for texto, comando in botoes:
            
            tk.Button(self.menu, text=texto, command=comando, bg="#34495e", fg="white", font=("Comic Sans MS", 12), relief="flat", padx=10, pady=10).pack(fill="x", pady=5)

        self.area_principal = tk.Frame(self.root, bg="white")
        self.area_principal.pack(expand=True, fill="both")

        self.label_boas_vindas = tk.Label(self.area_principal, text="EDS - Bem-vindo(a) à Plataforma de Cursos!", font=("Comic Sans MS", 18, "bold"), bg="white")
        self.label_boas_vindas.pack(pady=(10, 5))

        self.label_titulo = tk.Label(self.area_principal, text="Painel Inicial", font=("Comic Sans MS", 16), bg="white")
        self.label_titulo.pack(pady=(0, 2))

        self.label_conteudo = tk.Label(self.area_principal, text="", font=("Comic Sans MS", 12), bg="white")
        self.label_conteudo.pack(pady=(0, 0))

    def sair (self):

        session_manager.remover_sessao()
        self.root.destroy()

    def meus_cursos (self):

        ui_components.atualizar_conteudo(self.label_titulo, self.label_conteudo, "Meus Cursos", "Acompanhe os cursos que você iniciou abaixo:")
        ui_components.limpar_area_conteudo(self.area_principal, [self.label_boas_vindas, self.label_titulo, self.label_conteudo])

        cursos_disponiveis = course_manager.carregar_cursos()
        cursos_usuario = course_manager.obter_cursos_iniciados(self.usuario_logado, cursos_disponiveis)

        if not cursos_usuario:
            
            tk.Label(self.area_principal, text="Você ainda não iniciou nenhum curso.", font=("Comic Sans MS", 12), bg="white").pack(pady=20)
            return

        frame_cursos, _ = ui_components.criar_frame_rolagem(self.area_principal)

        for curso in cursos_usuario:
            
            botao = ui_components.criar_card_curso(frame_cursos, curso, bg_color="#dff9fb", btn_text="Finalizar Curso", btn_color="#109010", comando=self.finalizar_curso)
            
            if curso["id"] in self.usuario_logado.get("cursos_finalizados", []):
                
                botao.config(text="Curso Finalizado", state="disabled", bg="#ff0000", fg="white", disabledforeground="white", font=("Comic Sans MS", 11, "bold"), activebackground="#ff0000", activeforeground="white", relief="flat", bd=0, cursor="arrow")

    def finalizar_curso (self, curso, botao):

        if course_manager.finalizar_curso(self.usuario_logado, curso):
            
            if user_manager.atualizar_usuario(self.usuario_logado):

                botao.config(text="Curso Finalizado", state="disabled", bg="#ff0000", fg="white", disabledforeground="white", font=("Comic Sans MS", 11, "bold"), activebackground="#ff0000", activeforeground="white", relief="flat", bd=0, cursor="arrow")
                messagebox.showinfo("200 - OK", f"Parabéns! Você acaba de finalizar o Curso: {curso['titulo']}")

    def explorar_cursos (self):

        ui_components.atualizar_conteudo(self.label_titulo, self.label_conteudo, "Explorar Cursos", "Inicie com uma variedade de opções abaixo:")
        ui_components.limpar_area_conteudo(self.area_principal, [self.label_boas_vindas, self.label_titulo, self.label_conteudo])

        cursos_disponiveis = course_manager.carregar_cursos()

        if not cursos_disponiveis:

            tk.Label(self.area_principal, text="Nenhum curso disponível no momento.", font=("Comic Sans MS", 12), bg="white").pack(pady=20)
            return

        frame_cursos, _ = ui_components.criar_frame_rolagem(self.area_principal)

        for curso in cursos_disponiveis:
            
            botao = ui_components.criar_card_curso(frame_cursos, curso, bg_color="#ecf0f1", btn_text="Começar Curso", btn_color="#3498db", comando=self.iniciar_curso)

            if curso["id"] in self.usuario_logado.get("cursos_finalizados", []):
                
                botao.config(text="Curso Finalizado", state="disabled", bg="#ff0000", fg="white", disabledforeground="white", font=("Comic Sans MS", 11, "bold"), activebackground="#ff0000", activeforeground="white", relief="flat", bd=0, cursor="arrow")

            elif curso["id"] in self.usuario_logado.get("cursos_iniciados", []):
                
                botao.config(text="Em Andamento", state="disabled", bg="#109010", fg="white", disabledforeground="white", font=("Comic Sans MS", 11, "bold"), activebackground="#109010", activeforeground="white", relief="flat", bd=0, cursor="arrow")

    def iniciar_curso (self, curso, botao):
        
        if course_manager.iniciar_curso(self.usuario_logado, curso):
            
            if user_manager.atualizar_usuario(self.usuario_logado):
                
                botao.config(text="Em Andamento", state="disabled", bg="#109010", fg="white", disabledforeground="white", font=("Comic Sans MS", 11, "bold"), activebackground="#2A7B9B", activeforeground="white", relief="flat", bd=0, cursor="arrow")
                ui_components.atualizar_conteudo(self.label_titulo, self.label_conteudo, curso["titulo"], f"Você iniciou o curso: {curso['titulo']}\n\n{curso['descricao']}")


    def certificados (self):

        ui_components.atualizar_conteudo(self.label_titulo, self.label_conteudo, "Certificados", "Meus certificados conquistados abaixo:")
        ui_components.limpar_area_conteudo(self.area_principal, [self.label_boas_vindas, self.label_titulo, self.label_conteudo])

        cursos_disponiveis = course_manager.carregar_cursos()
        cursos_finalizados = course_manager.obter_cursos_finalizados(self.usuario_logado, cursos_disponiveis)

        if not cursos_finalizados:
            
            tk.Label(self.area_principal, text="Nenhum certificado disponível ainda.", font=("Comic Sans MS", 12), bg="white").pack(pady=20)
            return

        frame_certificados, _ = ui_components.criar_frame_rolagem(self.area_principal)

        for curso in cursos_finalizados:
            
            frame = tk.Frame(frame_certificados, bg="#e8f9f1", padx=20, pady=10, bd=1, relief="solid")
            frame.pack(fill="x", pady=5)

            texto_frame = tk.Frame(frame, bg="#e8f9f1")
            texto_frame.grid(row=0, column=0, sticky="w")

            tk.Label(texto_frame, text=curso["titulo"], font=("Comic Sans MS", 14, "bold"), bg="#e8f9f1", fg="#4F7086").pack(anchor="w")
            tk.Label(texto_frame, text=curso["descricao"], font=("Comic Sans MS", 12), bg="#e8f9f1", fg="#4F7086").pack(anchor="w", pady=(0, 5))

            tk.Button(frame, text="Ter Certificado", command=lambda c=curso: self.gerar_certificado(c), bg="#f1c40f", fg="white", font=("Comic Sans MS", 11, "bold"), padx=10, pady=5, activebackground="#f1c40f", activeforeground="white", relief="flat", bd=0, cursor="hand2").grid(row=0, column=1, sticky="e", padx=10)

            frame.grid_columnconfigure(0, weight=1)

    def gerar_certificado (self, curso):

        certificate_generator.gerar_certificado(self.usuario_logado, curso)