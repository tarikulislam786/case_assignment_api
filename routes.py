from flask import Blueprint, request, jsonify
from  flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Assignment

assignment_bp = Blueprint('assignment', __name__, url_prefix='/assignments')

@assignment_bp.route('', methods=['POST'])
@jwt_required()
def create_assignment():
    data = request.get_json()
    assignment = Assignment(
        case_id=data['case_id'],
        user_id=data['user_id'],
        status=data['status']
    )
    db.session.add(assignment)
    db.session.commit()
    return jsonify(msg="Assignment created"), 201
@assignment_bp.route('', methods=['GET'])
@jwt_required()
def get_assignments():
    assignments = Assignment.query.all()
    return jsonify([{
        "id": a.id,
        "case_id": a.case_id,
        "user_id":a.user_id,
        "status": a.status
    } for a in assignments])

@assignment_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_assignment(id):
    data = request.get_json()
    assignment = Assignment.query.get_or_404(id)
    assignment.status = data['status']
    assignment.case_id = data['case_id']
    assignment.user_id = data['user_id']
    db.session.commit()
    return jsonify(msg="Assignment updated"), 200

@assignment_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_assignment(id):
    assignment = Assignment.query.get_or_404(id)
    db.session.delete(assignment)
    db.session.commit()
    return jsonify(msg="Assignment deleted"), 200