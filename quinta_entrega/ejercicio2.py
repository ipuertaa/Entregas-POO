import tkinter as tk
from tkinter import messagebox, scrolledtext

class Vendedor:
    """
    Clase Vendedor que modela un vendedor con nombre, apellidos y edad.
    Implementa validaciones de edad con lanzamiento de excepciones.
    """
    def __init__(self, nombre, apellidos):
        """
        Constructor de la clase Vendedor.
        Inicializa el nombre y los apellidos. La edad se establece a través de verificar_edad.
        """
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not isinstance(apellidos, str) or not apellidos.strip():
            raise ValueError("Los apellidos no pueden estar vacíos.")

        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = None  # La edad se inicializa a None y se asigna con verificar_edad

    def imprimir(self):
        """
        Método que devuelve una cadena con los datos del vendedor.
        """
        # Aseguramos que la edad esté establecida antes de imprimir
        edad_str = str(self.edad) if self.edad is not None else "No establecida"
        return (f"--- Datos del Vendedor ---\n"
                f"Nombre: {self.nombre}\n"
                f"Apellidos: {self.apellidos}\n"
                f"Edad: {edad_str}")

    def verificar_edad(self, edad):
        """
        Método que verifica que la edad de un vendedor es apropiada.
        Lanza IllegalArgumentException (Python: ValueError) si la edad no cumple los requisitos.
        """
        if not isinstance(edad, int):
            raise TypeError()

        if (edad < 0) or (edad > 120):
            # Equivalente a IllegalArgumentException para rangos inválidos
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        elif edad < 18:
            # Equivalente a IllegalArgumentException para ser mayor de edad
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        else:
            self.edad = edad
            return True # Retorna True si la edad es válida y se ha asignado

class VendedorApp:
    """
    Aplicación de interfaz gráfica para gestionar la creación de objetos Vendedor.
    Maneja la entrada de datos y muestra los resultados o errores.
    """
    def __init__(self, master):
        self.master = master
        master.title("Gestión de Vendedor")
        master.geometry("450x450")
        master.resizable(False, False)
        master.config(bg="#72cc9e")

        # Configuración de estilos
        self.font_label = ("Arial", 10)
        self.font_entry = ("Arial", 10)
        self.font_button = ("Arial", 10, "bold")
        self.font_result = ("Courier New", 10)

        self.vendedor_actual = None # Para almacenar el objeto Vendedor si se crea

        # --- Frame para la entrada de datos ---
        self.input_frame = tk.LabelFrame(master, text="Datos del Vendedor", padx=15, pady=15, bg="#72cc9e")
        self.input_frame.pack(pady=15, padx=20, fill="x")

        # Nombre
        tk.Label(self.input_frame, text="Nombre:", font=self.font_label, bg="#72cc9e").grid(row=0, column=0, sticky="w", pady=5, padx=5)
        self.nombre_entry = tk.Entry(self.input_frame, width=30, font=self.font_entry, bd=1, relief="solid")
        self.nombre_entry.grid(row=0, column=1, sticky="ew", pady=5, padx=5)

        # Apellidos
        tk.Label(self.input_frame, text="Apellidos:", font=self.font_label, bg="#72cc9e").grid(row=1, column=0, sticky="w", pady=5, padx=5)
        self.apellidos_entry = tk.Entry(self.input_frame, width=30, font=self.font_entry, bd=1, relief="solid")
        self.apellidos_entry.grid(row=1, column=1, sticky="ew", pady=5, padx=5)

        # Edad
        tk.Label(self.input_frame, text="Edad:", font=self.font_label, bg="#72cc9e").grid(row=2, column=0, sticky="w", pady=5, padx=5)
        self.edad_entry = tk.Entry(self.input_frame, width=30, font=self.font_entry, bd=1, relief="solid")
        self.edad_entry.grid(row=2, column=1, sticky="ew", pady=5, padx=5)

        # Configurar la expansión de la columna para que los campos de entrada se estiren
        self.input_frame.grid_columnconfigure(1, weight=1)

        # --- Frame para los botones ---
        self.button_frame = tk.Frame(master, bg="#72cc9e")
        self.button_frame.pack(pady=10)

        self.register_button = tk.Button(self.button_frame, text="Registrar Vendedor", command=self._registrar_vendedor,
                                         font=self.font_button, bg="#4CAF50", fg="white", padx=10, pady=5, relief="raised")
        self.register_button.pack(side=tk.LEFT, padx=10)

        self.clear_button = tk.Button(self.button_frame, text="Limpiar Campos", command=self._limpiar_campos,
                                       font=self.font_button, bg="#f44336", fg="white", padx=10, pady=5, relief="raised")
        self.clear_button.pack(side=tk.RIGHT, padx=10)

        # --- Área de resultados ---
        self.result_label = tk.Label(master, text="Estado/Datos del Vendedor:", font=("Arial", 12, "bold"), anchor="w", bg="#72cc9e")
        self.result_label.pack(pady=(10, 5), padx=20, fill="x")

        self.result_text = scrolledtext.ScrolledText(master, height=10, width=50, state="disabled", wrap="word",
                                                     font=self.font_result, bg="#e8e8e8", fg="black", bd=1, relief="sunken")
        self.result_text.pack(pady=(0, 20), padx=20, fill="both", expand=True)

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

    def _limpiar_campos(self):
        """
        Limpia todos los campos de entrada y el área de resultados.
        """
        self.nombre_entry.delete(0, tk.END)
        self.apellidos_entry.delete(0, tk.END)
        self.edad_entry.delete(0, tk.END)
        self._update_result_text("") # Limpiar el texto de resultados
        self.vendedor_actual = None # Reiniciar el objeto vendedor

    def _registrar_vendedor(self):
        """
        Captura los datos de la GUI, intenta crear y verificar el vendedor.
        Maneja las excepciones y actualiza la interfaz.
        """
        nombre = self.nombre_entry.get().strip()
        apellidos = self.apellidos_entry.get().strip()
        edad_str = self.edad_entry.get().strip()

        # Limpiar cualquier mensaje anterior
        self._update_result_text("")

        try:
            # 1. Validar y convertir la edad a entero
            if not edad_str:
                raise ValueError("La edad no puede estar vacía.")
            edad = int(edad_str)

            # 2. Intentar crear el objeto Vendedor (puede lanzar ValueError por nombre/apellidos vacíos)
            vendedor = Vendedor(nombre, apellidos)

            # 3. Verificar la edad del vendedor (puede lanzar ValueError)
            vendedor.verificar_edad(edad)

            # Si todo es exitoso:
            self.vendedor_actual = vendedor
            self._update_result_text(f"Vendedor registrado exitosamente:\n{self.vendedor_actual.imprimir()}", is_error=False)
            messagebox.showinfo("Éxito", "Vendedor registrado correctamente.")

        except ValueError as e:
            # Captura de las excepciones de validación de edad y campos vacíos
            self._update_result_text(f"Error de validación: {e}", is_error=True)
            messagebox.showerror("Error de Validación", str(e))
        except TypeError as e:
            # Captura si la edad no es un número entero
            self._update_result_text(f"Error de tipo de dato: {e}", is_error=True)
            messagebox.showerror("Error de Tipo", "La edad debe ser un número entero.")
        except Exception as e:
            # Captura cualquier otra excepción inesperada
            self._update_result_text(f"Ocurrió un error inesperado: {e}", is_error=True)
            messagebox.showerror("Error Desconocido", f"Un error inesperado ocurrió: {e}")

# --- Punto de entrada de la aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = VendedorApp(root)
    root.mainloop()