import tkinter as tk
import Busqueda

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Buscar Archivo")
        self.master.geometry("700x400")
        
        # Texto principal
        self.texto_principal = tk.Label(self.master, text="¿Qué archivo desea buscar?")
        self.texto_principal.config(font=("Arial", 20))
        self.texto_principal.pack(pady=20)
        
        # Listado de opciones
        self.nombre_archivo_label = tk.Label(self.master, text="Nombre del archivo (*)")
        self.nombre_archivo_label.pack()
        self.nombre_archivo_entry = tk.Entry(self.master)
        self.nombre_archivo_entry.pack()

        self.directorio_label = tk.Label(self.master, text="Directorio por el cual buscar (*)")
        self.directorio_label.pack()
        self.directorio_entry = tk.Entry(self.master)
        self.directorio_entry.pack()

        self.subdirectorios_label = tk.Label(self.master, text="Subdirectorios")
        self.subdirectorios_label.pack()
        self.subdirectorios_entry = tk.Entry(self.master)
        self.subdirectorios_entry.pack()

        self.extension_label = tk.Label(self.master, text="Extension")
        self.extension_label.pack()
        self.extension_entry = tk.Entry(self.master)
        self.extension_entry.pack()

        # Botones
        self.confirmar_button = tk.Button(self.master, text="Confirmar", command=self.confirmar)
        self.confirmar_button.pack(side=tk.RIGHT, padx=10, pady=20)

        self.buscar_texto_button = tk.Button(self.master, text="¿Desea buscar un texto en especifico?", command=self.abrir_ventana_texto)
        self.buscar_texto_button.pack(pady=20)

    def confirmar(self):
        nombre_archivo = self.nombre_archivo_entry.get()
        directorio = self.directorio_entry.get()
        subdirectorios = self.subdirectorios_entry.get()
        extension = self.extension_entry.get()

        path=Busqueda.search_file_in_dir(nombre_archivo,directorio,subdirectorios,extension)
        self.ventana_encontrar_file=tk.Tk()
        mostrar=tk.Label(self.ventana_encontrar_file,text=f"File encontrado en: {path}")
        mostrar.grid(row=3, column=0, padx=10, pady=10)

    def abrir_ventana_texto(self):
        self.master.withdraw()  # Ocultar la ventana principal
        self.buscar_texto_especifico()

    def buscar_texto_especifico(self):
        # Cerrar la ventana actual
        self.master.destroy()

        # Crear una nueva ventana para la búsqueda de texto específico
        ventana_busqueda_texto = tk.Tk()
        ventana_busqueda_texto.title("Buscar Texto Específico")

        # Crear los widgets de la nueva ventana
        directorio_label = tk.Label(ventana_busqueda_texto, text="Directorio:")
        directorio_label.grid(row=0, column=0, padx=10, pady=10)
        self.directorio_entry = tk.Entry(ventana_busqueda_texto, width=50)
        self.directorio_entry.grid(row=0, column=1, padx=10, pady=10)

        texto_label = tk.Label(ventana_busqueda_texto, text="Texto:")
        texto_label.grid(row=1, column=0, padx=10, pady=10)
        self.texto_entry1 = tk.Entry(ventana_busqueda_texto, width=50)
        self.texto_entry1.grid(row=1, column=1, padx=10, pady=10)

        subdirectorio_label = tk.Label(ventana_busqueda_texto, text="Subdirectorio:")
        subdirectorio_label.grid(row=2, column=0, padx=10, pady=10)
        self.subdirectorio_entry1 = tk.Entry(ventana_busqueda_texto, width=50)
        self.subdirectorio_entry1.grid(row=2, column=1, padx=10, pady=10)

        autor_label = tk.Label(ventana_busqueda_texto, text="Autor:")
        autor_label.grid(row=3, column=0, padx=10, pady=10)
        self.autor_entry1 = tk.Entry(ventana_busqueda_texto, width=50)
        self.autor_entry1.grid(row=3, column=1, padx=10, pady=10)

        fecha_label = tk.Label(ventana_busqueda_texto, text="Fecha Aproximada:")
        fecha_label.grid(row=4, column=0, padx=10, pady=10)
        self.fecha_entry12 = tk.Entry(ventana_busqueda_texto, width=25)
        self.fecha_entry12.grid(row=4, column=1, padx=10, pady=10)

        self.fecha_entry21 = tk.Entry(ventana_busqueda_texto, width=25)
        self.fecha_entry21.grid(row=4, column=2, padx=10, pady=10)

        #Crear Boton Confirmar

        boton_confirmar = tk.Button(ventana_busqueda_texto, text="Confirmar", command=lambda: self.confirmar_buscar_texto())
        boton_confirmar.grid(row=5, column=0, columnspan=2, pady=10)
    
    def confirmar_buscar_texto(self):
        Texto = self.texto_entry1.get()
        Directorio = self.directorio_entry.get()
        Subdirectorio = self.subdirectorio_entry1.get()
        Autor = self.autor_entry1.get()
        fecha_Inicio = self.fecha_entry12.get()
        Fecha_Fin = self.fecha_entry21.get()

        path=Busqueda.search_text_in_dir(Directorio,Texto,Subdirectorio,Autor,fecha_Inicio,Fecha_Fin)
        self.ventana_encontrar=tk.Tk()
        mostrar=tk.Label(self.ventana_encontrar,text=f"Texto encontrado en: {path}")
        mostrar.grid(row=3, column=0, padx=10, pady=10)
# Instanciar Ventanas
root = tk.Tk()
Ventana = VentanaPrincipal(root)
root.mainloop()