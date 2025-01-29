from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from controller import webhook

app = Flask(__name__)

#Configuracion de la base de datos SQLITE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metapython.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db =SQLAlchemy(app)

#Modelo de la tabla log
class Log(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fecha_y_hora = db.Column(db.DateTime, default=datetime.utcnow)
    texto = db.Column(db.TEXT)

#Crear la tabla si no existe
with app.app_context():
    db.create_all()



    # Registrar rutas del controlador
app.register_blueprint(webhook)

#Funcion para ordenar los registros por fecha y hora
def ordenar_por_fecha_y_hora(registros):
    return sorted(registros, key=lambda x: x.fecha_y_hora,reverse=True)


@app.route('/')
def index():
    #obtener todos los registros ed la base de datos
    registros = Log.query.all()
    registros_ordenados = ordenar_por_fecha_y_hora(registros)
    return render_template('index.html',registros=registros_ordenados)

    

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
                "body": "🚀 Hola, ¿Cómo estás? Bienvenido. escribe BOTON para mas opciones"
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
                "body": "La región Amazónica de Colombia, o Amazonía, comprende cerca del 40% del territorio colombiano y es la zona menos poblada del país."
            }
        }
    elif "2" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "image",
            "image": {
                "link": "https://i.pinimg.com/736x/1d/eb/b4/1debb497f6cc3f367bc21a6f415ca11d.jpg"
            }
        }
    elif "3" in texto:
        data={
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "Cubre los departamentos de Amazonas, Caquetá, Guainía, Guaviare, Putumayo y Vaupés."
            }
            }
    elif "4" in texto:
        data={
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "Itahuba, Caricari, Tajibos, Cedro, Cuta barcina, Reyna Victoria amazónica, Orquídeas, entre otros."
            }
        }
    elif "5" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "Jaguares, perezosos, delfines de río, guacamayos, anacondas, ranas de cristal, entre otros."
            }
        }
    elif "6" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": True,
                "body": "🎥 Mira este video: https://www.youtube.com/watch?v=2uQ0BzI1rVI&ab_channel=DiscosElDorado"
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
                "body": "La región tiene un clima tropical húmedo, con altas precipitaciones y temperaturas calurosas."
            }
        }
    elif "8" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "El relieve está formado por montañas, llanuras, selvas, ríos y cuevas."
            }
        }
    elif "boton" in texto:
        data = {
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
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "body": {
                    "text": "Selecciona alguna opción"
                },
                "footer": {
                    "text": "Selecciona una de las regiones para explorar"
                },
                "action": {
                    "button": "Ver opciones",
                    "sections": [
                        {
                            "title": "Regiones",
                            "rows": [
                                {
                                    "id": "btnamazonia",
                                    "title": "Región Amazónica",
                                    
                                },
                                {
                                    "id": "btnandina",
                                    "title": "Región Andina",
                                    
                                },
                                {
                                    "id": "btncaribe",
                                    "title": "Región Caribe",
                                    
                                },
                                {
                                    "id": "btninsular",
                                    "title": "Región Insular",
                                    
                                },
                                {
                                    "id": "btnorinoquia",
                                    "title": "Región Orinoquia",
                                    
                                },
                                {
                                    "id": "btnpacifica",
                                    "title": "Región Pacifica",
                                    
                                },
                            ]
                        },
                        {
                            "title": "Salir",
                            "rows": [
                                {
                                    "id": "fina",
                                    "title": "Finalizar",
                                    "description": "Hasta luego. 🌟"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    elif "btnno" in texto:
        data = {
            "messaging_product": "whatsapp",
        "to": number,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": "Te gustaria tener conocimiento de la flora Colombiana?"
            },
            "footer": {
                "text": "Selecciona una de las opciones"
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "flosi",
                            "title": "Si"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "flono",
                            "title": "No"
                        }
                    },
                    {
                        "type": "reply",
                        "reply":{
                            "id":"fina",
                            "title":"Finalizar"
                        }
                    }
                ]
            }
        }
        }


    elif "flono" in texto:
        data = {
            "messaging_product": "whatsapp",
        "to": number,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": "Te gustaria conocer la fauna colombiana?"
            },
            "footer": {
                "text": "Selecciona una de las opciones"
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "fausi",
                            "title": "Si"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "fauno",
                            "title": "No"
                        }
                    },
                    {
                        "type": "reply",
                        "reply":{
                            "id":"fina",
                            "title":"Finalizar"
                        }
                    }
                ]
            }
        }
        }
    elif "fauno" in texto:
        data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": "Te gustaria saber que climas tiene colombia?"
                },
                "footer": {
                    "text": "Selecciona una de las opciones"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "clisi",
                                "title": "Si"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "clino",
                                "title": "No"
                            }
                        },
                        {
                            "type": "reply",
                            "reply":{
                                "id":"fina",
                                "title":"Finalizar"
                            }
                        }
                    ]
                }
            }
        }
    elif "clino" in texto:
        data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": "Te gustaria saber que relieve tiene colombia?"
                },
                "footer": {
                    "text": "Selecciona una de las opciones"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "relsi",
                                "title": "Si"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "finalizar",
                                "title": "No"
                            }
                        },
                        {
                            "type": "reply",
                            "reply":{
                                "id":"fina",
                                "title":"Finalizar"
                            }
                        }
                    ]
                }
            }
        }
    elif "btnamazonia" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "🌿 *La Región Amazónica* 🌿 \n\n📌 Por favor, ingresa un número #️⃣ para recibir información:\n\n"
                        "1️⃣. Información Región Amazónica ❔\n2️⃣. Ubicación 📍 (PDF)\n3️⃣. Departamentos 📄\n4️⃣. Flora 🌿\n"
                        "5️⃣. Fauna 🐉\n6️⃣. Video sobre la región ⏯️\n7️⃣. Clima 🌤️\n8️⃣. Relieve 🏔️"
            }
        }

    #Convertir el diccionaria a formato JSON    
    data=json.dumps(data)



if __name__=="__main__":
    app.run(host='0.0.0.0',port=80,debug=True)