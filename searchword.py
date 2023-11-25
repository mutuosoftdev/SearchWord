import os
import tkinter as tk
from tkinter import filedialog, ttk

def buscar_palabra(directorio, palabra, extension):
    resultados = []
    for raiz, dirs, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.endswith(extension):
                ruta = os.path.join(raiz, archivo)
                with open(ruta, 'r', encoding='utf8', errors='ignore') as f:
                    for num_linea, linea in enumerate(f, 1):
                        if palabra in linea:
                            resultados.append((archivo, ruta, num_linea))
    return resultados

def seleccionar_directorio():
    directorio.set(filedialog.askdirectory())

def iniciar_busqueda():
    tabla.delete(*tabla.get_children())
    resultados = buscar_palabra(directorio.get(), palabra.get(), extension.get())
    for resultado in resultados:
        tabla.insert('', 'end', values=resultado)

root = tk.Tk()
root.geometry("1100x500")

directorio = tk.StringVar()
palabra = tk.StringVar()
extension = tk.StringVar()

tk.Button(root, text="Buscar", command=seleccionar_directorio).pack()
tk.Entry(root, textvariable=palabra).pack()
tk.Label(root, text="Palabra clave:").pack()
opciones = ['html', 'css', 'htm', 'py', 'txt', 'doc']
combobox = ttk.Combobox(root, values=opciones, textvariable=extension).pack()
tk.Button(root, text="START", command=iniciar_busqueda).pack()

frame = tk.Frame(root)
frame.pack()

tabla = ttk.Treeview(frame)
tabla["columns"]=("Nombre del archivo", "Ubicación", "Número de línea")
tabla.column("#0", width=0, stretch=tk.NO)
tabla.column("Nombre del archivo", anchor=tk.W)
tabla.column("Ubicación", anchor=tk.W, width=600)
tabla.column("Número de línea", anchor=tk.W)
tabla.heading("Nombre del archivo", text="Nombre del archivo", anchor=tk.W)
tabla.heading("Ubicación", text="Ubicación", anchor=tk.W)
tabla.heading("Número de línea", text="Número de línea", anchor=tk.W)

scrollbar = ttk.Scrollbar(frame, orient="horizontal", command=tabla.xview)
tabla.configure(xscrollcommand=scrollbar.set)

tabla.pack(side=tk.TOP, fill=tk.BOTH)
scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()

#write by Harold Castro.
#GPL V4