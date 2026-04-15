from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

comercios = []

@app.route('/comercios', methods=['POST'])
def crear_comercio():
    data = request.json

    comercio = {
        "id": str(uuid.uuid4()),
        "nombre": data.get("nombre"),
        "nit": data.get("nit")
    }

    comercios.append(comercio)
    return jsonify(comercio), 201


@app.route('/comercios', methods=['GET'])
def listar_comercios():
    return jsonify(comercios)


if __name__ == '__main__':
    app.run(port=5004, debug=True)