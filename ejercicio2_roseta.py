# Ejercicio 2 - Rosetas geometricas con Bresenham
# Taller de Programacion de 5.a Generacion I - Unidad III
from PIL import Image
import math
import colorsys


def bresenham(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Traza una linea con decisiones basadas en errores enteros."""
    dx, dy = abs(x1 - x0), abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x, y = x0, y0
    while True:
        if 0 <= x < ancho and 0 <= y < alto:
            pixels[x, y] = color
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy


def generar_puntos_circulo(cx, cy, radio, n):
    """Distribuye n puntos a igual distancia angular sin dibujar el circulo."""
    puntos = []
    for i in range(n):
        angulo = 2 * math.pi * i / n
        x = cx + int(radio * math.cos(angulo))
        y = cy + int(radio * math.sin(angulo))
        puntos.append((x, y))
    return puntos


def dibujar_roseta(pixels, puntos, ancho, alto):
    """Conecta cada par de puntos una sola vez y cambia el color por angulo."""
    n = len(puntos)
    for i in range(n):
        for j in range(i + 1, n):
            # El angulo del punto medio determina el tono del gradiente.
            mx = (puntos[i][0] + puntos[j][0]) / 2
            my = (puntos[i][1] + puntos[j][1]) / 2
            angulo = math.atan2(my - alto / 2, mx - ancho / 2)
            tono = (angulo + math.pi) / (2 * math.pi)
            r, g, b = colorsys.hsv_to_rgb(tono, 0.78, 0.85)
            color = (round(r * 255), round(g * 255), round(b * 255))
            bresenham(pixels, *puntos[i], *puntos[j], color, ancho, alto)


def main():
    ancho = alto = 700
    for n in (12, 24, 36):
        img = Image.new('RGB', (ancho, alto), 'white')
        pixels = img.load()
        puntos = generar_puntos_circulo(350, 350, 300, n)
        dibujar_roseta(pixels, puntos, ancho, alto)
        nombre = f'roseta_{n}.png'
        img.save(nombre)
        print(f'Imagen creada: {nombre} ({n * (n - 1) // 2} lineas)')


if __name__ == '__main__':
    main()
