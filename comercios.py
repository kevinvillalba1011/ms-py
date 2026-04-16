from flask import Blueprint, request, jsonify
import uuid

comercios_bp = Blueprint('comercios', __name__)

comercios = []

@comercios_bp.route('/comercios', methods=['POST'])
def crear_comercio():
    data = request.json

    comercio = {
        "id": str(uuid.uuid4()),
        "nombre": data.get("nombre"),
        "nit": data.get("nit")
    }

    comercios.append(comercio)
    return jsonify(comercio), 201


@comercios_bp.route('/comercios', methods=['GET'])
def listar_comercios():
    return jsonify(comercios)