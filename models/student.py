import uuid
from typing import List, Dict, Optional

class Student:
    def __init__(self, first_name: str, last_name: str, group: str, email: str, status: str = "active"):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.email = email
        self.status = status
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "group": self.group,
            "email": self.email,
            "status": self.status
        }

class StudentStorage:
    def __init__(self):
        self.students: List[Student] = []
        self._init_test_data()
    
    def _init_test_data(self):
        test_students = [
            Student("Иван", "Иванов", "ИВТ-21", "ivanov@example.com", "active"),
            Student("Петр", "Петров", "ИВТ-21", "petrov@example.com", "active"),
            Student("Анна", "Сидорова", "ИВТ-22", "sidorova@example.com", "expelled"),
        ]
        self.students.extend(test_students)
    
    def get_all(self) -> List[Dict]:
        return [student.to_dict() for student in self.students]
    
    def get_active(self) -> List[Dict]:
        return [student.to_dict() for student in self.students if student.status == "active"]
    
    def get_by_id(self, student_id: str) -> Optional[Dict]:
        for student in self.students:
            if student.id == student_id:
                return student.to_dict()
        return None
    
    def add_student(self, student_data: Dict) -> Dict:
        student = Student(
            student_data["first_name"],
            student_data["last_name"],
            student_data["group"],
            student_data["email"],
            student_data.get("status", "active")
        )
        self.students.append(student)
        return student.to_dict()
    
    def delete_student(self, student_id: str) -> bool:
        for i, student in enumerate(self.students):
            if student.id == student_id:
                del self.students[i]
                return True
        return False
