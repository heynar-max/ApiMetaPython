from flask import Blueprint, request
from app import verificar_token, recibir_mensajes

webhook = Blueprint('webhook', __name__)

@webhook.route('/webhook', methods=['GET', 'POST'])
def webhook_handler():
    if request.method == 'GET':
        return verificar_token(request)
    elif request.method == 'POST':
        return recibir_mensajes(request)