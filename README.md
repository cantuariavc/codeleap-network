# 🚀 CodeLeap Network API

API built with Django REST Framework for managing posts (full CRUD), including creation, listing, updating, and deletion.

## 🔧 Installation and Setup

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/cantuariavc/codeleap-network.git
   cd codeleap-network
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   # ou
   venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **(Optional) Load sample data**
   ```bash
   python manage.py loaddata career_data.json
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at: `http://127.0.0.1:8000/`

## 📚 API Documentation

### Available Endpoints

#### Posts
- `GET /careers/` - Retrieve all posts
- `POST /careers/` - Create a new post
- `GET /careers/{id}/` - Retrieve a specific post
- `PATCH /careers/{id}/` - Partially update a post
- `DELETE /careers/{id}/` - Delete a post

### Post Structure

```json
{
  "id": "number",
  "username": "string",
  "created_datetime": "datetime",
  "title": "string",
  "content": "string",
}
```

### Usage Examples

#### Create a new post
```bash
curl -X POST http://127.0.0.1:8000/careers/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "ana",
    "title": "Analista de Dados",
    "content": "Especialista em Python e SQL"
  }'
```

#### List all posts
```bash
curl http://127.0.0.1:8000/careers/
```

#### Retrieve a specific post
```bash
curl http://127.0.0.1:8000/careers/1/
```

#### Partially update a post
```bash
curl -X PATCH http://127.0.0.1:8000/careers/1/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Title", "content": "Updated Content"}'
```

#### Delete a post
```bash
curl -X DELETE http://127.0.0.1:8000/careers/1/
```


## 🗄️ Modelo de Dados

### Career
- `id` (Integer, Primary Key) - Unique identifier (auto-generated)
- `username` (CharField, max_length=50) - Username
- `title` (CharField, max_length=200) - Post title
- `content` (TextField) - Post content
- `created_datetime` (DateTimeField) - Creation date and time (auto-generated)

## 📝 Sample Data

The project includes example data in the file: `career/fixtures/career_data.json`

This file contains posts from different users to make development and testing easier.

## 📄 License

This project is licensed under the MIT License, as specified in the LICENSE file.