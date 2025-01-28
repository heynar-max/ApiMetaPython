

from regiones import amazonasregion


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
    if  "btnamazonia" in texto:
        return {
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
    # elif "btnamazonia" in texto:
    #     # Llamar a la función ApiRegiones o devolver el mensaje correspondiente
    #     return amazonasregion(texto, number)
        
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
    
        