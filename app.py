from flask import Flask, jsonify, request
from models.student import StudentStorage

app = Flask(__name__)
storage = StudentStorage()

@app.route('/students', methods=['GET'])
def get_students():
    """Получить список всех студентов"""
    return jsonify(storage.get_all())

@app.route('/students/active', methods=['GET'])
def get_active_students():
    """Получить только активных студентов"""
    return jsonify(storage.get_active())

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    """Получить информацию о студенте по ID"""
    student = storage.get_by_id(student_id)
    if student:
        return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

@app.route('/students', methods=['POST'])
def add_student():
    """Добавить нового студента"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        required_fields = ["first_name", "last_name", "group", "email"]
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {missing_fields}"}), 400
        
        # Валидация email
        if "@" not in data["email"]:
            return jsonify({"error": "Invalid email format"}), 400
        
        # Валидация статуса
        if "status" in data and data["status"] not in ["active", "expelled"]:
            return jsonify({"error": "Status must be 'active' or 'expelled'"}), 400
        
        student = storage.add_student(data)
        return jsonify(student), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Удалить студента"""
    if storage.delete_student(student_id):
        return jsonify({"message": "Student deleted successfully"})
    return jsonify({"error": "Student not found"}), 404

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
