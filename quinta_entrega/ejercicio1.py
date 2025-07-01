import tkinter as tk
from tkinter import messagebox

class PruebaExcepcionesApp:
    """
    Esta clase representa la aplicación de prueba de excepciones con una interfaz gráfica.
    Permite al usuario interactuar con diferentes operaciones que pueden lanzar excepciones
    y muestra los resultados o los errores en la GUI.
    """
    def __init__(self, master):
        self.master = master
        master.title("Prueba de Excepciones en Python")
        master.geometry("400x450")
        master.resizable(False, False)

        # Configuración de estilos
        self.font_label = ("Arial", 10)
        self.font_button = ("Arial", 10, "bold")
        self.font_result = ("Courier New", 10)

        # Etiqueta de título
        self.title_label = tk.Label(master, text="Demostración de Excepciones", font=("Arial", 14, "bold"), fg="green")
        self.title_label.pack(pady=10)

        # --- Sección de División por Cero ---
        self.frame_division = tk.LabelFrame(master, text="División por Cero", padx=10, pady=10)
        self.frame_division.pack(pady=5, padx=10, fill="x")

        tk.Label(self.frame_division, text="Numerador:", font=self.font_label).grid(row=0, column=0, sticky="w", pady=2)
        self.numerador_entry = tk.Entry(self.frame_division, width=15)
        self.numerador_entry.grid(row=0, column=1, sticky="ew", pady=2)
        self.numerador_entry.insert(0, "10") # Valor por defecto

        tk.Label(self.frame_division, text="Denominador:", font=self.font_label).grid(row=1, column=0, sticky="w", pady=2)
        self.denominador_entry = tk.Entry(self.frame_division, width=15)
        self.denominador_entry.grid(row=1, column=1, sticky="ew", pady=2)
        self.denominador_entry.insert(0, "0") # Valor por defecto para probar excepción

        self.dividir_button = tk.Button(self.frame_division, text="Dividir", command=self._realizar_division, font=self.font_button, bg="#4CAF50", fg="white")
        self.dividir_button.grid(row=0, column=2, rowspan=2, padx=10)

        # --- Sección de Acceso a Índice ---
        self.frame_indice = tk.LabelFrame(master, text="Acceso a Índice de Lista", padx=10, pady=10)
        self.frame_indice.pack(pady=5, padx=10, fill="x")

        tk.Label(self.frame_indice, text="Índice a acceder:", font=self.font_label).grid(row=0, column=0, sticky="w", pady=2)
        self.indice_entry = tk.Entry(self.frame_indice, width=15)
        self.indice_entry.grid(row=0, column=1, sticky="ew", pady=2)
        self.indice_entry.insert(0, "5") # Valor por defecto para probar excepción

        self.acceder_indice_button = tk.Button(self.frame_indice, text="Acceder", command=self._acceder_indice, font=self.font_button, bg="#2196F3", fg="white")
        self.acceder_indice_button.grid(row=0, column=2, padx=10)

        # --- Sección de Conversión de Tipo ---
        self.frame_conversion = tk.LabelFrame(master, text="Conversión de Tipo", padx=10, pady=10)
        self.frame_conversion.pack(pady=5, padx=10, fill="x")

        tk.Label(self.frame_conversion, text="Texto a número:", font=self.font_label).grid(row=0, column=0, sticky="w", pady=2)
        self.texto_entry = tk.Entry(self.frame_conversion, width=15)
        self.texto_entry.grid(row=0, column=1, sticky="ew", pady=2)
        self.texto_entry.insert(0, "abc") # Valor por defecto para probar excepción

        self.convertir_button = tk.Button(self.frame_conversion, text="Convertir", command=self._convertir_tipo, font=self.font_button, bg="#FF9800", fg="white")
        self.convertir_button.grid(row=0, column=2, padx=10)

        # --- Área de Resultados ---
        self.result_label = tk.Label(master, text="Resultados:", font=("Arial", 12, "bold"), anchor="w")
        self.result_label.pack(pady=(10, 5), padx=10, fill="x")

        self.result_text = tk.Text(master, height=5, width=45, state="disabled", wrap="word", font=self.font_result, bg="#F0F0F0")
        self.result_text.pack(pady=(0, 10), padx=10, fill="both", expand=True)


    def _update_result_text(self, message, is_error=False):
        """
        Actualiza el área de texto de resultados con un mensaje.
        Si is_error es True, el mensaje se muestra en rojo.
        """
        self.result_text.config(state="normal")
        self.result_text.delete(1.0, tk.END)
        if is_error:
            self.result_text.config(fg="red")
        else:
            self.result_text.config(fg="black")
        self.result_text.insert(tk.END, message)
        self.result_text.config(state="disabled")

    def _realizar_division(self):
        """
        Intenta realizar una división y maneja las excepciones de valor y división por cero.
        """
        try:
            numerador_str = self.numerador_entry.get()
            denominador_str = self.denominador_entry.get()

            numerador = float(numerador_str)
            denominador = float(denominador_str)

            if denominador == 0:
                raise ZeroDivisionError("¡Error: No se puede dividir por cero!")

            resultado = numerador / denominador
            self._update_result_text(f"División exitosa: {numerador} / {denominador} = {resultado:.2f}")

        except ValueError:
            self._update_result_text("Error de entrada: Asegúrate de introducir números válidos para la división.", is_error=True)
            messagebox.showerror("Error de Entrada", "Por favor, introduce solo números en los campos de división.")
        except ZeroDivisionError as e:
            self._update_result_text(str(e), is_error=True)
            messagebox.showerror("Error de División", str(e))
        except Exception as e:
            self._update_result_text(f"Ocurrió un error inesperado al dividir: {e}", is_error=True)
            messagebox.showerror("Error Desconocido", f"Un error inesperado ocurrió: {e}")
        finally:
            print("Intento de división finalizado.") # Esto se imprime en la consola, no en la GUI

    def _acceder_indice(self):
        """
        Intenta acceder a un índice de una lista y maneja la excepción de índice fuera de rango.
        """
        mi_lista = [10, 20, 30, 40, 50]
        try:
            indice_str = self.indice_entry.get()
            indice = int(indice_str)

            if not (0 <= indice < len(mi_lista)):
                raise IndexError(f"¡Error: El índice {indice} está fuera de los límites (0-{len(mi_lista)-1}) de la lista!")

            valor = mi_lista[indice]
            self._update_result_text(f"Acceso a índice exitoso: mi_lista[{indice}] = {valor}")

        except ValueError:
            self._update_result_text("Error de entrada: Por favor, introduce un número entero para el índice.", is_error=True)
            messagebox.showerror("Error de Entrada", "Por favor, introduce un número entero válido para el índice.")
        except IndexError as e:
            self._update_result_text(str(e), is_error=True)
            messagebox.showerror("Error de Índice", str(e))
        except Exception as e:
            self._update_result_text(f"Ocurrió un error inesperado al acceder al índice: {e}", is_error=True)
            messagebox.showerror("Error Desconocido", f"Un error inesperado ocurrió: {e}")
        finally:
            print("Intento de acceso a índice finalizado.")

    def _convertir_tipo(self):
        """
        Intenta convertir una cadena a un número entero y maneja la excepción de valor.
        """
        try:
            texto = self.texto_entry.get()
            numero = int(texto)
            self._update_result_text(f"Conversión exitosa: '{texto}' convertido a {numero} (entero)")
        except ValueError:
            self._update_result_text(f"Error de conversión: '{texto}' no es un número entero válido.", is_error=True)
            messagebox.showerror("Error de Conversión", f"'{texto}' no se puede convertir a un número entero.")
        except Exception as e:
            self._update_result_text(f"Ocurrió un error inesperado al convertir el tipo: {e}", is_error=True)
            messagebox.showerror("Error Desconocido", f"Un error inesperado ocurrió: {e}")
        finally:
            print("Intento de conversión de tipo finalizado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PruebaExcepcionesApp(root)
    root.mainloop()