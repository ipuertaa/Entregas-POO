import tkinter as tk
from tkinter import messagebox, ttk
import math

# Colores implementados

BG_COLOR = "#f0f0f0"
BUTTON_COLOR = "#4a7a8c"
TEXT_COLOR = "#333333"
ENTRY_BG = "#ffffff"
LABEL_FONT = ("Arial", 10)
TITLE_FONT = ("Arial", 12, "bold")

# Clases para las figuras geométricas
 
 #Clase Principal que heredarán las figuras geométricas
class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0
        self.superficie = 0
    
    def calcular_volumen(self):
        pass
    
    def calcular_superficie(self):
        pass

#Subclases 

#Cilindro
class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()
    
    def calcular_volumen(self):
        return math.pi * self.altura * (self.radio ** 2)
    
    def calcular_superficie(self):
        area_lateral = 2 * math.pi * self.radio * self.altura
        area_base = 2 * math.pi * (self.radio ** 2)
        return area_lateral + area_base
    
#Esfera

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()
    
    def calcular_volumen(self):
        return (4/3) * math.pi * (self.radio ** 3)
    
    def calcular_superficie(self):
        return 4 * math.pi * (self.radio ** 2)

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()
    
    def calcular_volumen(self):
        return (self.base ** 2) * self.altura / 3
    
    def calcular_superficie(self):
        area_base = self.base ** 2
        area_lateral = 2 * self.base * self.apotema
        return area_base + area_lateral

# Ventanas con la interfaz interactiva

#Cilindro

