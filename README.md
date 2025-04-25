# Student Management API with JWT Authentication and PDF Generation

This is a Django-based API project that allows CRUD operations on student data, integrates JWT authentication for secure access, and provides PDF generation of student records using `xhtml2pdf`.

## Features

- **CRUD Operations**: 
  - Create, Read, Update, and Delete student records.
  - Handles the student data including validation for age and name.
  
- **JWT Authentication**: 
  - Secures API access by implementing JSON Web Tokens (JWT) authentication for all endpoints.
  
- **PDF Generation**: 
  - Generates a PDF containing student records using `xhtml2pdf`.
  
- **Serializers**:
  - Custom validation for student data.
  - Nested serializer for related models (e.g., Book).

## Technologies Used

- **Django**: Backend framework for creating RESTful APIs.
- **Django REST Framework**: For building the API.
- **JWT Authentication**: For securing API endpoints.
- **xhtml2pdf**: To generate PDFs.
- **SQLite**: Database used for storing student and book data.
- **DRF SimpleJWT**: A package for JWT authentication.

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Django REST Framework
- DRF SimpleJWT
- xhtml2pdf

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repository-name.git
    cd your-repository-name
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser (optional but useful for accessing the admin panel):

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

### API Endpoints

- **GET /students/** - Fetch all students.
- **POST /students/** - Add a new student.
- **PUT /students/{id}/** - Update an existing student by ID.
- **DELETE /students/{id}/** - Delete a student by ID.
- **POST /register/** - Register a new user (returns JWT tokens).
- **GET /students/pdf/** - Generate a PDF of all students.

### Authentication

- The API uses JWT for authentication.
- Register a user using the `/register/` endpoint.
- Use the returned JWT tokens for accessing protected API endpoints by passing them in the `Authorization` header.

Example:

```bash
Authorization: Bearer <your_token>
