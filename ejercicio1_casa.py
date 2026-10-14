# Ejercicio 1 - Casa con el algoritmo DDA
# Taller de Programacion de 5.a Generacion I - Unidad III
from PIL import Image
import math


def dda(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Traza una linea usando incrementos y redondeo (DDA)."""
    dx = x1 - x0
    dy = y1 - y0
    pasos = max(abs(dx), abs(dy))
    if pasos == 0:
        if 0 <= x0 < ancho and 0 <= y0 < alto:
            pixels[x0, y0] = color
        return
    incremento_x = dx / pasos
    incremento_y = dy / pasos
    x, y = float(x0), float(y0)
    for _ in range(pasos + 1):
        px, py = round(x), round(y)
        if 0 <= px < ancho and 0 <= py < alto:
            pixels[px, py] = color
        x += incremento_x
        y += incremento_y


def dibujar_rectangulo(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Construye un rectangulo con cuatro lineas DDA."""
    dda(pixels, x0, y0, x1, y0, color, ancho, alto)
    dda(pixels, x1, y0, x1, y1, color, ancho, alto)
    dda(pixels, x1, y1, x0, y1, color, ancho, alto)
    dda(pixels, x0, y1, x0, y0, color, ancho, alto)


def dibujar_triangulo(pixels, p1, p2, p3, color, ancho, alto):
    """Une los tres vertices del techo con DDA."""
    dda(pixels, *p1, *p2, color, ancho, alto)
    dda(pixels, *p2, *p3, color, ancho, alto)
    dda(pixels, *p3, *p1, color, ancho, alto)


def dibujar_puerta(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Dibuja la puerta y su picaporte."""
    dibujar_rectangulo(pixels, x0, y0, x1, y1, color, ancho, alto)
    dda(pixels, x1 - 10, (y0 + y1) // 2, x1 - 8, (y0 + y1) // 2, color, ancho, alto)


def dibujar_ventana(pixels, x0, y0, tam, color, ancho, alto):
    """Dibuja una ventana cuadrada con divisiones interiores."""
    dibujar_rectangulo(pixels, x0, y0, x0 + tam, y0 + tam, color, ancho, alto)
    dda(pixels, x0 + tam // 2, y0, x0 + tam // 2, y0 + tam, color, ancho, alto)
    dda(pixels, x0, y0 + tam // 2, x0 + tam, y0 + tam // 2, color, ancho, alto)


def dibujar_sol(pixels, cx, cy, radio, n_rayos, color, ancho, alto):
    """Dibuja rayos radiales alrededor del centro del sol."""
    for i in range(n_rayos):
        angulo = 2 * math.pi * i / n_rayos
        x0 = cx + round((radio // 3) * math.cos(angulo))
        y0 = cy + round((radio // 3) * math.sin(angulo))
        x1 = cx + round(radio * math.cos(angulo))
        y1 = cy + round(radio * math.sin(angulo))
        dda(pixels, x0, y0, x1, y1, color, ancho, alto)


def dibujar_arbol(pixels, x, suelo, color_tronco, color_copa, ancho, alto):
    """Extension voluntaria: arbol con tronco y copa triangular."""
    dibujar_rectangulo(pixels, x - 9, suelo - 55, x + 9, suelo, color_tronco, ancho, alto)
    dibujar_triangulo(pixels, (x - 38, suelo - 45), (x, suelo - 150),
                      (x + 38, suelo - 45), color_copa, ancho, alto)


def main():
    ancho, alto = 600, 500
    imagen = Image.new('RGB', (ancho, alto), (225, 241, 255))
    pixels = imagen.load()

    # Piso, cuerpo, techo, puerta y dos ventanas.
    dda(pixels, 0, 425, ancho - 1, 425, (55, 140, 70), ancho, alto)
    dibujar_rectangulo(pixels, 155, 210, 445, 425, (30, 90, 165), ancho, alto)
    dibujar_triangulo(pixels, (130, 210), (300, 92), (470, 210),
                      (185, 67, 58), ancho, alto)
    dibujar_puerta(pixels, 270, 323, 330, 425, (115, 70, 42), ancho, alto)
    dibujar_ventana(pixels, 190, 260, 58, (22, 125, 160), ancho, alto)
    dibujar_ventana(pixels, 352, 260, 58, (22, 125, 160), ancho, alto)

    # Sol de doce rayos y arbol decorativo (extension opcional).
    dibujar_sol(pixels, 75, 80, 48, 12, (235, 151, 0), ancho, alto)
    dibujar_arbol(pixels, 525, 425, (115, 75, 45), (35, 130, 65), ancho, alto)
    imagen.save('casa.png')
    print('Imagen creada: casa.png')


if __name__ == '__main__':
    main()