class VentanaCilindro(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cilindro")
        self.geometry("350x300")
        self.resizable(False, False)
        self.configure(bg=BG_COLOR)
        
        # Frame principal

        main_frame = tk.Frame(self, bg=BG_COLOR, padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Título

        tk.Label(main_frame, text="Cálculo de Cilindro", font=TITLE_FONT, bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, columnspan=2, pady=(0, 15))
        
        # Campos de entrada

        tk.Label(main_frame, text="Radio [cm]:", font=LABEL_FONT, bg=BG_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.radio_entry = ttk.Entry(main_frame, font=LABEL_FONT)
        self.radio_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        tk.Label(main_frame, text="Altura [cm]:", font=LABEL_FONT, bg=BG_COLOR, fg=TEXT_COLOR).grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.altura_entry = ttk.Entry(main_frame, font=LABEL_FONT)
        self.altura_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        # Botón calcular

        calcular_btn = ttk.Button(main_frame, text="Calcular", command=self.calcular, style="Accent.TButton")
        calcular_btn.grid(row=3, column=0, columnspan=2, pady=15, sticky="ew")
        
        # Resultados

        self.volumen_label = tk.Label(main_frame, text="Volumen [cm³]:", font=LABEL_FONT, bg=BG_COLOR, fg=TEXT_COLOR)
        self.volumen_label.grid(row=4, column=0, columnspan=2, pady=5)
        
        self.superficie_label = tk.Label(main_frame, text="Superficie [cm²]:", font=LABEL_FONT, bg=BG_COLOR, fg=TEXT_COLOR)
        self.superficie_label.grid(row=5, column=0, columnspan=2, pady=5)
        
        # Peso de columnas
        main_frame.columnconfigure(1, weight=1)
    
    def calcular(self):
        try:
            radio = float(self.radio_entry.get())
            altura = float(self.altura_entry.get())
            
            cilindro = Cilindro(radio, altura)
            
            self.volumen_label.config(text=f"Volumen [cm³]: {cilindro.volumen:.2f}")
            self.superficie_label.config(text=f"Superficie [cm²]: {cilindro.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

#Esfera 

class VentanaEsfera(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Esfera")
        self.geometry("350x280")
        self.resizable(False, False)
        self.configure(bg=BG_COLOR)
        
        # Frame principal

        main_frame = tk.Frame(self, bg=BG_COLOR, padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Título

        tk.Label(main_frame, text="Cálculo de Esfera", font=TITLE_FONT, bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, columnspan=2, pady=(0, 15))
        
        # Campo de entrada

        tk.Label(main_frame, text="Radio [cm]:", font=LABEL_FONT, bg=BG_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.radio_entry = ttk.Entry(main_frame, font=LABEL_FONT)
        self.radio_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Botón calcular

        calcular_btn = ttk.Button(main_frame, text="Calcular", command=self.calcular, style="Accent.TButton")
        calcular_btn.grid(row=2, column=0, columnspan=2, pady=15, sticky="ew")
        
        # Resultados

        self.volumen_label = tk.Label(main_frame, text="Volumen [cm³]:", font=LABEL_FONT, bg=BG_COLOR, fg=TEXT_COLOR)
        self.volumen_label.grid(row=3, column=0, columnspan=2, pady=5)
        
        self.superficie_label = tk.Label(main_frame, text="Superficie [cm²]:", font=LABEL_FONT, bg=BG_COLOR, fg=TEXT_COLOR)
        self.superficie_label.grid(row=4, column=0, columnspan=2, pady=5)
        
        # Peso de columnas

        main_frame.columnconfigure(1, weight=1)
    
    def calcular(self):
        try:
            radio = float(self.radio_entry.get())
            
            esfera = Esfera(radio)
            
            self.volumen_label.config(text=f"Volumen [cm³]: {esfera.volumen:.2f}")
            self.superficie_label.config(text=f"Superficie [cm²]: {esfera.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un valor numérico válido")

#Pirámide

class VentanaPiramide(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pirámide")
        self.geometry("350x350")
        self.resizable(False, False)
        self.configure(bg=BG_COLOR)
        
        # Frame principal

        main_frame = tk.Frame(self, bg=BG_COLOR, padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Título

        tk.Label(main_frame, text="Cálculo de Pirámide", font=TITLE_FONT, bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, columnspan=2, pady=(0, 15))
        
        # Campos de entrada

        tk.Label(main_frame, text="Base [cm]:", font=LABEL_FONT, bg=BG_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.base_entry = ttk.Entry(main_frame, font=LABEL_FONT)
        self.base_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        tk.Label(main_frame, text="Altura [cm]:", font=LABEL_FONT, bg=BG_COLOR, fg=TEXT_COLOR).grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.altura_entry = ttk.Entry(main_frame, font=LABEL_FONT)
        self.altura_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        tk.Label(main_frame, text="Apotema [cm]:", font=LABEL_FONT, bg=BG_COLOR, fg=TEXT_COLOR).grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.apotema_entry = ttk.Entry(main_frame, font=LABEL_FONT)
        self.apotema_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        
        # Botón calcular

        calcular_btn = ttk.Button(main_frame, text="Calcular", command=self.calcular, style="Accent.TButton")
        calcular_btn.grid(row=4, column=0, columnspan=2, pady=15, sticky="ew")
        
        # Resultados

        self.volumen_label = tk.Label(main_frame, text="Volumen [cm³]:", font=LABEL_FONT, bg=BG_COLOR, fg=TEXT_COLOR)
        self.volumen_label.grid(row=5, column=0, columnspan=2, pady=5)
        
        self.superficie_label = tk.Label(main_frame, text="Superficie [cm²]:", font=LABEL_FONT, bg=BG_COLOR, fg=TEXT_COLOR)
        self.superficie_label.grid(row=6, column=0, columnspan=2, pady=5)
        
        # Peso de columnas
        main_frame.columnconfigure(1, weight=1)
    
    def calcular(self):
        try:
            base = float(self.base_entry.get())
            altura = float(self.altura_entry.get())
            apotema = float(self.apotema_entry.get())
            
            piramide = Piramide(base, altura, apotema)
            
            self.volumen_label.config(text=f"Volumen [cm³]: {piramide.volumen:.2f}")
            self.superficie_label.config(text=f"Superficie [cm²]: {piramide.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

# Ventana principal

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("400x200")
        self.resizable(False, False)
        self.configure(bg=BG_COLOR)
        
        # Estilo
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure("TButton", padding=6, relief="flat", background=BUTTON_COLOR, foreground="white")
        self.style.configure("Accent.TButton", padding=6, relief="flat", background="#5d9b9b", foreground="white")
        self.style.map("TButton", background=[("active", "#3a5f6f")])
        self.style.map("Accent.TButton", background=[("active", "#4a8a8a")])
        
        # Frame principal

        main_frame = tk.Frame(self, bg=BG_COLOR, padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Título

        tk.Label(main_frame, text="Calculadora de Figuras Geométricas", font=("Arial", 14, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=(0, 20))
        
        # Subtítulo

        tk.Label(main_frame, text="Seleccione una figura:", font=LABEL_FONT, bg=BG_COLOR, fg=TEXT_COLOR).pack()
        
        # Botones

        btn_frame = tk.Frame(main_frame, bg=BG_COLOR)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Cilindro", command=self.abrir_cilindro).pack(side="left", padx=5, ipadx=10)
        ttk.Button(btn_frame, text="Esfera", command=self.abrir_esfera).pack(side="left", padx=5, ipadx=10)
        ttk.Button(btn_frame, text="Pirámide", command=self.abrir_piramide).pack(side="left", padx=5, ipadx=10)
    
    def abrir_cilindro(self):
        VentanaCilindro(self)
    
    def abrir_esfera(self):
        VentanaEsfera(self)
    
    def abrir_piramide(self):
        VentanaPiramide(self)

# Ejecución

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()