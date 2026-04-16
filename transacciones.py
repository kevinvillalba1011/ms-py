from flask import Blueprint, request, jsonify
import uuid
import requests

transacciones_bp = Blueprint('transacciones', __name__)

transacciones = []

@transacciones_bp.route('/transacciones', methods=['POST'])
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


@transacciones_bp.route('/transacciones', methods=['GET'])
def listar_transacciones():
    return jsonify(transacciones)