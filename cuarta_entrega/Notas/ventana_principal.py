import tkinter as tk
from tkinter import messagebox
from .notas import Notas

class VentanaPrincipal():
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Notas")
        master.geometry("450x550")
        master.resizable(False, False)
        master.configure(bg="#F0F0F0")

        self.notas_obj = Notas()

        # Frame principal para organizar los elementos
        self.main_frame = tk.Frame(master, bg="#F0F0F0", padx=20, pady=20)
        self.main_frame.pack(expand=True)

        # Título
        self.title_label = tk.Label(self.main_frame, text="Ingreso de Notas", font=("Helvetica", 16, "bold"), bg="#F0F0F0", fg="#333333")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Entradas de notas
        self.entry_notas = []
        for i in range(5):
            label = tk.Label(self.main_frame, text=f"Nota {i+1}:", font=("Helvetica", 10), bg="#F0F0F0", fg="#555555")
            label.grid(row=i+1, column=0, sticky="w", pady=5)
            entry = tk.Entry(self.main_frame, width=20, font=("Helvetica", 10), bd=2, relief="groove")
            entry.grid(row=i+1, column=1, pady=5)
            self.entry_notas.append(entry)

        # Botones
        self.button_frame = tk.Frame(self.main_frame, bg="#F0F0F0")
        self.button_frame.grid(row=6, column=0, columnspan=2, pady=20)

        self.calculate_button = tk.Button(self.button_frame, text="Calcular", command=self.calcular_notas,
                                          bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"),
                                          width=10, relief="raised", bd=3)
        self.calculate_button.pack(side=tk.LEFT, padx=10)

        self.clear_button = tk.Button(self.button_frame, text="Limpiar", command=self.limpiar_campos,
                                       bg="#f44336", fg="white", font=("Helvetica", 10, "bold"),
                                       width=10, relief="raised", bd=3)
        self.clear_button.pack(side=tk.LEFT, padx=10)

        # Sección de Resultados
        self.results_frame = tk.LabelFrame(self.main_frame, text="Resultados", font=("Helvetica", 12, "bold"),
                                           bg="#E0E0E0", fg="#333333", padx=15, pady=15, bd=2, relief="groove")
        self.results_frame.grid(row=7, column=0, columnspan=2, pady=(10, 0), sticky="ew")

        # Etiquetas y campos de resultados
        self.labels_resultados = {}
        resultados_textos = ["Promedio:", "Desviación Estándar:", "Mayor Nota:", "Menor Nota:"]
        for i, texto in enumerate(resultados_textos):
            label = tk.Label(self.results_frame, text=texto, font=("Helvetica", 10), bg="#E0E0E0", fg="#555555")
            label.grid(row=i, column=0, sticky="w", pady=5)
            value_label = tk.Label(self.results_frame, text="", font=("Helvetica", 10, "bold"), bg="#E0E0E0", fg="#000000")
            value_label.grid(row=i, column=1, sticky="w", pady=5)
            self.labels_resultados[texto] = value_label

    def calcular_notas(self):
        notas_ingresadas = []
        for entry in self.entry_notas:
            try:
                nota = float(entry.get())
                if not (0 <= nota <= 10): # Validación básica para notas entre 0 y 10
                    messagebox.showwarning("Entrada Inválida", "Por favor, ingrese notas entre 0 y 10.")
                    return
                notas_ingresadas.append(nota)
            except ValueError:
                messagebox.showerror("Error de Entrada", "Por favor, ingrese solo números válidos para las notas.")
                return

        if len(notas_ingresadas) != 5:
            messagebox.showwarning("Entrada Incompleta", "Debe ingresar las 5 notas.")
            return

        try:
            self.notas_obj.set_notas(notas_ingresadas)
            promedio = self.notas_obj.calcular_promedio()
            desviacion = self.notas_obj.calcular_desviacion()
            mayor = self.notas_obj.calcular_mayor()
            menor = self.notas_obj.calcular_menor()

            self.labels_resultados["Promedio:"].config(text=f"{promedio:.2f}")
            self.labels_resultados["Desviación Estándar:"].config(text=f"{desviacion:.2f}")
            self.labels_resultados["Mayor Nota:"].config(text=f"{mayor:.2f}")
            self.labels_resultados["Menor Nota:"].config(text=f"{menor:.2f}")

        except ValueError as e:
            messagebox.showerror("Error de Cálculo", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")


    def limpiar_campos(self):
        for entry in self.entry_notas:
            entry.delete(0, tk.END)
        for label_text in self.labels_resultados:
            self.labels_resultados[label_text].config(text="")