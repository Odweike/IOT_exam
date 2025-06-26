# Student Management API

REST API для управления студентами на Flask.

## Установка

1. Клонировать репозиторий:  
   ```bash
   git clone https://github.com/Odweike/IOT_exam.git
   cd IOT_exam
   ```

2. Создать виртуальное окружение:  
   ```bash
   python3 -m venv venv
   ```

3. Активировать виртуальное окружение:  
   - Для macOS/Linux:  
     ```bash
     source venv/bin/activate
     ```  
   - Для Windows:  
     ```bash
     venv\Scripts\activate
     ```

4. Установить зависимости:  
   ```bash
   pip install -r requirements.txt
   ```

5. Запустить сервер:  
   ```bash
   python app.py
   ```
   Сервер будет работать по адресу: http://localhost:8000

## API

- `GET /students` — получить всех студентов  
- `GET /students/active` — получить активных студентов  
- `GET /students/<id>` — получить студента по ID  
- `POST /students` — добавить нового студента  
- `DELETE /students/<id>` — удалить студента  

## Тестирование

Для запуска тестов выполните:  
```bash
pytest
```

## Пример POST запроса

```bash
curl -X POST http://localhost:8000/students -H "Content-Type: application/json" -d '{"first_name": "Иван", "last_name": "Петров", "group": "ИВТ-21", "email": "petrov@example.com"}'
```

## Формат данных студента

```json
{
  "id": "uuid",
  "first_name": "Имя",
  "last_name": "Фамилия",
  "group": "Группа",
  "email": "email@example.com",
  "status": "active или expelled"
}
```

Данные хранятся в памяти. При запуске загружаются тестовые данные.
