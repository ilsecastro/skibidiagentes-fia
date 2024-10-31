from collections import deque
from anytree import Node
import pygame

def bfs_decision_por_decision_con_arbol(mapa, punto_inicio, punto_fin, game_manager):
    filas = len(mapa)
    columnas = len(mapa[0])
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cola = deque([punto_inicio])
    visitado = set([punto_inicio])
    padre = {punto_inicio: None}

    # Crear el árbol de decisiones
    nodo_raiz = Node(f"Punto: {punto_inicio}")
    nodos = {punto_inicio: nodo_raiz}

    while cola:
        actual = cola.popleft()

        # Contar las opciones disponibles para tomar una decisión
        opciones_disponibles = 0
        for movimiento in movimientos:
            nuevo_x = actual[0] + movimiento[0]
            nuevo_y = actual[1] + movimiento[1]

            if 0 <= nuevo_x < filas and 0 <= nuevo_y < columnas:
                if mapa[nuevo_x][nuevo_y] != 1 and (nuevo_x, nuevo_y) not in visitado:
                    opciones_disponibles += 1

        # Si hay más de una opción, es un nodo de decisión
        if opciones_disponibles > 1 or actual == punto_inicio:
            game_manager.dibujar_mapa()
            game_manager.agente.dibujar(game_manager.screen)
            pygame.display.flip()
            pygame.time.delay(500)  # Pausa para visualizar la decisión

        if actual == punto_fin:
            camino = []
            while actual is not None:
                camino.append(actual)
                actual = padre[actual]
            return camino[::-1], nodo_raiz  # Retorna el camino y el árbol

        # Explorar los vecinos
        for movimiento in movimientos:
            nuevo_x = actual[0] + movimiento[0]
            nuevo_y = actual[1] + movimiento[1]

            if 0 <= nuevo_x < filas and 0 <= nuevo_y < columnas:
                if mapa[nuevo_x][nuevo_y] != 1 and (nuevo_x, nuevo_y) not in visitado:
                    cola.append((nuevo_x, nuevo_y))
                    visitado.add((nuevo_x, nuevo_y))
                    padre[(nuevo_x, nuevo_y)] = actual

                    # Agregar nodo al árbol
                    nodo_actual = nodos[actual]
                    nodo_nuevo = Node(f"Punto: {(nuevo_x, nuevo_y)}", parent=nodo_actual)
                    nodos[(nuevo_x, nuevo_y)] = nodo_nuevo

    return None, nodo_raiz  # Si no hay solución, retorna el árbol generado




def bfs_paso_a_paso_con_arbol(mapa, punto_inicio, punto_fin, game_manager):
    filas = len(mapa)
    columnas = len(mapa[0])
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cola = deque([punto_inicio])
    visitado = set([punto_inicio])
    padre = {punto_inicio: None}

    # Crear el árbol de decisiones
    nodo_raiz = Node(f"Punto: {punto_inicio}")
    nodos = {punto_inicio: nodo_raiz}
    print(f"Árbol inicial: {nodo_raiz}")  # Verificación inicial del árbol

    while cola:
        actual = cola.popleft()

        # Mostrar el mapa en cada paso
        game_manager.dibujar_mapa()
        game_manager.agente.dibujar(game_manager.screen)
        pygame.display.flip()
        pygame.time.delay(500)

        if actual == punto_fin:
            camino = []
            while actual is not None:
                camino.append(actual)
                actual = padre[actual]
            print(f"Camino encontrado: {camino}")
            return camino[::-1], nodo_raiz  # Retorna el camino y el árbol

        for movimiento in movimientos:
            nuevo_x = actual[0] + movimiento[0]
            nuevo_y = actual[1] + movimiento[1]

            if 0 <= nuevo_x < filas and 0 <= nuevo_y < columnas:
                if mapa[nuevo_x][nuevo_y] != 1 and (nuevo_x, nuevo_y) not in visitado:
                    cola.append((nuevo_x, nuevo_y))
                    visitado.add((nuevo_x, nuevo_y))
                    padre[(nuevo_x, nuevo_y)] = actual

                    # Crear nodo en el árbol
                    nodo_actual = nodos[actual]
                    nodo_nuevo = Node(f"Punto: {(nuevo_x, nuevo_y)}", parent=nodo_actual)
                    nodos[(nuevo_x, nuevo_y)] = nodo_nuevo
                    print(f"Nuevo nodo añadido: {nodo_nuevo}")  # Verificar cada nodo añadido

    return None, nodo_raiz  # Si no hay solución
