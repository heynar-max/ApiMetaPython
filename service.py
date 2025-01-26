import json
import http.client
from model import Log
from db import db
from flask import request, jsonify
from app import mensajes_log

TOKEN_HESODOKS = "HESODOKS"

def agregar_mensajes_log(texto):
    mensajes_log.append(texto)
    texto_json = json.dumps(texto, ensure_ascii=False)
    nuevo_registro = Log(texto=texto_json)
    db.session.add(nuevo_registro)
    db.session.commit()

def verificar_token(req):
    token = req.args.get('hub.verify_token')
    challenge = req.args.get('hub.challenge')

    if challenge and token == TOKEN_HESODOKS:
        return challenge
    else:
        return jsonify({'error': 'Token Inválido'}), 401

def recibir_mensajes(req):
    try:
        req = request.get_json()
        entry = req['entry'][0]
        changes = entry['changes'][0]
        value = changes['value']
        objeto_mensaje = value.get('messages')

        if objeto_mensaje:
            messages = objeto_mensaje[0]

            if "type" in messages:
                tipo = messages["type"]
                agregar_mensajes_log(messages)

                if tipo == "interactive":
                    handle_interactive(messages)

                elif "text" in messages:
                    handle_text(messages)

        return jsonify({'message': 'EVENT_RECEIVED'})
    except Exception as e:
        agregar_mensajes_log(str(e))
        return jsonify({'message': 'EVENT_RECEIVED'})

def handle_interactive(messages):
    tipo_interactivo = messages["interactive"]["type"]
    numero = messages["from"]

    if tipo_interactivo == "button_reply":
        text = messages["interactive"]["button_reply"]["id"]
        enviar_mensajes_whatsapp(text, numero)
    elif tipo_interactivo == "list_reply":
        text = messages["interactive"]["list_reply"]["id"]
        enviar_mensajes_whatsapp(text, numero)

def handle_text(messages):
    text = messages["text"]["body"]
    numero = messages["from"]
    enviar_mensajes_whatsapp(text, numero)

def enviar_mensajes_whatsapp(texto, number):
    data = generar_respuesta(texto.lower(), number)
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer EAAImrVwLfJkBOzGWAFeukQaohFT3Pccy6c9uNtkWJebyRY0OZACyr9xqUZAx6wZCiCV9YLk5cpateXpJdzFz3AeYN146ONW2flirF6mybyuZC26bpdZA8sZCPCEPz6iXQJeqgRdnbZC2ns0TRufGfiRTxAZAlc0MTyVscwdZCdjK6wrNarcdH2kDYRlklC36hbiJIngZDZD"
    }
    connection = http.client.HTTPSConnection("graph.facebook.com")

    try:
        connection.request("POST", "/v21.0/591402320714042/messages", json.dumps(data), headers)
        response = connection.getresponse()
        print(response.status, response.reason)
    except Exception as e:
        agregar_mensajes_log(str(e))
    finally:
        connection.close()

