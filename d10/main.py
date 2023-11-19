import pygame

# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título e ícono
pygame.display.set_caption("Invasión Espacial", "IE")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

# Variables del jugador
img_jugador = pygame.image.load('cohete.png')
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0


# Función jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Loop del juego
se_ejecuta = True
while se_ejecuta:

    # RGB
    pantalla.fill((205, 144, 228))

    # Iteración de eventos
    for evento in pygame.event.get():

        # Evento cerrar ventana
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento presionar tecla
        if evento.type == pygame.KEYDOWN:

            # Evento presinar tecla fleca izq.
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.1

            # Evento presinar tecla fleca der.
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.1

        # Evento soltar tecla
        if evento.type == pygame.KEYUP:

            # Eventos de presionar flechas izq. y der.
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificar ubicación jugador
    jugador_x += jugador_x_cambio

    # Mantener dentro de bordes
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Llamando a función para posicionar al jugador
    jugador(jugador_x, jugador_y)

    # Actualizar
    pygame.display.update()
