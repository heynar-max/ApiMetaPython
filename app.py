from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controller import webhook

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metapython.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Crear la tabla si no existe
with app.app_context():
    db.create_all()

# Registrar rutas del controlador
app.register_blueprint(webhook)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)