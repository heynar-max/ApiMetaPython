from flora import apiflora
from regiones import apiregiones


def generar_respuesta(texto, number):
    
    if "boton" in texto:
        return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": "Hola 👋 te damos la bienvenida. ¿Te gustaría conocer sobre las regiones de Colombia?"
                },
                "footer": {
                    "text": "Selecciona una de las opciones"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "btnsi",
                                "title": "Si"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "btnno",
                                "title": "No"
                            }
                        }
                    ]
                }
            }
        }
    elif "btnsi" in texto:
        # Llamar a la función ApiRegiones o devolver el mensaje correspondiente
        return {
            apiregiones(texto, number)
        }
    elif "btnno" in texto:
        # Llamar a la función ApiFlora o devolver el mensaje correspondiente
        return {
            apiflora(texto, number)
        }