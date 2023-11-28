import pyttsx3
import speech_recognition as sr  # El paquete instalado se llama realmente SpeechRecognition
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser  # No tuvo que instalarse - librería nativa
import datetime
import wikipedia  # No tuvo que instalarse - librería nativa


# Escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():

    # Almacenar recognizer en variable
    r = sr.Recognizer()

    # Configurar el microfono
    with sr.Microphone() as origen:

        # Tiempo de espera
        r.pause_threshold = 0.8

        # Informar que comenzo la grabación
        print('Ya puedes hablar')

        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # Buscar en Google
            pedido = r.recognize_google(audio)

            # Prueba de que pudo ingresar
            print('Dijiste: ' +  pedido)

            # Devolver pedido
            return pedido

        # En Caso de que no comprenda el audio
        except sr.UnknownvalueError:

            # Prueba de que no comprendió el audio
            print("Ups, no entendí.")

            # Devolver error
            return "Sigo esperando"

        # En caso de no resolver el pedido
        except sr.RequestError:

            # Prueba de que no comprendió el audio
            print("Ups, no hay servicio.")

            # Devolver error
            return "Sigo esperando"

        # Error inesperado
        except:

            # Prueba de que no comprendió el audio
            print("Ups, algo ha salido mal.")

            # Devolver error
            return "Sigo esperando"


transformar_audio_en_texto()