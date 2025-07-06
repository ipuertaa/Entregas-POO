import tkinter as tk
from tkinter import messagebox, scrolledtext
import os

# Define el nombre del archivo donde se guardarán los registros.
# En Linux, esto creará el archivo en el directorio donde se ejecute el script.
FILE_NAME = "asistencia.txt"

class AsistenciaApp:
    def __init__(self, master):
        """
        Inicializa la aplicación de registro de asistencia.
        Configura la ventana principal y los widgets de la interfaz gráfica.
        """
        self.master = master
        master.title("Registro de Asistencia")
        master.geometry("600x500") # Establece un tamaño inicial para la ventana
        master.resizable(True, True) # Permite redimensionar la ventana

        # Configuración de la fuente para una mejor legibilidad
        self.font_label = ("Arial", 12)
        self.font_entry = ("Arial", 12)
        self.font_button = ("Arial", 12, "bold")
        self.font_text_area = ("Consolas", 10)

        # --- Widgets de Entrada ---
        # Marco para las entradas
        input_frame = tk.Frame(master, padx=10, pady=10, bd=2, relief="groove")
        input_frame.pack(pady=10, padx=10, fill="x")

        # Etiqueta y campo de entrada para el Nombre
        self.label_nombre = tk.Label(input_frame, text="Nombre:", font=self.font_label)
        self.label_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_nombre = tk.Entry(input_frame, width=40, font=self.font_entry)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Etiqueta y campo de entrada para el Número de Contacto
        self.label_contacto = tk.Label(input_frame, text="Número de Contacto:", font=self.font_label)
        self.label_contacto.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_contacto = tk.Entry(input_frame, width=40, font=self.font_entry)
        self.entry_contacto.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Configurar la expansión de columnas para que los campos de entrada se expandan
        input_frame.grid_columnconfigure(1, weight=1)

        # --- Botones CRUD ---
        # Marco para los botones
        button_frame = tk.Frame(master, padx=10, pady=10)
        button_frame.pack(pady=10, padx=10, fill="x")

        # Botón Crear
        self.btn_crear = tk.Button(button_frame, text="Crear Registro", command=self.create_record,
                                   font=self.font_button, bg="#4CAF50", fg="white", relief="raised", bd=3)
        self.btn_crear.pack(side="left", expand=True, fill="x", padx=5, pady=5)

        # Botón Leer
        self.btn_leer = tk.Button(button_frame, text="Leer Registros", command=self.read_records,
                                  font=self.font_button, bg="#2196F3", fg="white", relief="raised", bd=3)
        self.btn_leer.pack(side="left", expand=True, fill="x", padx=5, pady=5)

        # Botón Actualizar
        self.btn_actualizar = tk.Button(button_frame, text="Actualizar Registro", command=self.update_record,
                                       font=self.font_button, bg="#FFC107", fg="black", relief="raised", bd=3)
        self.btn_actualizar.pack(side="left", expand=True, fill="x", padx=5, pady=5)

        # Botón Eliminar
        self.btn_eliminar = tk.Button(button_frame, text="Eliminar Registro", command=self.delete_record,
                                     font=self.font_button, bg="#F44336", fg="white", relief="raised", bd=3)
        self.btn_eliminar.pack(side="left", expand=True, fill="x", padx=5, pady=5)

        # --- Área de Mensajes/Resultados ---
        self.message_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, height=10, font=self.font_text_area,
                                                     bg="#e0e0e0", fg="#333333", bd=2, relief="sunken")
        self.message_area.pack(pady=10, padx=10, fill="both", expand=True)
        self.message_area.insert(tk.END, "Bienvenido al programa de registro de asistencia.\n")
        self.message_area.config(state="disabled") # Hacer el área de texto de solo lectura

    def _display_message(self, message):
        """
        Muestra un mensaje en el área de texto de la interfaz.
        """
        self.message_area.config(state="normal") # Habilitar para escribir
        self.message_area.delete(1.0, tk.END) # Limpiar contenido anterior
        self.message_area.insert(tk.END, message + "\n")
        self.message_area.config(state="disabled") # Deshabilitar de nuevo

    def _get_all_records(self):
        """
        Lee todos los registros del archivo y los devuelve como una lista de diccionarios.
        Cada diccionario tiene las claves 'nombre' y 'contacto'.
        Retorna una lista vacía si el archivo no existe o está vacío.
        """
        records = []
        try:
            with open(FILE_NAME, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line: # Asegurarse de que la línea no esté vacía
                        parts = line.split(',')
                        if len(parts) == 2:
                            records.append({'nombre': parts[0], 'contacto': parts[1]})
            return records
        except FileNotFoundError:
            return []
        except Exception as e:
            messagebox.showerror("Error de Lectura", f"Ocurrió un error al leer el archivo: {e}")
            return []

    def _write_all_records(self, records):
        """
        Escribe una lista de registros (diccionarios) en el archivo, sobrescribiendo el contenido existente.
        """
        try:
            with open(FILE_NAME, 'w') as f:
                for record in records:
                    f.write(f"{record['nombre']},{record['contacto']}\n")
        except Exception as e:
            messagebox.showerror("Error de Escritura", f"Ocurrió un error al escribir en el archivo: {e}")

    def create_record(self):
        """
        Crea un nuevo registro de asistencia y lo guarda en el archivo.
        Si el archivo no existe, lo crea.
        """
        nombre = self.entry_nombre.get().strip()
        contacto = self.entry_contacto.get().strip()

        if not nombre or not contacto:
            messagebox.showwarning("Entrada Inválida", "Por favor, ingrese el nombre y el número de contacto.")
            return

        try:
            # Abrir el archivo en modo de añadir ('a') para no sobrescribir los datos existentes
            # 'x' para crear un nuevo archivo si no existe, 'a' para añadir si existe
            with open(FILE_NAME, 'a') as f:
                f.write(f"{nombre},{contacto}\n")
            self._display_message(f"Registro creado exitosamente:\nNombre: {nombre}\nContacto: {contacto}")
            self.entry_nombre.delete(0, tk.END) # Limpiar campos
            self.entry_contacto.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error de Creación", f"Ocurrió un error al crear el registro: {e}")

    def read_records(self):
        """
        Lee y muestra todos los registros de asistencia desde el archivo.
        """
        records = self._get_all_records()
        if not records:
            self._display_message("No hay registros de asistencia para mostrar.")
            return

        display_text = "--- Registros de Asistencia ---\n"
        for i, record in enumerate(records):
            display_text += f"{i+1}. Nombre: {record['nombre']}, Contacto: {record['contacto']}\n"
        self._display_message(display_text)

    def update_record(self):
        """
        Actualiza un registro existente. El usuario debe ingresar el nombre del registro a actualizar
        y los nuevos datos.
        """
        nombre_a_actualizar = self.entry_nombre.get().strip()
        nuevo_contacto = self.entry_contacto.get().strip()

        if not nombre_a_actualizar:
            messagebox.showwarning("Entrada Inválida", "Por favor, ingrese el nombre del registro a actualizar.")
            return
        if not nuevo_contacto:
            messagebox.showwarning("Entrada Inválida", "Por favor, ingrese el nuevo número de contacto.")
            return

        records = self._get_all_records()
        found = False
        updated_records = []

        for record in records:
            if record['nombre'].lower() == nombre_a_actualizar.lower():
                record['contacto'] = nuevo_contacto
                found = True
            updated_records.append(record)

        if found:
            self._write_all_records(updated_records)
            self._display_message(f"Registro de '{nombre_a_actualizar}' actualizado exitosamente a nuevo contacto: {nuevo_contacto}.")
            self.entry_nombre.delete(0, tk.END) # Limpiar campos
            self.entry_contacto.delete(0, tk.END)
        else:
            messagebox.showinfo("No Encontrado", f"No se encontró ningún registro con el nombre '{nombre_a_actualizar}'.")
            self._display_message(f"No se encontró ningún registro con el nombre '{nombre_a_actualizar}'.")


    def delete_record(self):
        """
        Elimina un registro existente del archivo basado en el nombre.
        """
        nombre_a_eliminar = self.entry_nombre.get().strip()

        if not nombre_a_eliminar:
            messagebox.showwarning("Entrada Inválida", "Por favor, ingrese el nombre del registro a eliminar.")
            return

        records = self._get_all_records()
        initial_record_count = len(records)
        # Filtra los registros, manteniendo solo aquellos que no coinciden con el nombre a eliminar
        remaining_records = [record for record in records if record['nombre'].lower() != nombre_a_eliminar.lower()]

        if len(remaining_records) < initial_record_count:
            self._write_all_records(remaining_records)
            self._display_message(f"Registro de '{nombre_a_eliminar}' eliminado exitosamente.")
            self.entry_nombre.delete(0, tk.END) # Limpiar campos
            self.entry_contacto.delete(0, tk.END)
        else:
            messagebox.showinfo("No Encontrado", f"No se encontró ningún registro con el nombre '{nombre_a_eliminar}'.")
            self._display_message(f"No se encontró ningún registro con el nombre '{nombre_a_eliminar}'.")

        # Opcional: Eliminar el archivo si no quedan registros
        if not remaining_records and os.path.exists(FILE_NAME):
            try:
                os.remove(FILE_NAME)
                self._display_message(f"Todos los registros han sido eliminados. El archivo '{FILE_NAME}' también ha sido eliminado.")
            except Exception as e:
                messagebox.showerror("Error al Eliminar Archivo", f"No se pudo eliminar el archivo '{FILE_NAME}': {e}")


# Punto de entrada de la aplicación
if __name__ == "__main__":
    root = tk.Tk() # Crea la ventana principal de Tkinter
    app = AsistenciaApp(root) # Instancia la aplicación
    root.mainloop() # Inicia el bucle principal de eventos de Tkinter
