
# coding: UTF-8

# certificate_generator.py

import os
import datetime
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from tkinter import messagebox

get_cwd = os.getcwd ()

def gerar_certificado (usuario, curso):

    nome_usuario = usuario["nome"]
    sobrenome_usuario = usuario.get("sobrenome", "")
    nome_completo = f"{nome_usuario} {sobrenome_usuario}".strip()

    titulo_curso = curso["titulo"]
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
    nome_arquivo = f"certificado_{titulo_curso.replace(' ', '_')}.pdf"

    c = canvas.Canvas(nome_arquivo, pagesize=landscape(A4))
    largura, altura = landscape(A4)

    caminho_logo = f"{get_cwd}\\logo\\eds.png"
    logo_width = 194
    logo_height = 69

    if os.path.exists(caminho_logo):
        
        x_logo = (largura - logo_width) / 2
        y_logo = altura - logo_height - 59
        
        try:
            
            c.drawImage(caminho_logo, x_logo, y_logo, width=logo_width, height=logo_height, preserveAspectRatio=True, mask='auto')
            
        except Exception as e:
            
            print(f"[ERRO ao carregar a logo]: {e}")
    
    else:
    
        print("[AVISO] Logo não encontrada:", caminho_logo)

    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(largura / 2, altura - 169, "CERTIFICADO DE CONCLUSÃO DE CURSO")

    c.setFont("Helvetica", 18)
    c.drawCentredString(largura / 2, altura - 200, "Certificamos que")
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(largura / 2, altura - 240, nome_completo)

    c.setFont("Helvetica", 18)
    c.drawCentredString(largura / 2, altura - 285, "Concluiu com êxito o curso:")
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(largura / 2, altura - 320, f"{titulo_curso}")

    c.setFont("Helvetica", 16)
    c.drawCentredString(largura / 2, altura - 370, f"Emitido em {data_atual}")

    c.setFont("Helvetica-Oblique", 12)
    c.drawRightString(largura - 50, 50, "EDS - Educação Digital Segura")

    c.save()

    messagebox.showinfo("200 - OK", "Certificado gerado com Sucesso!")
    return nome_arquivo