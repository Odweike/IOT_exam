# Student Management API

REST API для управления студентами на Flask.

## Установка

1. Клонировать репозиторий:
git clone <ссылка>
cd student-management-api

2. Создать виртуальное окружение:
python3 -m venv venv

3. Активировать окружение:
macOS/Linux: source venv/bin/activate
Windows: venv\Scripts\activate

4. Установить зависимости:
pip install -r requirements.txt

5. Запустить сервер:
python app.py

Сервер работает на http://localhost:8000

## API

GET /students - все студенты
GET /students/active - активные студенты  
GET /students/<id> - студент по ID
POST /students - добавить студента
DELETE /students/<id> - удалить студента

## Тестирование

pytest

## Пример POST запроса

curl -X POST http://localhost:8000/students -H "Content-Type: application/json" -d '{"first_name": "Иван", "last_name": "Петров", "group": "ИВТ-21", "email": "petrov@example.com"}'

## Формат данных студента

{
  "id": "uuid",
  "first_name": "Имя",
  "last_name": "Фамилия",
  "group": "Группа", 
  "email": "email@example.com",
  "status": "active или expelled"
}

Данные хранятся в памяти. При запуске загружаются тестовые данные.
