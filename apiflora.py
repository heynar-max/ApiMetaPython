def apiflora(texto, number):
    return {
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