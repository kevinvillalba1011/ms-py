from flask import Flask, request, jsonify
import uuid
import requests

app = Flask(__name__)

transacciones = []

@app.route('/transacciones', methods=['POST'])
def crear_transaccion():
    data = request.json

    transaccion = {
        "id": str(uuid.uuid4()),
        "origen": data.get("origen"),
        "destino": data.get("destino"),
        "monto": data.get("monto")
    }

    transacciones.append(transaccion)
    return jsonify(transaccion), 201


@app.route('/transacciones', methods=['GET'])
def listar_transacciones():
    return jsonify(transacciones)


if __name__ == '__main__':
    app.run(port=5003, debug=True)