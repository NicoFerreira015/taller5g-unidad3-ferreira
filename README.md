# Taller de Programación de 5.ª Generación I — Unidad III

**Alumno:** César Ferreira (completar nombre completo si corresponde)  
**Universidad:** Universidad Americana  
**Tema:** Conversión por rastreo — DDA y Bresenham

## Contenido

- `ejercicio1_casa.py`: dibuja una casa con el algoritmo DDA en un lienzo de 600 × 500.
- `ejercicio2_roseta.py`: genera rosetas con Bresenham usando 12, 24 y 36 puntos sobre una circunferencia imaginaria.
- `casa.png`, `roseta_12.png`, `roseta_24.png`, `roseta_36.png`: resultados generados.

## Ejecución

Se necesita Python 3 y la biblioteca Pillow:

```bash
python -m pip install Pillow
python ejercicio1_casa.py
python ejercicio2_roseta.py
```

Los archivos PNG se guardan en la carpeta desde la cual se ejecuten los programas.

## Cómo funcionan

DDA divide el desplazamiento de una línea en pequeños pasos, calcula las posiciones intermedias y pinta los píxeles más cercanos. Bresenham elige los siguientes píxeles a partir de un error acumulado, usando operaciones enteras para trazar líneas.

La casa está formada por líneas DDA y contiene los elementos solicitados, más un árbol opcional. En las rosetas se conectan todos los pares de puntos, con un gradiente que depende del ángulo del punto medio de cada línea.

**Nota:** la función DDA fue reconstruida a partir de la firma y los requisitos del enunciado, ya que no se disponía del archivo original de clase. Conviene contrastarla con la versión del docente si se consigue.
