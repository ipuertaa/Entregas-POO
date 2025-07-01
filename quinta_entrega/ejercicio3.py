import tkinter as tk
from tkinter import messagebox
import math

class CalculosNumericos:
    """
    Clase que realiza cálculos de logaritmo neperiano y raíz cuadrada.
    Todos los métodos son estáticos y manejan excepciones para valores no válidos.
    """

    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        """
        Calcula el logaritmo neperiano de un valor.
        Lanza ValueError si el valor no es positivo.
        """
        if valor <= 0:
            # En Python, para errores de valor de argumento, se usa ValueError
            raise ValueError("El valor para el logaritmo neperiano debe ser un número positivo.")
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        """
        Calcula la raíz cuadrada de un valor.
        Lanza ValueError si el valor no es positivo.
        """
        if valor < 0:
            # En Python, la función math.sqrt ya lanza ValueError para negativos.
            # Sin embargo, lo manejamos explícitamente para un mensaje más claro.
            raise ValueError("El valor para la raíz cuadrada no puede ser negativo.")
        return math.sqrt(valor)

class CalculosApp:
    """
    Aplicación de interfaz gráfica para realizar cálculos numéricos
    y manejar sus excepciones.
    """
    def __init__(self, master):
        self.master = master
        master.title("Cálculos Numéricos")
        master.geometry("400x350")
        master.resizable(False, False)
        master.config(bg="#5ac4d7")

        # Configuración de estilos
        self.font_label = ("Arial", 11)
        self.font_entry = ("Arial", 11)
        self.font_button = ("Arial", 11, "bold")
        self.font_result = ("Courier New", 10)

        # --- Frame principal de entrada ---
        self.input_frame = tk.LabelFrame(master, text="Ingresar Valor", padx=15, pady=15, bg="#5ac4d7")
        self.input_frame.pack(pady=20, padx=20, fill="x")

        tk.Label(self.input_frame, text="Valor Numérico:", font=self.font_label, bg="#5ac4d7").pack(pady=5)
        self.valor_entry = tk.Entry(self.input_frame, width=25, font=self.font_entry, bd=1, relief="solid", justify="center")
        self.valor_entry.pack(pady=5)
        self.valor_entry.insert(0, "10.0") # Valor por defecto

        self.calculate_button = tk.Button(self.input_frame, text="Calcular", command=self._realizar_calculos,
                                           font=self.font_button, bg="#4CAF50", fg="white", padx=15, pady=7, relief="raised")
        self.calculate_button.pack(pady=10)

        # --- Área de resultados ---
        self.result_label = tk.Label(master, text="Resultados:", font=("Arial", 12, "bold"), anchor="w", bg="#5ac4d7")
        self.result_label.pack(pady=(10, 5), padx=20, fill="x")

        self.log_result_label = tk.Label(master, text="Logaritmo Neperiano: ", font=self.font_result, bg="#353e40", anchor="w", padx=5, pady=5, relief="groove", bd=1)
        self.log_result_label.pack(pady=5, padx=20, fill="x")

        self.sqrt_result_label = tk.Label(master, text="Raíz Cuadrada: ", font=self.font_result, bg="#353e40", anchor="w", padx=5, pady=5, relief="groove", bd=1)
        self.sqrt_result_label.pack(pady=5, padx=20, fill="x")

        self.error_message_label = tk.Label(master, text="", font=("Arial", 10, "bold"), fg="red", bg="#5ac4d7", anchor="center")
        self.error_message_label.pack(pady=10, padx=20, fill="x")

    def _update_results(self, log_msg, sqrt_msg, error_msg=""):
        """Actualiza las etiquetas de resultados y el mensaje de error."""
        self.log_result_label.config(text=f"Logaritmo Neperiano: {log_msg}")
        self.sqrt_result_label.config(text=f"Raíz Cuadrada: {sqrt_msg}")
        self.error_message_label.config(text=error_msg)

    def _realizar_calculos(self):
        """
        Captura el valor de la GUI, intenta realizar los cálculos y maneja las excepciones.
        """
        valor_str = self.valor_entry.get().strip()
        self._update_results("", "", "") # Limpiar resultados y errores previos

        try:
            valor = float(valor_str) # Intenta convertir a double (float en Python)

            log_res = "N/A"
            sqrt_res = "N/A"
            error_happened = False
            error_message_parts = []

            # Calcular Logaritmo Neperiano
            try:
                log_res = f"{CalculosNumericos.calcular_logaritmo_neperiano(valor):.4f}"
            except ValueError as e:
                log_res = "Error"
                error_message_parts.append(f"Logaritmo: {e}")
                error_happened = True
            except Exception as e:
                log_res = "Error"
                error_message_parts.append(f"Logaritmo (inesperado): {e}")
                error_happened = True

            # Calcular Raíz Cuadrada
            try:
                sqrt_res = f"{CalculosNumericos.calcular_raiz_cuadrada(valor):.4f}"
            except ValueError as e:
                sqrt_res = "Error"
                error_message_parts.append(f"Raíz Cuadrada: {e}")
                error_happened = True
            except Exception as e:
                sqrt_res = "Error"
                error_message_parts.append(f"Raíz Cuadrada (inesperado): {e}")
                error_happened = True

            final_error_msg = "\n".join(error_message_parts) if error_happened else ""
            self._update_results(log_res, sqrt_res, final_error_msg)

            if error_happened:
                messagebox.showerror("Error en Cálculos", final_error_msg)
            else:
                messagebox.showinfo("Cálculos Exitosos", "Ambos cálculos se realizaron correctamente.")

        except ValueError:
            # Captura si el string no pudo convertirse a float (InputMismatchException de Java)
            self._update_results("Error", "Error", "Error: Por favor, ingrese un valor numérico válido.")
            messagebox.showerror("Error de Entrada", "El valor ingresado no es un número válido.")
        except Exception as e:
            # Captura cualquier otra excepción inesperada
            self._update_results("Error", "Error", f"Un error inesperado ocurrió: {e}")
            messagebox.showerror("Error Desconocido", f"Un error inesperado ocurrió: {e}")


# --- Punto de entrada de la aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculosApp(root)
    root.mainloop()