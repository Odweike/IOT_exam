import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestStudentsAPI:
    
    def test_get_all_students_success(self, client):
        """Тест получения всех студентов - корректный случай"""
        response = client.get('/students')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) >= 3  # У нас есть тестовые данные

    def test_get_all_students_structure(self, client):
        """Тест структуры данных студентов"""
        response = client.get('/students')
        data = json.loads(response.data)
        student = data[0]  # Исправлено: берем первого студента из списка
        required_fields = ["id", "first_name", "last_name", "group", "email", "status"]
        for field in required_fields:
            assert field in student

    def test_get_active_students_success(self, client):
        """Тест получения активных студентов - корректный случай"""
        response = client.get('/students/active')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        for student in data:
            assert student["status"] == "active"

    def test_get_active_students_empty_result(self, client):
        """Тест получения активных студентов - может быть пустой список"""
        response = client.get('/students/active')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)

    def test_get_student_by_id_success(self, client):
        """Тест получения студента по ID - корректный случай"""
        # Сначала получаем список студентов
        response = client.get('/students')
        students = json.loads(response.data)
        student_id = students[0]["id"]  # Исправлено: берем ID первого студента
        
        # Затем получаем конкретного студента
        response = client.get(f'/students/{student_id}')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data["id"] == student_id

    def test_get_student_by_id_not_found(self, client):
        """Тест получения студента по ID - некорректный ID"""
        response = client.get('/students/nonexistent-id')
        assert response.status_code == 404
        data = json.loads(response.data)
        assert "error" in data

    def test_add_student_success(self, client):
        """Тест добавления студента - корректные данные"""
        new_student = {
            "first_name": "Тест",
            "last_name": "Тестов",
            "group": "ИВТ-23",
            "email": "test@example.com",
            "status": "active"
        }
        response = client.post('/students', 
                             data=json.dumps(new_student),
                             content_type='application/json')
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data["first_name"] == "Тест"
        assert "id" in data

    def test_add_student_missing_fields(self, client):
        """Тест добавления студента - отсутствуют обязательные поля"""
        incomplete_student = {
            "first_name": "Тест"
            # Отсутствуют остальные обязательные поля
        }
        response = client.post('/students',
                             data=json.dumps(incomplete_student),
                             content_type='application/json')
        assert response.status_code == 400
        data = json.loads(response.data)
        assert "error" in data

    def test_delete_student_success(self, client):
        """Тест удаления студента - корректный случай"""
        # Сначала получаем ID существующего студента
        response = client.get('/students')
        students = json.loads(response.data)
        student_id = students[0]["id"]  # Исправлено: берем ID первого студента
        
        # Удаляем студента
        response = client.delete(f'/students/{student_id}')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "message" in data

    def test_delete_student_not_found(self, client):
        """Тест удаления студента - несуществующий ID"""
        response = client.delete('/students/nonexistent-id')
        assert response.status_code == 404
        data = json.loads(response.data)
        assert "error" in data
