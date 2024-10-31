from heapq import heappop, heappush
from anytree import Node
from constantes import COSTOS_MOVIMIENTO

def heuristica(nodo_actual, nodo_final):
    return abs(nodo_actual[0] - nodo_final[0]) + abs(nodo_actual[1] - nodo_final[1])



def a_estrella_con_arbol(mapa, punto_inicio, punto_fin, agente, game_manager):
    filas = len(mapa)
    columnas = len(mapa[0])
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    open_list = []
    heappush(open_list, (0, punto_inicio))
    closed_list = set()

    g_cost = {punto_inicio: 0}
    padres = {punto_inicio: None}

    nodo_raiz = Node(f"Punto: {punto_inicio}")
    nodos = {punto_inicio: nodo_raiz}

    while open_list:
        _, actual = heappop(open_list)

        if actual == punto_fin:
            camino = []
            while actual is not None:
                camino.append(actual)
                actual = padres[actual]
            return camino[::-1], nodo_raiz

        closed_list.add(actual)

        for movimiento in movimientos:
            vecino = (actual[0] + movimiento[0], actual[1] + movimiento[1])

            if 0 <= vecino[0] < filas and 0 <= vecino[1] < columnas:
                tipo_terreno = mapa[vecino[0]][vecino[1]]
                costo_movimiento = game_manager.obtener_costo_terreno(agente, tipo_terreno)

                if costo_movimiento == float('inf') or vecino in closed_list:
                    continue

                nuevo_g_cost = g_cost[actual] + costo_movimiento

                if vecino not in g_cost or nuevo_g_cost < g_cost[vecino]:
                    g_cost[vecino] = nuevo_g_cost
                    f_cost = nuevo_g_cost + heuristica(vecino, punto_fin)
                    padres[vecino] = actual

                    nodo_actual = nodos[actual]
                    nodo_nuevo = Node(f"Punto: {vecino}, Costo: {nuevo_g_cost}", parent=nodo_actual)
                    nodos[vecino] = nodo_nuevo

                    heappush(open_list, (f_cost, vecino))

    return None, nodo_raiz
