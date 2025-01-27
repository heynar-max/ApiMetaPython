def apiregiones(texto, number):
    return {
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
                                "description": "Con mayor biodiversidad del planeta, ubicada al sur del país."
                            },
                            {
                                "id": "btnandina",
                                "title": "Región Andina",
                                "description": "Una de las regiones más pobladas, Se encuentra en el centro del país."
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