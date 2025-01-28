def amazonasregion(texto, number):
    
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
    # if  "1" in texto:
    #     return  {
    #         "messaging_product": "whatsapp",
    #         "recipient_type": "individual",
    #         "to": number,
    #         "type": "text",
    #         "text": {
    #             "preview_url": False,
    #             "body": "La región Amazónica de Colombia, o Amazonía, comprende cerca del 40% del territorio colombiano y es la zona menos poblada del país."
    #         }
    #     }
    # elif  "2" in texto:
    #     return  {
    #         "messaging_product": "whatsapp",
    #         "recipient_type": "individual",
    #         "to": number,
    #         "type": "image",
    #         "image": {
    #             "link": "https://i.pinimg.com/736x/1d/eb/b4/1debb497f6cc3f367bc21a6f415ca11d.jpg"
    #         }
    #     }
    # elif  "3" in texto:
    #     return  {
    #         "messaging_product": "whatsapp",
    #         "recipient_type": "individual",
    #         "to": number,
    #         "type": "text",
    #         "text": {
    #             "preview_url": False,
    #             "body": "Cubre los departamentos de Amazonas, Caquetá, Guainía, Guaviare, Putumayo y Vaupés."
    #         }
    #     }
    # elif  "4" in texto:
    #     return  {
    #         "messaging_product": "whatsapp",
    #         "recipient_type": "individual",
    #         "to": number,
    #         "type": "text",
    #         "text": {
    #             "preview_url": False,
    #             "body": "Itahuba, Caricari, Tajibos, Cedro, Cuta barcina, Reyna Victoria amazónica, Orquídeas, entre otros."
    #         }
    #     }
    # elif  "5" in texto:
    #     return  {
    #         "messaging_product": "whatsapp",
    #         "recipient_type": "individual",
    #         "to": number,
    #         "type": "text",
    #         "text": {
    #             "preview_url": False,
    #             "body": "Jaguares, perezosos, delfines de río, guacamayos, anacondas, ranas de cristal, entre otros."
    #         }
    #     }
    # elif  "6" in texto:
    #     return  {
    #         "messaging_product": "whatsapp",
    #         "recipient_type": "individual",
    #         "to": number,
    #         "type": "text",
    #         "text": {
    #             "preview_url": True,
    #             "body": "🎥 Mira este video: https://www.youtube.com/watch?v=2uQ0BzI1rVI&ab_channel=DiscosElDorado"
    #         }
    #     }
    # elif  "7" in texto:
    #     return  {
    #         "messaging_product": "whatsapp",
    #         "recipient_type": "individual",
    #         "to": number,
    #         "type": "text",
    #         "text": {
    #             "preview_url": False,
    #             "body": "La región tiene un clima tropical húmedo, con altas precipitaciones y temperaturas calurosas."
    #         }
    #     }
    # elif  "8" in texto:
    #     return  {
    #         "messaging_product": "whatsapp",
    #         "recipient_type": "individual",
    #         "to": number,
    #         "type": "text",
    #         "text": {
    #             "preview_url": False,
    #             "body": "El relieve está formado por montañas, llanuras, selvas, ríos y cuevas."
    #         }
    #     }
    # else:
    #     return  {
    #         "messaging_product": "whatsapp",
    #         "recipient_type": "individual",
    #         "to": number,
    #         "type": "text",
    #         "text": {
    #             "preview_url": False,
    #             "body": "❌ Opción no válida. Por favor, ingresa un número entre 1 y 8 para recibir información."
    #         }
    #     }

