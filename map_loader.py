import pygame
import csv
from tkinter import filedialog, Tk

# Función para cargar el archivo de mapa
def cargar_mapa(archivo, delimitador):
    mapa = []
    try:
        with open(archivo, newline='') as archivo_texto:
            lector = csv.reader(archivo_texto, delimiter=delimitador)
            for fila in lector:
                mapa.append([int(celda) for celda in fila])
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None
    return mapa

# Función para abrir el cuadro de diálogo y cargar el archivo
def seleccionar_archivo():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter
    archivo = filedialog.askopenfilename(
        title="Selecciona archivo",
        filetypes=[("Archivos de texto", "*.txt"), ("Archivos CSV", "*.csv")]
    )
    root.destroy()  # Destruye la ventana después de seleccionar el archivo
    return archivo

# Función para dibujar el mapa en la ventana de Pygame
def dibujar_mapa(screen, mapa, cell_size):
    colores = {
        0: (128, 128, 128),  # Gris
        1: (255, 255, 255),  # Blanco
        2: (0, 0, 255),      # Azul
        3: (255, 255, 0),    # Amarillo
        4: (0, 255, 0),      # Verde
    }
    for y, fila in enumerate(mapa):
        for x, celda in enumerate(fila):
            color = colores.get(celda, (0, 0, 0))  # Color negro por defecto
            pygame.draw.rect(screen, color, pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))

# Clase para manejar al agente
class Agente:
    def __init__(self, pos_x, pos_y, cell_size, mapa):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.cell_size = cell_size
        self.mapa = mapa

    def mover(self, dx, dy):
        nueva_x = self.pos_x + dx
        nueva_y = self.pos_y + dy

        # Verificar que el agente no se salga de los límites
        if 0 <= nueva_x < len(self.mapa[0]) and 0 <= nueva_y < len(self.mapa):
            self.pos_x = nueva_x
            self.pos_y = nueva_y

    def dibujar(self, screen):
        # Dibujar al agente como un rectángulo rojo
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.pos_x * self.cell_size, self.pos_y * self.cell_size, self.cell_size, self.cell_size))

# Función principal que ejecuta el bucle del juego
def ejecutar_juego(mapa):
    pygame.init()
    
    # Tamaño de la celda
    cell_size = 30
    num_filas = len(mapa)
    num_columnas = len(mapa[0])
    
    # Crear la ventana de Pygame
    screen = pygame.display.set_mode((num_columnas * cell_size, num_filas * cell_size))
    pygame.display.set_caption("Mapa con Agente")

    # Crear al agente en la posición inicial (0, 0)
    agente = Agente(0, 0, cell_size, mapa)

    clock = pygame.time.Clock()
    corriendo = True

    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    agente.mover(0, -1)
                elif event.key == pygame.K_DOWN:
                    agente.mover(0, 1)
                elif event.key == pygame.K_LEFT:
                    agente.mover(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    agente.mover(1, 0)

        # Dibujar mapa y agente
        screen.fill((0, 0, 0))  # Fondo negro
        dibujar_mapa(screen, mapa, cell_size)
        agente.dibujar(screen)

        pygame.display.flip()
        clock.tick(10)  # Controlar la velocidad del bucle

    pygame.quit()

if __name__ == "__main__":
    archivo = seleccionar_archivo()
    if archivo:
        delimitador = ',' if archivo.endswith('.csv') else ' '
        mapa = cargar_mapa(archivo, delimitador)
        if mapa:
            ejecutar_juego(mapa)
