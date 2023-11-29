import pyttsx3
import speech_recognition as sr  # El paquete instalado se llama realmente SpeechRecognition
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser  # No tuvo que instalarse - librería nativa
import datetime
import wikipedia  # No tuvo que instalarse - librería nativa


"""
# Validar voces existentes
engine = pyttsx3.init()
for voz in engine.getProperty('voices')
    print(voz)
"""

# Opciones de voz / idioma
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id4 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'


# Escuchar micrófono y devolver el audio como texto
def trasformar_audio_en_texto():
    # Almacenar recognizer en variable
    r = sr.Recognizer()

    # Configurar el micrófono
    with sr.Microphone() as origen:

        # Tiempo de espera
        r.pause_threshold = 0.8

        # Informar que comenzó la grabación
        print("ya puedes hablar")

        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # Buscar en Google
            pedido = r.recognize_google(audio, language="es-ar")

            # Prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # Devolver pedido
            return pedido

        # En caso de que no comprenda el audio
        except sr.UnknownValueError:

            # Prueba de que no comprendió el audio
            print("ups, no entendi")

            # Devolver error
            return "sigo esperando"

        # En caso de no resolver el pedido
        except sr.RequestError:

            # Prueba de que no comprendió el audio
            print("ups, no hay servicio")

            # Devolver error
            return "sigo esperando"

        # Error inesperado
        except:

            # Prueba de que no comprendió el audio
            print("ups, algo ha salido mal")

            # Devolver error
            return "sigo esperando"


# Función para que el asistente pueda ser escuchado
def hablar(mensaje):
    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id3)

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# Informar el día de la semana
def pedir_dia():
    # Crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # Crear variable para el día de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # Diccionario con nombres de días
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    # Decir el día de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


# Informar qué hora es
def pedir_hora():
    # Crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    # Decir la hora
    hablar(hora)


# Función saludo inicial
def saludo_inicial():
    # Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    # Decir el saludo
    hablar(f'{momento}, soy Helena, tu asistente personal. Por favor, dime en qué te puedo ayudar')


# Función central del asistente
def pedir_cosas():
    # Activar saludo inicial
    saludo_inicial()

    # Variable de corte
    comenzar = True

    # Loop central
    while comenzar:

        # Activar el micro y guardar el pedido en un string
        pedido = trasformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon': 'AMZN',
                       'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("Perdón pero no la he encontrado")
                continue
        elif 'adiós' in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break


pedir_cosas()
