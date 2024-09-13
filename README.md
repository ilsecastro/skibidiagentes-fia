
# Proyecto: Entorno de Exploración Manual

## Descripción del Proyecto

Este proyecto tiene como objetivo inicial desarrollar un entorno en el que se pueda cargar y visualizar mapas como laberintos o tableros definidos por una cuadrícula. En esta primera etapa, el enfoque estará en la creación del entorno gráfico, la carga de mapas y la interacción manual con dicho entorno.

No se implementarán agentes inteligentes en esta fase, sino que permitiremos la manipulación y exploración del entorno de forma manual mediante controles de usuario. El usuario podrá modificar el mapa y realizar consultas sobre las celdas.

## Funcionalidades para esta Entrega

### 1. Cargar Mapas desde Archivos
- El sistema permitirá cargar un archivo de texto (ej. `mapa.txt`) que contenga un mapa codificado en forma de matriz.
- Cada tipo de terreno estará representado por un valor codificado (ejemplo: 0 para muros, 1 para caminos) y se podrá visualizar de manera gráfica utilizando colores.
- El mapa cargado se mostrará en una interfaz gráfica simple utilizando **Pygame**.

### 2. Consultar el Valor de una Celda
- El usuario podrá seleccionar una celda específica en la cuadrícula (mediante coordenadas) y el sistema le indicará el tipo de terreno que representa esa celda (ej. muro, camino, etc.).

### 3. Modificar el Valor de una Celda
- Se habilitará la posibilidad de cambiar el tipo de terreno de una celda específica. Por ejemplo, se podrá cambiar una celda de muro (0) a camino (1) y viceversa.
- Esto permitirá modificar el entorno de forma interactiva.

### 4. Marcar Posiciones
- El sistema permitirá marcar diferentes posiciones en el mapa, como:
  - Punto de inicio (I)
  - Posición actual (X)
  - Posiciones ya visitadas (V)
  - Lugares donde se han tomado decisiones (O)
- Estas marcas serán visibles en la visualización del mapa.

### 5. Interacción Manual
- El usuario controlará manualmente un objeto dentro del mapa usando el teclado. Este objeto se moverá de celda en celda dentro de los caminos disponibles.
- El movimiento estará restringido a las celdas que representan caminos (valor 1) y no podrá cruzar muros (valor 0).

## Estructura del Proyecto

### Archivos Principales
- En construcción
  
## Tecnologías y Herramientas

- **Python 3.x**
- **Pygame**: Utilizado para la visualización del mapa y la interacción con el usuario.

## Instalación y Ejecución

### Requisitos

- Python 3.x
- Pygame

### Instalación de Pygame

```bash
pip install pygame
```

### Cómo ejecutar el proyecto

1. Clona este repositorio:

```bash
git clone https://github.com/luisferdev11/skibidiagentes-fia.git
cd exploracion-entorno-manual
```

2. Todavía no hay nada :v

## Contribuciones

Si deseas contribuir al proyecto, por favor sigue los siguientes pasos:

1. Haz un fork de este repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un pull request para revisión.
