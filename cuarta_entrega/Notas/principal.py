import tkinter as tk
from .ventana_principal import VentanaPrincipal

def main():
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    main()