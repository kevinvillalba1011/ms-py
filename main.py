from flask import Flask, jsonify
from config import Config
from extensions import db
from usuarios import usuarios_bp, TipoDocumento, Estado
from billeteras import billeteras_bp
from transacciones import transacciones_bp
from comercios import comercios_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Create tables within app context
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return {"message": "Microservicio unificado funcionando con DB", "status": "ok"}

@app.route('/seed')
def seed():
    try:
        # Insertar Tipos de Documento si no existen
        if not TipoDocumento.query.get(1):
            db.session.add_all([
                TipoDocumento(id=1, nombre='Cédula de Ciudadanía'),
                TipoDocumento(id=2, nombre='Tarjeta de Identidad'),
                TipoDocumento(id=3, nombre='Pasaporte')
            ])
        
        # Insertar Estados si no existen
        if not Estado.query.get(1):
            db.session.add_all([
                Estado(id=1, nombre='Activo'),
                Estado(id=2, nombre='Inactivo')
            ])
        
        db.session.commit()
        return jsonify({"message": "Datos iniciales (Tipos y Estados) insertados correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Register Blueprints
app.register_blueprint(usuarios_bp)
app.register_blueprint(billeteras_bp)
app.register_blueprint(transacciones_bp)
app.register_blueprint(comercios_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
