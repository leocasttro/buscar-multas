import tkinter as tk  # Importe o módulo tkinter

from gui import MinhaAplicacao

def main():
    root = tk.Tk()  # Crie uma instância do objeto Tk
    app = MinhaAplicacao(root)
    app.run()

if __name__ == "__main__":
    main()
