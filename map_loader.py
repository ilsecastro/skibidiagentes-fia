import csv
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Función para cargar el archivo de mapa
def cargar_mapa(archivo, delimitador):
    mapa = []
    
    try:
        with open(archivo, newline='') as archivo_texto:
            lector = csv.reader(archivo_texto, delimiter=delimitador)
            for fila in lector:
                try:
                    mapa.append([int(celda) for celda in fila])
                except ValueError:
                    messagebox.showerror("Error", f"No se pudo convertir una celda a entero en {fila}")
                    return None
    except FileNotFoundError:
        messagebox.showerror("Error", f"El archivo {archivo} no se encontró.")
        return None
    except Exception as e:
        messagebox.showerror("Error", f"Error al leer el archivo: {e}")
        return None
    return mapa
    
   

# Función para abrir el cuadro de diálogo y cargar el archivo
def seleccionar_archivo():
    archivo = filedialog.askopenfilename(
        title="Selecciona archivo",
        filetypes=[("Archivos de texto", "*.txt"), ("Archivos CSV", "*.csv")]
    )

    if archivo:
        # Determinar el delimitador basado en la extensión del archivo
        extension = os.path.splitext(archivo)[1]
        delimitador = ',' if extension == '.csv' else ' '
        
        # Cargar el archivo seleccionado
        mapa = cargar_mapa(archivo, delimitador=delimitador)
        if mapa:
            ventana_mapa(mapa)

def ventana_mapa(mapa):
    # Crear una nueva ventana para mostrar el mapa
    ventana_mapa = tk.Toplevel()
    ventana_mapa.title("Mapa Cargado")
    
    #Editar la matriz
    cell_size=30
    num_filas = len(mapa)
    num_columnas = len(mapa[0]) if num_filas > 0 else 0

    #ajustar la ventana y la matriz
    ventana_mapa.geometry(f"{(num_columnas + 1) * cell_size + 100}x{(num_filas + 1) * cell_size + 100}")
    
    # Configurar columnas y filas adicionales para centrar el contenido
    #ventana_mapa.grid_columnconfigure(0, weight=0)  
    #ventana_mapa.grid_columnconfigure(num_columnas + 1, weight=0) 
    #ventana_mapa.grid_rowconfigure(0, weight=0)  
    #ventana_mapa.grid_rowconfigure(num_filas + 1, weight=0)  

    #Contenido ajustado 
    for i in range(1, num_filas + 1):
        ventana_mapa.grid_rowconfigure(i, weight=1)
    for j in range(1, num_columnas + 1):
        ventana_mapa.grid_columnconfigure(j, weight=1)
   
    #Fila superior (letas)
    letras =[chr(i) for i in range(65, 65 + num_columnas)]
    for j, letra in enumerate(letras):
        label = tk.Label(ventana_mapa, text=letra, width=cell_size//17, height=cell_size//17,
                             font=("Arial", 12), relief="solid", borderwidth=1)
        label.grid(row=0, column=j + 1, sticky="nsew")
        
    #columna izquierda (numeros)
    for i in range(num_filas):
        label = tk.Label(ventana_mapa, text=str(i +1), width=cell_size//15, height=cell_size//15,
                             font=("Arial", 12), relief="solid", borderwidth=1)
        label.grid(row=i+1, column=0, sticky="nsew")

    

    #contenido de la matriz
    for i, fila in enumerate(mapa):
        for j, celda in enumerate(fila):
            if celda == 0:
                color ="gray"
            elif celda ==1:
                color ="white"
            elif celda == 2:
                color="blue"
            elif celda == 3:
                color="yellow"  
            elif celda == 4:
                color="green"  
            else:
                color="black"            

            label = tk.Label(ventana_mapa, text="",bg= color, width=cell_size//2, height=cell_size//2, 
                             font=("Arial", 12), relief="solid", borderwidth=1)
            label.grid(row=i + 1, column=j + 1, sticky="nsew")
        
       

#Ventana principal 
def crear_ventana():
    window = tk.Tk()
    window.title("Cargar Mapa")
    window.geometry("350x350")
    window.configure(background="#333333")

    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)

    label = tk.Label(window, text="Selecciona archivo", bg="#333333", fg="#5659C3", font=("Arial", 15))
    label.grid(row=0, column=0, columnspan=2, sticky="nsew")

    # Crear botón para cargar el archivo
    button_cargar = tk.Button(
        window, text="Cargar archivo", command=seleccionar_archivo,
        font=("Arial", 10), bg="#5659C3", fg="#FFFFFF", pady=10, padx=10
    )
    button_cargar.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

    # Iniciar el loop de la interfaz gráfica
    window.mainloop()

if __name__ == "__main__":
    crear_ventana()
