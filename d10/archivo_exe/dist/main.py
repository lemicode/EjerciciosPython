import pygame
import random
import math
from pygame import mixer
from d10.convertir_fuente import fuente_bytes


# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título e ícono
pygame.display.set_caption("Invasión Espacial", "IE")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.jpg')

# Agregar música
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Variables del jugador
img_jugador = pygame.image.load('cohete.png')
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0  # Tasa de cambio

# Variables del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(20, 200))
    enemigo_x_cambio.append(0.5)  # Tasa de cambio
    enemigo_y_cambio.append(50)  # Tasa de cambio

# Variables del bala
balas = []
img_bala = pygame.image.load('bala.png')

# Puntaje
puntaje = 0
fuente_como_bytes = fuente_bytes('Asteroid 7337.ttf')
fuente = pygame.font.Font(fuente_como_bytes, 32)
texto_x = 10
texto_y = 10

# Texto final del juego
fuente_final = pygame.font.Font(fuente_como_bytes, 40)


# Función mostrar mensaje final
def texto_final():
    mi_fuente_final = fuente_final.render(f'JUEGO TERMINADO', True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (200, 250))


# Función mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Función jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Función enemigo
def enemigo(x, y, indice):
    pantalla.blit(img_enemigo[indice], (x, y))


# Función disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# Función detectar colisión
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Loop del juego
se_ejecuta = True
while se_ejecuta:

    """# RGB
    pantalla.fill((205, 144, 228))"""

    # Imagen de fondo
    pantalla.blit(fondo, (0, 0))

    # Iteración de eventos
    for evento in pygame.event.get():

        # Evento cerrar ventana
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento presionar tecla
        if evento.type == pygame.KEYDOWN:

            # Evento presinar tecla fleca izq.
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1

            # Evento presinar tecla fleca der.
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1

            # Evento presionar barra espaciadora -> Disparar balas
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -5
                }
                balas.append(nueva_bala)

        # Evento soltar tecla
        if evento.type == pygame.KEYUP:

            # Eventos de presionar flechas izq. y der.
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificar ubicación jugador
    jugador_x += jugador_x_cambio

    # Mantener dentro de bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Modificar ubicación del enemigo
    for e in range(cantidad_enemigos):

        # Fin del juego
        if enemigo_y[e] > 500:
            balas.clear()
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        # Posicionar al enemigo
        enemigo_x[e] += enemigo_x_cambio[e]

        # Mantener dentro de bordes al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.5
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.5
            enemigo_y[e] += enemigo_y_cambio[e]

        # Colisión
        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala['x'], bala['y'])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound('Golpe.mp3')
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)
                break

        # Llamando a función para posicionar al enemigo
        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiento bala
    for bala in balas:
        bala['y'] += bala['velocidad']
        pantalla.blit(img_bala, (bala['x'] + 16, bala['y'] + 10))
        if bala['y'] < 0:
            balas.remove(bala)

    # Llamando a función para posicionar al jugador
    jugador(jugador_x, jugador_y)

    # Mostrar puntaje
    mostrar_puntaje(texto_x, texto_y)

    # Actualizar
    pygame.display.update()
