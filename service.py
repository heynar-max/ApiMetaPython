import json
import http.client
from model import Log
from db import db
from flask import request, jsonify
from respuesta import generar_respuesta

TOKEN_HESODOKS = "HESODOKS"


#Funcion para agregar mensajes y guardar en la base de datos
def agregar_mensajes_log(texto):
    

    # Convertir el dict a una cadena JSON
    texto_json = json.dumps(texto, ensure_ascii=False)

    # Guardar el mensaje en la base de dato
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

