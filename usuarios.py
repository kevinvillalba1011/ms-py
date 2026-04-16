from flask import Blueprint, request, jsonify
from extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID

usuarios_bp = Blueprint("usuarios", __name__)


# Definición de modelos para las tablas relacionadas (opcional pero recomendado para integridad)
class TipoDocumento(db.Model):
    __tablename__ = "tipos_documento"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)


class Estado(db.Model):
    __tablename__ = "estados"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tipo_documento_id = db.Column(db.Integer, db.ForeignKey("tipos_documento.id"))
    numero_documento = db.Column(db.String(30), nullable=False)
    nombre_completo = db.Column(db.String(150), nullable=False)
    telefono = db.Column(db.String(20))
    estado_id = db.Column(db.Integer, db.ForeignKey("estados.id"))

    # Restricción de unicidad
    __table_args__ = (
        db.UniqueConstraint(
            "tipo_documento_id", "numero_documento", name="uix_tipo_numero"
        ),
    )

    def to_dict(self):
        return {
            "id": str(self.id),
            "tipo_documento_id": self.tipo_documento_id,
            "numero_documento": self.numero_documento,
            "nombre_completo": self.nombre_completo,
            "telefono": self.telefono,
            "estado_id": self.estado_id,
        }


@usuarios_bp.route("/usuarios", methods=["POST"])
def crear_usuario():
    data = request.json

    try:
        nuevo_usuario = Usuario(
            tipo_documento_id=data.get("tipo_documento_id"),
            numero_documento=data.get("numero_documento"),
            nombre_completo=data.get("nombre_completo"),
            telefono=data.get("telefono"),
            estado_id=1,
        )

        db.session.add(nuevo_usuario)
        db.session.commit()
        return jsonify(nuevo_usuario.to_dict()), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


@usuarios_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():
    nombre = request.args.get("nombre_completo")
    documento = request.args.get("numero_documento")

    query = Usuario.query

    if nombre:
        query = query.filter(Usuario.nombre_completo.ilike(f"%{nombre}%"))
    if documento:
        query = query.filter(Usuario.numero_documento == documento)

    usuarios = query.all()
    return jsonify([u.to_dict() for u in usuarios])


@usuarios_bp.route("/usuarios/<id>", methods=["GET"])
def obtener_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        return jsonify(usuario.to_dict())
    return {"error": "Usuario no encontrado"}, 404
