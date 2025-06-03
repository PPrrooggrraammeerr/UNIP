
# coding: UTF-8

# main.py

import tkinter as tk
import session_manager
import main_window

def main():
    
    usuario_logado = session_manager.carregar_sessao ()
    
    root = tk.Tk ()
    
    app = main_window.MainWindow (root, usuario_logado)
    
    root.mainloop ()

if __name__ == "__main__":
    
    main ()