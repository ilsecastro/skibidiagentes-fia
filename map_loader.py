import csv

class MapLoader:
    @staticmethod
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