import tkinter as tk # Esto es para hacer la ventana y los botones.
from tkinter import ttk, messagebox # Esto nos da más opciones para la ventana y los mensajes emergentes.

class Programador:
    def __init__(self, nombre, apellidos):
        # Cuando creamos un programador, le guardamos su nombre y sus apellidos.
        self.nombre = nombre
        self.apellidos = apellidos
    
    def __str__(self):
        # Si queremos mostrar el programador, nos devuelve su nombre completo.
        return f"{self.nombre} {self.apellidos}"

class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        # Aquí guardamos los detalles del equipo: su nombre, universidad y el lenguaje que usarán.
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.programadores = [] # Aquí vamos a poner a los programadores del equipo.
        self.MAX_PROGRAMADORES = 3 # El equipo no puede tener más de 3 programadores.
        self.MIN_PROGRAMADORES = 2 # El equipo necesita al menos 2 programadores para ser válido.
    
    def esta_lleno(self):
        # Nos dice si el equipo ya tiene 3 programadores y no podemos añadir más.
        return len(self.programadores) >= self.MAX_PROGRAMADORES
    
    def agregar_programador(self, programador):
        # Intentamos añadir un programador.
        if self.esta_lleno():
            # Si ya hay 3, avisamos que está lleno.
            raise Exception("El equipo está completo (máximo 3 programadores).")
        self.programadores.append(programador) # Si no está lleno, lo añadimos.
    
    @staticmethod
    def validar_campo(campo):
        # Revisa que los campos de texto no estén vacíos, no tengan números y no sean muy largos.
        if not campo.strip():
            raise Exception("Este campo no puede estar vacío.")
        
        if any(c.isdigit() for c in campo):
            raise Exception("No se permiten números en nombres/apellidos.")
        
        if len(campo) > 20:
            raise Exception("Máximo 20 caracteres permitidos.")
    
    def cumple_minimo_integrantes(self):
        # Nos dice si el equipo tiene suficientes programadores (al menos 2).
        return len(self.programadores) >= self.MIN_PROGRAMADORES