def generar_respuesta(texto, number):
    
    texto = texto.lower()

    if "hola" in texto:
        return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "🚀 Hola, ¿Cómo estás? Bienvenido."
            }
        }
    elif "1" in texto:
        return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            }
        }
    elif "2" in texto:
        return {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "location",
            "location": {
                "latitude": "3.429954100205143",
                "longitude": "-76.54103829003456",
                "name": "Pascual Guerrero",
                "address": "san fernado cali"
            }
        }
    elif "3" in texto:
        return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "document",
            "document": {
                    "link": "https://www.turnerlibros.com/wp-content/uploads/2021/02/ejemplo.pdf",
                    "caption": "Temario del Curso #001"
                }
            }
    elif "4" in texto:
        return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "audio",
            "audio": {
                "link": "https://filesamples.com/samples/audio/mp3/sample1.mp3"
            }
        }
    elif "5" in texto:
        return {
            "messaging_product": "whatsapp",
            "to": number,
            "text": {
                "preview_url": True,
                "body": "Introduccion  https://www.youtube.com/watch?v=7M56JNzPH54&t=131s&ab_channel=HeynarSotoHolguin"
            }
        }
    elif "6" in texto:
        return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "🤝 En breve me pondre en contacto contigo. 🤓"
            }
        }
    elif "7" in texto:
        return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "📅 Horario de Atención : Lunes a Viernes. \n🕜 Horario : 9:00 am a 5:00 pm 🤓"
            }
        }
    elif "0" in texto:
        return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "🚀 Hola, visita mi web heso doks.com para más información.\n \n📌Por favor, ingresa un número #️⃣ para recibir información.\n \n1️⃣. Información del Curso. ❔\n2️⃣. Ubicación del local. 📍\n3️⃣. Enviar temario en PDF. 📄\n4️⃣. Audio explicando curso. 🎧\n5️⃣. Video de Introducción. ⏯️\n6️⃣. Hablar con AnderCode. 🙋‍♂️\n7️⃣. Horario de Atención. 🕜 \n0️⃣. Regresar al Menú. 🕜"
            }
        }
    elif "boton" in texto:
        return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive":{
                "type":"button",
                "body": {
                    "text": "¿Confirmas tu registro?"
                },
                "footer": {
                    "text": "Selecciona una de las opciones"
                },
                "action": {
                    "buttons":[
                        {
                            "type": "reply",
                            "reply":{
                                "id":"btnsi",
                                "title":"Si"
                            }
                        },{
                            "type": "reply",
                            "reply":{
                                "id":"btnno",
                                "title":"No"
                            }
                        },{
                            "type": "reply",
                            "reply":{
                                "id":"btntalvez",
                                "title":"Tal Vez"
                            }
                        }
                    ]
                }
            }
        }
    elif "btnsi" in texto:
        return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "Muchas Gracias por Aceptar."
            }
        }
    elif "btnno" in texto:
        return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "Es una Lastima."
            }
        }
    elif "btntalvez" in texto:
        return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "Estare a la espera."
            }
        }
    elif "lista" in texto:
        return {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "interactive",
            "interactive":{
                "type" : "list",
                "body": {
                    "text": "Selecciona Alguna Opción"
                },
                "footer": {
                    "text": "Selecciona una de las opciones para poder ayudarte"
                },
                "action":{
                    "button":"Ver Opciones",
                    "sections":[
                        {
                            "title":"Compra y Venta",
                            "rows":[
                                {
                                    "id":"btncompra",
                                    "title" : "Comprar",
                                    "description": "Compra los mejores articulos de tecnologia"
                                },
                                {
                                    "id":"btnvender",
                                    "title" : "Vender",
                                    "description": "Vende lo que ya no estes usando"
                                }
                            ]
                        },{
                            "title":"Distribución y Entrega",
                            "rows":[
                                {
                                    "id":"btndireccion",
                                    "title" : "Local",
                                    "description": "Puedes visitar nuestro local."
                                },
                                {
                                    "id":"btnentrega",
                                    "title" : "Entrega",
                                    "description": "La entrega se realiza todos los dias."
                                }
                            ]
                        }
                    ]
                }
            }
        }
    elif "btncompra" in texto:
        return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "Los mejos articulos top en ofertas."
            }
        }
    elif "btnvender" in texto:
        return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "Excelente elección."
            }
        }
    else:
        return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "🚀 Hola, visita mi web heso doks.com para más información.\n \n📌Por favor, ingresa un número #️⃣ para recibir información.\n \n1️⃣. Información del Curso. ❔\n2️⃣. Ubicación del local. 📍\n3️⃣. Enviar temario en PDF. 📄\n4️⃣. Audio explicando curso. 🎧\n5️⃣. Video de Introducción. ⏯️\n6️⃣. Hablar con AnderCode. 🙋‍♂️\n7️⃣. Horario de Atención. 🕜 \n0️⃣. Regresar al Menú. 🕜"
            }
        }