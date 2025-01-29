import json
import http.client


from app import agregar_mensajes_log

#funcion de la logica de los mensajes
def enviar_mensajes_whatsapp(texto,number):
    texto = texto.lower()

    if "hola" in texto:
        data={
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
        data = {
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
        data = {
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
        data={
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
        data={
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "audio",
            "audio": {
                "link": "https://filesamples.com/samples/audio/mp3/sample1.mp3"
            }
        }
    elif "5" in texto:
        data = {
            "messaging_product": "whatsapp",
            "to": number,
            "text": {
                "preview_url": True,
                "body": "Introduccion  https://www.youtube.com/watch?v=7M56JNzPH54&t=131s&ab_channel=HeynarSotoHolguin"
            }
        }
    elif "6" in texto:
        data = {
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
        data = {
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
        data = {
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
        data = {
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
        data = {
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
        data = {
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
        data = {
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
        data ={
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
        data = {
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
        data = {
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
        data={
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "🚀 Hola, visita mi web heso doks.com para más información.\n \n📌Por favor, ingresa un número #️⃣ para recibir información.\n \n1️⃣. Información del Curso. ❔\n2️⃣. Ubicación del local. 📍\n3️⃣. Enviar temario en PDF. 📄\n4️⃣. Audio explicando curso. 🎧\n5️⃣. Video de Introducción. ⏯️\n6️⃣. Hablar con AnderCode. 🙋‍♂️\n7️⃣. Horario de Atención. 🕜 \n0️⃣. Regresar al Menú. 🕜"
            }
        }

    #Convertir el diccionaria a formato JSON    
    data=json.dumps(data)

    headers = {
        "Content-Type" : "application/json",
        "Authorization" : "Bearer EAAImrVwLfJkBOzGWAFeukQaohFT3Pccy6c9uNtkWJebyRY0OZACyr9xqUZAx6wZCiCV9YLk5cpateXpJdzFz3AeYN146ONW2flirF6mybyuZC26bpdZA8sZCPCEPz6iXQJeqgRdnbZC2ns0TRufGfiRTxAZAlc0MTyVscwdZCdjK6wrNarcdH2kDYRlklC36hbiJIngZDZD"
    }

    connection = http.client.HTTPSConnection("graph.facebook.com")

    try:
        connection.request("POST","/v21.0/591402320714042/messages", data, headers)
        response = connection.getresponse()
        print(response.status, response.reason)
    except Exception as e:
        agregar_mensajes_log(json.dumps(e))
    finally:
        connection.close()


# 




# #funcion de la logica de los mensajes
# def enviar_mensajes_whatsapp(texto,number):
#     texto = texto.lower()

#     if "hola" in texto:
#         data={
#             "messaging_product": "whatsapp",
#             "recipient_type": "individual",
#             "to": number,
#             "type": "text",
#             "text": {
#                 "preview_url": False,
#                 "body": "🚀 Hola, ¿Cómo estás? Bienvenido. escribe BOTON para mas opciones"
#             }
#         }
#     elif "1" in texto:
#         data = {
#             "messaging_product": "whatsapp",
#             "recipient_type": "individual",
#             "to": number,
#             "type": "text",
#             "text": {
#                 "preview_url": False,
#                 "body": "La región Amazónica de Colombia, o Amazonía, comprende cerca del 40% del territorio colombiano y es la zona menos poblada del país."
#             }
#         }
#     elif "2" in texto:
#         data = {
#             "messaging_product": "whatsapp",
#             "recipient_type": "individual",
#             "to": number,
#             "type": "image",
#             "image": {
#                 "link": "https://i.pinimg.com/736x/1d/eb/b4/1debb497f6cc3f367bc21a6f415ca11d.jpg"
#             }
#         }
#     elif "3" in texto:
#         data={
#             "messaging_product": "whatsapp",
#             "recipient_type": "individual",
#             "to": number,
#             "type": "text",
#             "text": {
#                 "preview_url": False,
#                 "body": "Cubre los departamentos de Amazonas, Caquetá, Guainía, Guaviare, Putumayo y Vaupés."
#             }
#             }
#     elif "4" in texto:
#         data={
#             "messaging_product": "whatsapp",
#             "recipient_type": "individual",
#             "to": number,
#             "type": "text",
#             "text": {
#                 "preview_url": False,
#                 "body": "Itahuba, Caricari, Tajibos, Cedro, Cuta barcina, Reyna Victoria amazónica, Orquídeas, entre otros."
#             }
#         }
#     elif "5" in texto:
#         data = {
#             "messaging_product": "whatsapp",
#             "recipient_type": "individual",
#             "to": number,
#             "type": "text",
#             "text": {
#                 "preview_url": False,
#                 "body": "Jaguares, perezosos, delfines de río, guacamayos, anacondas, ranas de cristal, entre otros."
#             }
#         }
#     elif "6" in texto:
#         data = {
#             "messaging_product": "whatsapp",
#             "recipient_type": "individual",
#             "to": number,
#             "type": "text",
#             "text": {
#                 "preview_url": True,
#                 "body": "🎥 Mira este video: https://www.youtube.com/watch?v=2uQ0BzI1rVI&ab_channel=DiscosElDorado"
#             }
#         }
#     elif "7" in texto:
#         data = {
#             "messaging_product": "whatsapp",
#             "recipient_type": "individual",
#             "to": number,
#             "type": "text",
#             "text": {
#                 "preview_url": False,
#                 "body": "La región tiene un clima tropical húmedo, con altas precipitaciones y temperaturas calurosas."
#             }
#         }
#     elif "8" in texto:
#         data = {
#             "messaging_product": "whatsapp",
#             "recipient_type": "individual",
#             "to": number,
#             "type": "text",
#             "text": {
#                 "preview_url": False,
#                 "body": "El relieve está formado por montañas, llanuras, selvas, ríos y cuevas."
#             }
#         }
#     elif "boton" in texto:
#         data = {
#             "messaging_product": "whatsapp",
#             "recipient_type": "individual",
#             "to": number,
#             "type": "interactive",
#             "interactive": {
#                 "type": "button",
#                 "body": {
#                     "text": "Hola 👋 te damos la bienvenida. ¿Te gustaría conocer sobre las regiones de Colombia?"
#                 },
#                 "footer": {
#                     "text": "Selecciona una de las opciones"
#                 },
#                 "action": {
#                     "buttons": [
#                         {
#                             "type": "reply",
#                             "reply": {
#                                 "id": "btnsi",
#                                 "title": "Si"
#                             }
#                         },
#                         {
#                             "type": "reply",
#                             "reply": {
#                                 "id": "btnno",
#                                 "title": "No"
#                             }
#                         }
#                     ]
#                 }
#             }
#         }
#     elif "btnsi" in texto:
#         data = {
#             "messaging_product": "whatsapp",
#             "recipient_type": "individual",
#             "to": number,
#             "type": "interactive",
#             "interactive": {
#                 "type": "list",
#                 "body": {
#                     "text": "Selecciona alguna opción"
#                 },
#                 "footer": {
#                     "text": "Selecciona una de las regiones para explorar"
#                 },
#                 "action": {
#                     "button": "Ver opciones",
#                     "sections": [
#                         {
#                             "title": "Regiones",
#                             "rows": [
#                                 {
#                                     "id": "btnamazonia",
#                                     "title": "Región Amazónica",
                                    
#                                 },
#                                 {
#                                     "id": "btnandina",
#                                     "title": "Región Andina",
                                    
#                                 },
#                                 {
#                                     "id": "btncaribe",
#                                     "title": "Región Caribe",
                                    
#                                 },
#                                 {
#                                     "id": "btninsular",
#                                     "title": "Región Insular",
                                    
#                                 },
#                                 {
#                                     "id": "btnorinoquia",
#                                     "title": "Región Orinoquia",
                                    
#                                 },
#                                 {
#                                     "id": "btnpacifica",
#                                     "title": "Región Pacifica",
                                    
#                                 },
#                             ]
#                         },
#                         {
#                             "title": "Salir",
#                             "rows": [
#                                 {
#                                     "id": "fina",
#                                     "title": "Finalizar",
#                                     "description": "Hasta luego. 🌟"
#                                 }
#                             ]
#                         }
#                     ]
#                 }
#             }
#         }
#     elif "btnno" in texto:
#         data = {
#             "messaging_product": "whatsapp",
#         "to": number,
#         "type": "interactive",
#         "interactive": {
#             "type": "button",
#             "body": {
#                 "text": "Te gustaria tener conocimiento de la flora Colombiana?"
#             },
#             "footer": {
#                 "text": "Selecciona una de las opciones"
#             },
#             "action": {
#                 "buttons": [
#                     {
#                         "type": "reply",
#                         "reply": {
#                             "id": "flosi",
#                             "title": "Si"
#                         }
#                     },
#                     {
#                         "type": "reply",
#                         "reply": {
#                             "id": "flono",
#                             "title": "No"
#                         }
#                     },
#                     {
#                         "type": "reply",
#                         "reply":{
#                             "id":"fina",
#                             "title":"Finalizar"
#                         }
#                     }
#                 ]
#             }
#         }
#         }


#     elif "flono" in texto:
#         data = {
#             "messaging_product": "whatsapp",
#         "to": number,
#         "type": "interactive",
#         "interactive": {
#             "type": "button",
#             "body": {
#                 "text": "Te gustaria conocer la fauna colombiana?"
#             },
#             "footer": {
#                 "text": "Selecciona una de las opciones"
#             },
#             "action": {
#                 "buttons": [
#                     {
#                         "type": "reply",
#                         "reply": {
#                             "id": "fausi",
#                             "title": "Si"
#                         }
#                     },
#                     {
#                         "type": "reply",
#                         "reply": {
#                             "id": "fauno",
#                             "title": "No"
#                         }
#                     },
#                     {
#                         "type": "reply",
#                         "reply":{
#                             "id":"fina",
#                             "title":"Finalizar"
#                         }
#                     }
#                 ]
#             }
#         }
#         }
#     elif "fauno" in texto:
#         data = {
#             "messaging_product": "whatsapp",
#             "to": number,
#             "type": "interactive",
#             "interactive": {
#                 "type": "button",
#                 "body": {
#                     "text": "Te gustaria saber que climas tiene colombia?"
#                 },
#                 "footer": {
#                     "text": "Selecciona una de las opciones"
#                 },
#                 "action": {
#                     "buttons": [
#                         {
#                             "type": "reply",
#                             "reply": {
#                                 "id": "clisi",
#                                 "title": "Si"
#                             }
#                         },
#                         {
#                             "type": "reply",
#                             "reply": {
#                                 "id": "clino",
#                                 "title": "No"
#                             }
#                         },
#                         {
#                             "type": "reply",
#                             "reply":{
#                                 "id":"fina",
#                                 "title":"Finalizar"
#                             }
#                         }
#                     ]
#                 }
#             }
#         }
#     elif "clino" in texto:
#         data = {
#             "messaging_product": "whatsapp",
#             "to": number,
#             "type": "interactive",
#             "interactive": {
#                 "type": "button",
#                 "body": {
#                     "text": "Te gustaria saber que relieve tiene colombia?"
#                 },
#                 "footer": {
#                     "text": "Selecciona una de las opciones"
#                 },
#                 "action": {
#                     "buttons": [
#                         {
#                             "type": "reply",
#                             "reply": {
#                                 "id": "relsi",
#                                 "title": "Si"
#                             }
#                         },
#                         {
#                             "type": "reply",
#                             "reply": {
#                                 "id": "finalizar",
#                                 "title": "No"
#                             }
#                         },
#                         {
#                             "type": "reply",
#                             "reply":{
#                                 "id":"fina",
#                                 "title":"Finalizar"
#                             }
#                         }
#                     ]
#                 }
#             }
#         }
#     elif "btnamazonia" in texto:
#         data = {
#             "messaging_product": "whatsapp",
#             "recipient_type": "individual",
#             "to": number,
#             "type": "text",
#             "text": {
#                 "preview_url": False,
#                 "body": "🌿 *La Región Amazónica* 🌿 \n\n📌 Por favor, ingresa un número #️⃣ para recibir información:\n\n"
#                         "1️⃣. Información Región Amazónica ❔\n2️⃣. Ubicación 📍 (PDF)\n3️⃣. Departamentos 📄\n4️⃣. Flora 🌿\n"
#                         "5️⃣. Fauna 🐉\n6️⃣. Video sobre la región ⏯️\n7️⃣. Clima 🌤️\n8️⃣. Relieve 🏔️"
#             }
#         }

#     #Convertir el diccionaria a formato JSON    
#     data=json.dumps(data)
    
#     headers = {
#         "Content-Type" : "application/json",
#         "Authorization" : "Bearer EAAImrVwLfJkBOzGWAFeukQaohFT3Pccy6c9uNtkWJebyRY0OZACyr9xqUZAx6wZCiCV9YLk5cpateXpJdzFz3AeYN146ONW2flirF6mybyuZC26bpdZA8sZCPCEPz6iXQJeqgRdnbZC2ns0TRufGfiRTxAZAlc0MTyVscwdZCdjK6wrNarcdH2kDYRlklC36hbiJIngZDZD"
#     }

#     connection = http.client.HTTPSConnection("graph.facebook.com")

#     try:
#         connection.request("POST","/v21.0/591402320714042/messages", data, headers)
#         response = connection.getresponse()
#         print(response.status, response.reason)
#     except Exception as e:
#         agregar_mensajes_log(json.dumps(e))
#     finally:
#         connection.close()