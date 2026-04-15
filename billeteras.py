from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

billeteras = []

@app.route('/billeteras', methods=['POST'])
def crear_billetera():
    data = request.json

    billetera = {
        "id": str(uuid.uuid4()),
        "usuario_id": data.get("usuario_id"),
        "saldo": 0
    }

    billeteras.append(billetera)
    return jsonify(billetera), 201


@app.route('/billeteras', methods=['GET'])
def listar_billeteras():
    return jsonify(billeteras)


if __name__ == '__main__':
    app.run(port=5002, debug=True)