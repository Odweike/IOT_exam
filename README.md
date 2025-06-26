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

## Системные требования

### Операционная система
- macOS 10.14+  
- Windows 10+  
- Ubuntu Linux 18.04+ (или аналогичные дистрибутивы)

### Программное обеспечение
- **Python 3.8+** (обязательно)  
- **pip** (поставляется с Python)  
- **git** (для клонирования репозитория)

### Для Ubuntu Linux 24.04
Если у вас стандартная установка Ubuntu, выполните:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git curl
```

### Проверка установки
Убедитесь, что установлены нужные версии:
```bash
python3 --version  # должно быть 3.8+
pip --version
git --version
```

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
curl -X POST http://localhost:8000/students \
     -H "Content-Type: application/json" \
     -d '{"first_name": "Иван", "last_name": "Петров", "group": "ИВТ-21", "email": "petrov@example.com"}'
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

> ℹ️ Данные хранятся в памяти. При запуске загружаются тестовые данные.
