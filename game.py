import pygame
from map_loader import MapLoader
from file_selector import FileSelector
from agente import Agente

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
            pygame.draw.rect(screen, color, pygame.Rect(
                x * cell_size, y * cell_size, cell_size, cell_size
            ))

def ejecutar_juego(mapa):
    pygame.init()
    cell_size = 30
    num_filas = len(mapa)
    num_columnas = len(mapa[0])
    
    screen = pygame.display.set_mode((num_columnas * cell_size, num_filas * cell_size))
    pygame.display.set_caption("Mapa con Agente")
    
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

        screen.fill((0, 0, 0))  # Fondo negro
        dibujar_mapa(screen, mapa, cell_size)
        agente.dibujar(screen)

        pygame.display.flip()
        clock.tick(10)  # Controlar la velocidad del bucle

    pygame.quit()

if __name__ == "__main__":
    archivo = FileSelector.seleccionar_archivo()
    if archivo:
        delimitador = ',' if archivo.endswith('.csv') else ' '
        mapa = MapLoader.cargar_mapa(archivo, delimitador)
        if mapa:
            ejecutar_juego(mapa)
