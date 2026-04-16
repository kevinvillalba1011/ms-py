from flask import Blueprint, request, jsonify
import uuid

billeteras_bp = Blueprint('billeteras', __name__)

billeteras = []

@billeteras_bp.route('/billeteras', methods=['POST'])
def crear_billetera():
    data = request.json

    billetera = {
        "id": str(uuid.uuid4()),
        "usuario_id": data.get("usuario_id"),
        "saldo": 0
    }

    billeteras.append(billetera)
    return jsonify(billetera), 201


@billeteras_bp.route('/billeteras', methods=['GET'])
def listar_billeteras():
    return jsonify(billeteras)