class AplicacionMaraton:
    def __init__(self, root):
        # Esto se ejecuta cuando abres la aplicación. Prepara la ventana.
        self.root = root
        self.equipo = None # Al principio, no hay ningún equipo creado.
        self.programadores_agregados = 0 # Contamos cuántos programadores hemos añadido.
        
        self.configurar_interfaz() # Pone todos los botones y cajas en la ventana.
        self.centrar_ventana() # Mueve la ventana al centro de la pantalla.
    
    def centrar_ventana(self):
        # Calcula dónde poner la ventana para que quede en el medio.
        self.root.update_idletasks()
        ancho = 450   # El ancho de la ventana.
        alto = 550    # El alto de la ventana.
        # Estas líneas calculan la posición.
        x = (self.root.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.root.winfo_screenheight() // 2) - (alto // 2)
        self.root.geometry(f'{ancho}x{alto}+{x}+{y}') # Mueve la ventana.
    
    def configurar_interfaz(self):
        # Aquí se diseña la ventana: título, tamaño y si se puede cambiar de tamaño.
        self.root.title("Maratón de Programación")
        self.root.geometry("450x550")
        self.root.resizable(False, False)
        
        # Esto le da un estilo bonito a los elementos (letras, botones).
        estilo = ttk.Style()
        estilo.configure('Titulo.TLabel', font=('Arial', 11, 'bold'))
        estilo.configure('Campo.TEntry', font=('Arial', 9), padding=3)
        estilo.configure('Boton.TButton', font=('Arial', 9), padding=4)
        
        # El área principal de la ventana.
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill='both', expand=True)
        
        # Sección para los datos del equipo.
        frame_equipo = ttk.LabelFrame(main_frame, text=" Datos del Equipo ", padding=8)
        frame_equipo.pack(fill='x', pady=5)
        
        # Cajas para el nombre del equipo, universidad y lenguaje.
        ttk.Label(frame_equipo, text="Nombre del equipo:").grid(row=0, column=0, sticky='w', pady=2)
        self.txt_nombre_equipo = ttk.Entry(frame_equipo, width=30, style='Campo.TEntry')
        self.txt_nombre_equipo.grid(row=0, column=1, padx=5)
        
        ttk.Label(frame_equipo, text="Universidad:").grid(row=1, column=0, sticky='w', pady=2)
        self.txt_universidad = ttk.Entry(frame_equipo, width=30, style='Campo.TEntry')
        self.txt_universidad.grid(row=1, column=1, padx=5)
        
        ttk.Label(frame_equipo, text="Lenguaje:").grid(row=2, column=0, sticky='w', pady=2)
        self.txt_lenguaje = ttk.Entry(frame_equipo, width=30, style='Campo.TEntry')
        self.txt_lenguaje.grid(row=2, column=1, padx=5)
        
        # Sección para añadir programadores.
        frame_prog = ttk.LabelFrame(main_frame, text=" Programadores ", padding=8)
        frame_prog.pack(fill='x', pady=5)
        
        # Cajas para el nombre y apellidos del programador.
        ttk.Label(frame_prog, text="Nombre:").grid(row=0, column=0, sticky='w', pady=2)
        self.txt_nombre_programador = ttk.Entry(frame_prog, width=30, style='Campo.TEntry')
        self.txt_nombre_programador.grid(row=0, column=1, padx=5)
        
        ttk.Label(frame_prog, text="Apellidos:").grid(row=1, column=0, sticky='w', pady=2)
        self.txt_apellidos_programador = ttk.Entry(frame_prog, width=30, style='Campo.TEntry')
        self.txt_apellidos_programador.grid(row=1, column=1, padx=5)
        
        # Botón para añadir un programador.
        self.btn_agregar = ttk.Button(frame_prog, text="Agregar", style='Boton.TButton', command=self.agregar_programador)
        self.btn_agregar.grid(row=2, column=1, pady=5, sticky='e')
        
        # Muestra cuántos programadores van.
        self.lbl_contador = ttk.Label(frame_prog, text="0/3 programadores")
        self.lbl_contador.grid(row=3, column=1, sticky='e')
        
        # Sección donde se ve el resumen del equipo.
        frame_res = ttk.LabelFrame(main_frame, text=" Resumen ", padding=8)
        frame_res.pack(fill='both', expand=True, pady=5)
        
        # Caja de texto para mostrar el resumen. Tiene una barra para mover si es mucho texto.
        self.txt_resultado = tk.Text(frame_res, height=8, font=('Arial', 9), wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(frame_res, orient="vertical", command=self.txt_resultado.yview)
        scrollbar.pack(side="right", fill="y")
        self.txt_resultado.configure(yscrollcommand=scrollbar.set)
        self.txt_resultado.pack(fill='both', expand=True)
        self.txt_resultado.config(state=tk.DISABLED) # No se puede escribir directamente aquí.
        
        # Botón para terminar el registro.
        self.btn_finalizar = ttk.Button(main_frame, text="Finalizar Registro", style='Boton.TButton', command=self.finalizar_registro)
        self.btn_finalizar.pack(pady=5)
    
    def mostrar_mensaje(self, titulo, mensaje):
        # Hace que aparezca una ventanita con un mensaje corto.
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        ventana.resizable(False, False)
        
        tk.Label(ventana, text=mensaje, padx=15, pady=10).pack()
        tk.Button(ventana, text="OK", command=ventana.destroy, width=8).pack(pady=(0, 10))
        
        # Centra esta ventanita también.
        ventana.update_idletasks()
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.root.winfo_screenheight() // 2) - (alto // 2)
        ventana.geometry(f'+{x}+{y}')
        ventana.grab_set() # Bloquea la ventana principal hasta que cierres esta.
    
    def agregar_programador(self):
        # Lo que pasa cuando pulsas "Agregar".
        try:
            if self.equipo is None: # Si es el primer programador, primero creamos el equipo.
                # Coge la info del equipo de las cajas de texto.
                nombre_equipo = self.txt_nombre_equipo.get()
                universidad = self.txt_universidad.get()
                lenguaje = self.txt_lenguaje.get()
                
                # Si falta algún dato del equipo, avisa.
                if not all([nombre_equipo, universidad, lenguaje]):
                    raise Exception("Complete primero los datos del equipo.")
                
                # Crea el equipo con los datos que se pusieron.
                self.equipo = EquipoMaratonProgramacion(nombre_equipo, universidad, lenguaje)
            
            # Coge el nombre y apellidos del programador.
            nombre = self.txt_nombre_programador.get()
            apellidos = self.txt_apellidos_programador.get()
            
            # Revisa que el nombre y apellidos del programador estén bien.
            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(apellidos)
            
            # Añade el programador al equipo.
            self.equipo.agregar_programador(Programador(nombre, apellidos))
            self.programadores_agregados += 1 # Sube el contador.
            self.lbl_contador.config(text=f"{self.programadores_agregados}/3 programadores") # Actualiza el número en la ventana.
            
            # Borra el texto de las cajas para que puedas añadir otro.
            self.txt_nombre_programador.delete(0, tk.END)
            self.txt_apellidos_programador.delete(0, tk.END)
            self.mostrar_informacion() # Actualiza el resumen en la caja de texto.
            
            if self.equipo.esta_lleno(): # Si ya hay 3 programadores.
                # Avisa que el equipo está completo y deshabilita el botón de agregar.
                self.mostrar_mensaje("Equipo completo", "Se alcanzó el máximo de 3 programadores.")
                self.btn_agregar.config(state=tk.DISABLED)
        
        except Exception as e:
            # Si algo sale mal (un campo vacío, un número donde no va), muestra un error.
            self.mostrar_mensaje("Error", str(e))
    
    def mostrar_informacion(self):
        # Actualiza la caja de "Resumen" con la info del equipo y sus programadores.
        if self.equipo:
            info = f"Equipo: {self.equipo.nombre_equipo}\n"
            info += f"Universidad: {self.equipo.universidad}\n"
            info += f"Lenguaje: {self.equipo.lenguaje_programacion}\n\n"
            info += "Programadores:\n"
            
            # Lista los programadores uno por uno.
            for i, prog in enumerate(self.equipo.programadores, 1):
                info += f" {i}. {prog}\n"
            
            self.txt_resultado.config(state=tk.NORMAL) # Habilita para escribir.
            self.txt_resultado.delete(1.0, tk.END) # Borra lo viejo.
            self.txt_resultado.insert(tk.END, info) # Pone lo nuevo.
            self.txt_resultado.config(state=tk.DISABLED) # Vuelve a deshabilitar.
    
    def finalizar_registro(self):
        # Lo que pasa cuando pulsas "Finalizar Registro".
        if not self.equipo:
            # Si no has creado un equipo, te avisa.
            self.mostrar_mensaje("Error", "Primero cree un equipo y agregue programadores.")
            return
        
        if not self.equipo.cumple_minimo_integrantes():
            # Si no hay suficientes programadores, te avisa.
            self.mostrar_mensaje("Error", f"Mínimo {self.equipo.MIN_PROGRAMADORES} programadores requeridos.")
            return
        
        self.mostrar_informacion() # Muestra el resumen final.
        self.mostrar_mensaje("Registro exitoso",
                             f"¡Listo! Equipo '{self.equipo.nombre_equipo}' registrado.\n"
                             f"Con {len(self.equipo.programadores)} programadores.")
        self.root.destroy() # Cierra la ventana de la aplicación.

if __name__ == "__main__":
    # Esto es lo primero que se ejecuta cuando abres el programa.
    root = tk.Tk() # Crea la ventana principal.
    app = AplicacionMaraton(root) # Prepara toda la aplicación dentro de esa ventana.
    root.mainloop() # Hace que la ventana se quede abierta y responda a tus clics.