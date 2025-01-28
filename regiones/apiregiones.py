

from amazonasregion import amazonasregion


def apiregiones(texto, number):
    
    if "btnsi" in texto:
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
                                    "description": "Región Amazónica."
                                },
                                {
                                    "id": "btnandina",
                                    "title": "Región Andina",
                                    "description": "Región Andina."
                                },
                                {
                                    "id": "btncaribe",
                                    "title": "Región Caribe",
                                    "description": "Región Caribe."
                                },
                                {
                                    "id": "btninsular",
                                    "title": "Región Insular",
                                    "description": "Región Insular."
                                },
                                {
                                    "id": "btnorinoquia",
                                    "title": "Región Orinoquia",
                                    "description": "Región Orinoquia."
                                },
                                {
                                    "id": "btnpacifica",
                                    "title": "Región Pacifica",
                                    "description": "Región Pacifica."
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
    elif "btnamazonia" in texto:
        # Llamar a la función ApiRegiones o devolver el mensaje correspondiente
        return amazonasregion(texto, number)
        
    # elif "btnandina" in texto:
    #     # Llamar a la función ApiFlora o devolver el mensaje correspondiente
    #     return amazonasregion(texto, number)
    
    # elif "btncaribe" in texto:
    #     # Llamar a la función ApiFlora o devolver el mensaje correspondiente
    #     return amazonasregion(texto, number)
    
    # elif "btninsular" in texto:
    #     # Llamar a la función ApiFlora o devolver el mensaje correspondiente
    #     return amazonasregion(texto, number)
    
    # elif "btnorinoquia" in texto:
    #     # Llamar a la función ApiFlora o devolver el mensaje correspondiente
    #     return amazonasregion(texto, number)
    
    # elif "btnpacifica" in texto:
    #     # Llamar a la función ApiFlora o devolver el mensaje correspondiente
    #     return amazonasregion(texto, number)
    
        