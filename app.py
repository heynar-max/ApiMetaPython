from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

from service import enviar_mensajes_whatsapp

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


#Funcion para ordenar los registros por fecha y hora
def ordenar_por_fecha_y_hora(registros):
    return sorted(registros, key=lambda x: x.fecha_y_hora,reverse=True)


@app.route('/')
def index():
    #obtener todos los registros ed la base de datos
    registros = Log.query.all()
    registros_ordenados = ordenar_por_fecha_y_hora(registros)
    return render_template('index.html',registros=registros_ordenados)

mensajes_log = []

#Funcion para agregar mensajes y guardar en la base de datos
def agregar_mensajes_log(texto):
    mensajes_log.append(texto)
    
    # Convertir el dict a una cadena JSON
    texto_json = json.dumps(texto, ensure_ascii=False)

    # Guardar el mensaje en la base de datos
    nuevo_registro = Log(texto=texto_json)
    db.session.add(nuevo_registro)
    db.session.commit()

#Token de verificacion para la configuracion
TOKEN_HESODOKS = "HESODOKS"


@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        challenge = verificar_token(request)
        return challenge
    elif request.method == 'POST':
        reponse = recibir_mensajes(request)
        return reponse

def verificar_token(req):
    token = req.args.get('hub.verify_token')
    challenge = req.args.get('hub.challenge')

    if challenge and token == TOKEN_HESODOKS:
        return challenge
    else:
        return jsonify({'error':'Token Invalido'}),401
    

def recibir_mensajes(req):
    try:
        req = request.get_json()
        entry =req['entry'][0]
        changes = entry['changes'][0]
        value = changes['value']
        objeto_mensaje = value['messages']

        if objeto_mensaje:
            messages = objeto_mensaje[0]

            if "type" in messages:
                tipo = messages["type"]
                
                #guardar log en la BD
                agregar_mensajes_log(json.dumps(messages))

                if tipo == "interactive":
                    tipo_interactivo = messages["interactive"]["type"]

                    if tipo_interactivo == "button_reply":
                        text = messages["interactive"]["button_reply"]["id"]
                        numero = messages["from"]

                        enviar_mensajes_whatsapp(text,numero)

                    elif tipo_interactivo == "list_reply":
                        text = messages["interactive"]["list_reply"]["id"]
                        numero = messages["from"]

                        enviar_mensajes_whatsapp(text,numero)


                if "text" in messages:
                    text = messages["text"]["body"]
                    numero = messages["from"]

                    enviar_mensajes_whatsapp( text, numero )

                    #guardar log en la BD
                    agregar_mensajes_log(json.dumps (messages))

        return jsonify({'message':'EVENT_RECEIVED'})
    except Exception as e:
        return jsonify({'message':'EVENT_RECEIVED'})
    

if __name__=="__main__":
    app.run(host='0.0.0.0',port=80,debug=True)