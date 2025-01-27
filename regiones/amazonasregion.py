def amazonasregion(texto, number):
    # Imprimir el valor de texto para depuración
    print(f"Texto recibido: {texto}")
    
    # Normalizar el valor de texto por si contiene espacios adicionales
    texto = texto.strip().lower()  # Quita espacios y lo convierte en minúsculas
    
    if texto == "btnamazonia":
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
    elif texto == "1":
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
    elif texto == "2":
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "image",
            "image": {
                "link": "https://i.pinimg.com/736x/1d/eb/b4/1debb497f6cc3f367bc21a6f415ca11d.jpg"
            }
        }
    elif texto == "3":
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "Cubre los departamentos de Amazonas, Caquetá, Guainía, Guaviare, Putumayo y Vaupés."
            }
        }
    elif texto == "4":
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "Itahuba, Caricari, Tajibos, Cedro, Cuta barcina, Reyna Victoria amazónica, Orquídeas, entre otros."
            }
        }
    elif texto == "5":
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
    elif texto == "6":
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
    elif texto == "7":
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
    elif texto == "8":
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
    else:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "❌ Opción no válida. Por favor, ingresa un número entre 1 y 8 para recibir información."
            }
        }

    return data