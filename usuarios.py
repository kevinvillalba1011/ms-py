from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

usuarios = []

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json

    usuario = {
        "id": str(uuid.uuid4()),
        "nombre": data.get("nombre"),
        "documento": data.get("documento"),
        "telefono": data.get("telefono")
    }

    usuarios.append(usuario)
    return jsonify(usuario), 201


@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)


@app.route('/usuarios/<id>', methods=['GET'])
def obtener_usuario(id):
    for u in usuarios:
        if u["id"] == id:
            return jsonify(u)
    return {"error": "Usuario no encontrado"}, 404


if __name__ == '__main__':
    app.run(port=5001, debug=True)