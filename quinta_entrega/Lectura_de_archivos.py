import tkinter as tk
from tkinter import filedialog, messagebox
import os # Importamos os para manejar rutas de archivos

# --- Paleta de Colores Sobrios y Elegantes ---
COLOR_FONDO_CLARO = "#F8F8F8"       # Gris muy claro, casi blanco
COLOR_FONDO_MEDIO = "#E0E0E0"       # Gris claro para elementos destacados
COLOR_TEXTO_OSCURO = "#333333"      # Gris oscuro para el texto principal
COLOR_BORDE = "#BBBBBB"             # Gris para bordes sutiles
COLOR_BOTON_PRIMARIO = "#607D8B"    # Azul pizarra oscuro, profesional
COLOR_BOTON_TEXTO_CLARO = "white"   # Texto blanco para botones primarios
COLOR_BOTON_SECUNDARIO = "#9E9E9E"  # Gris medio para botones secundarios

class LectorArchivosApp:
    """
    Clase principal que define la aplicación de lectura de archivos
    con una interfaz gráfica Tkinter.
    """
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        ventana_principal.title("Lector de Archivos")
        ventana_principal.geometry("750x550") # Tamaño inicial de la ventana
        ventana_principal.minsize(600, 400) # Tamaño mínimo para redimensionar
        ventana_principal.configure(bg=COLOR_FONDO_CLARO)

        # --- Configuración del Marco Principal ---
        # Un contenedor para organizar los widgets con un padding y color de fondo.
        self.marco_principal = tk.Frame(ventana_principal, padx=25, pady=25, bg=COLOR_FONDO_CLARO)
        self.marco_principal.pack(fill=tk.BOTH, expand=True)

        # --- Sección de Entrada de Archivo ---
        # Etiqueta para indicar al usuario que ingrese la ruta del archivo.
        self.etiqueta_ruta_archivo = tk.Label(self.marco_principal, text="Ruta del archivo:",
                                              bg=COLOR_FONDO_CLARO, fg=COLOR_TEXTO_OSCURO,
                                              font=("Segoe UI", 10, "bold"))
        self.etiqueta_ruta_archivo.grid(row=0, column=0, pady=(0, 10), sticky=tk.W)

        # Campo de entrada para que el usuario escriba o vea la ruta del archivo.
        self.entrada_ruta_archivo = tk.Entry(self.marco_principal, font=("Segoe UI", 9),
                                             bg="white", fg=COLOR_TEXTO_OSCURO,
                                             bd=1, relief=tk.SOLID, highlightbackground=COLOR_BORDE, highlightthickness=1)
        self.entrada_ruta_archivo.grid(row=0, column=1, pady=(0, 10), padx=(0, 10), sticky=tk.EW)

        # Botón para abrir el explorador de archivos y seleccionar uno.
        self.boton_explorar = tk.Button(self.marco_principal, text="Explorar",
                                        command=self._explorar_archivo,
                                        bg=COLOR_BOTON_SECUNDARIO, fg=COLOR_BOTON_TEXTO_CLARO,
                                        font=("Segoe UI", 9, "bold"), bd=0, relief=tk.FLAT,
                                        activebackground=COLOR_BOTON_SECUNDARIO, activeforeground=COLOR_BOTON_TEXTO_CLARO)
        self.boton_explorar.grid(row=0, column=2, pady=(0, 10), sticky=tk.E)

        # --- Sección de Botones de Acción ---
        # Contenedor para los botones de acción para una mejor organización.
        self.marco_botones = tk.Frame(self.marco_principal, bg=COLOR_FONDO_CLARO)
        self.marco_botones.grid(row=1, column=0, columnspan=3, pady=(15, 20), sticky=tk.EW)
        self.marco_botones.grid_columnconfigure(0, weight=1) # Permite que el primer botón se expanda
        self.marco_botones.grid_columnconfigure(1, weight=1) # Permite que el segundo botón se expanda


        # Botón para leer el archivo y mostrar su contenido original.
        self.boton_leer_mostrar = tk.Button(self.marco_botones, text="Leer y Mostrar",
                                            command=self._leer_y_mostrar_archivo,
                                            bg=COLOR_BOTON_PRIMARIO, fg=COLOR_BOTON_TEXTO_CLARO,
                                            font=("Segoe UI", 10, "bold"), bd=0, relief=tk.FLAT,
                                            activebackground=COLOR_BOTON_PRIMARIO, activeforeground=COLOR_BOTON_TEXTO_CLARO)
        self.boton_leer_mostrar.grid(row=0, column=0, padx=(0, 10), sticky=tk.EW)

        # Botón para leer el archivo y mostrar su contenido en mayúsculas.
        self.boton_mostrar_mayusculas = tk.Button(self.marco_botones, text="Mostrar en MAYÚSCULAS",
                                                 command=self._mostrar_en_mayusculas,
                                                 bg=COLOR_BOTON_PRIMARIO, fg=COLOR_BOTON_TEXTO_CLARO,
                                                 font=("Segoe UI", 10, "bold"), bd=0, relief=tk.FLAT,
                                                 activebackground=COLOR_BOTON_PRIMARIO, activeforeground=COLOR_BOTON_TEXTO_CLARO)
        self.boton_mostrar_mayusculas.grid(row=0, column=1, sticky=tk.EW)

        # --- Área de Visualización del Contenido ---
        # Área de texto para mostrar el contenido del archivo.
        self.area_texto_contenido = tk.Text(self.marco_principal, wrap=tk.WORD,
                                            bg=COLOR_FONDO_MEDIO, fg=COLOR_TEXTO_OSCURO,
                                            font=("Consolas", 9),
                                            bd=1, relief=tk.SOLID, highlightbackground=COLOR_BORDE, highlightthickness=1)
        self.area_texto_contenido.grid(row=2, column=0, columnspan=3, pady=(0, 0), sticky=tk.NSEW)

        # Barra de desplazamiento vertical para el área de texto.
        self.barra_desplazamiento_y = tk.Scrollbar(self.marco_principal, command=self.area_texto_contenido.yview)
        self.barra_desplazamiento_y.grid(row=2, column=3, sticky=tk.NS)
        self.area_texto_contenido.config(yscrollcommand=self.barra_desplazamiento_y.set)

        # --- Configuración de Expansión de Grid ---
        # Permite que la columna central y la fila del área de texto se expandan
        # cuando la ventana se redimensiona.
        self.marco_principal.grid_columnconfigure(1, weight=1)
        self.marco_principal.grid_rowconfigure(2, weight=1)

    def _explorar_archivo(self):
        """
        Abre un diálogo de selección de archivo y actualiza el campo de entrada
        con la ruta del archivo seleccionado.
        """
        ruta_archivo = filedialog.askopenfilename(
            initialdir=os.getcwd(), # Inicia en el directorio actual del script
            title="Seleccionar archivo de texto",
            filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
        )
        if ruta_archivo:
            self.entrada_ruta_archivo.delete(0, tk.END)
            self.entrada_ruta_archivo.insert(0, ruta_archivo)

    def _leer_contenido_archivo(self, ruta_archivo):
        """
        Lee el contenido de un archivo de texto especificado por la ruta.
        Maneja errores de archivo no encontrado o de lectura.
        """
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                return contenido
        except FileNotFoundError:
            messagebox.showerror("Error", f"El archivo '{ruta_archivo}' no fue encontrado.")
            return None
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")
            return None

    def _mostrar_contenido_en_area(self, contenido):
        """
        Borra el contenido actual del área de texto y lo reemplaza con el nuevo contenido.
        """
        self.area_texto_contenido.delete("1.0", tk.END)
        self.area_texto_contenido.insert(tk.END, contenido)

    def _leer_y_mostrar_archivo(self):
        """
        Obtiene la ruta del archivo, lo lee y muestra su contenido en el área de texto.
        """
        ruta_archivo = self.entrada_ruta_archivo.get()
        if not ruta_archivo:
            messagebox.showwarning("Advertencia", "Por favor, ingrese la ruta de un archivo.")
            return

        contenido = self._leer_contenido_archivo(ruta_archivo)
        if contenido is not None:
            self._mostrar_contenido_en_area(contenido)

    def _mostrar_en_mayusculas(self):
        """
        Obtiene la ruta del archivo, lo lee y muestra su contenido
        convertido a mayúsculas en el área de texto.
        """
        ruta_archivo = self.entrada_ruta_archivo.get()
        if not ruta_archivo:
            messagebox.showwarning("Advertencia", "Por favor, ingrese la ruta de un archivo.")
            return

        contenido = self._leer_contenido_archivo(ruta_archivo)
        if contenido is not None:
            contenido_mayusculas = contenido.upper()
            self._mostrar_contenido_en_area(contenido_mayusculas)

# --- Punto de Entrada de la Aplicación ---
if __name__ == "__main__":
    ventana_raiz = tk.Tk()
    app = LectorArchivosApp(ventana_raiz)
    ventana_raiz.mainloop()