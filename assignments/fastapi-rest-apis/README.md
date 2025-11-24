# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using FastAPI, a modern, fast web framework for building APIs with Python. You will create a simple task management API that supports creating, reading, updating, and deleting tasks.

## 📝 Tasks

### 🛠️	Setup FastAPI and Create Your First Endpoint

#### Description
Set up a FastAPI application and create a basic endpoint that returns a welcome message. This will help you understand the fundamentals of FastAPI and how to run a local development server.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn (ASGI server) using pip
- Create a FastAPI application instance
- Define a GET endpoint at the root path (`/`) that returns a welcome message
- Run the server using Uvicorn and verify it works in the browser


### 🛠️	Create a Task Management API

#### Description
Build a complete REST API for managing tasks. Your API should support the four basic CRUD operations (Create, Read, Update, Delete) for tasks. Each task should have an id, title, description, and a completed status.

#### Requirements
Completed program should:

- Define a Task model using Pydantic with fields: id (int), title (str), description (str), and completed (bool)
- Implement a GET `/tasks` endpoint that returns all tasks
- Implement a GET `/tasks/{task_id}` endpoint that returns a specific task by ID
- Implement a POST `/tasks` endpoint that creates a new task
- Implement a PUT `/tasks/{task_id}` endpoint that updates an existing task
- Implement a DELETE `/tasks/{task_id}` endpoint that deletes a task
- Use an in-memory list to store tasks (no database required)
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Include proper error handling for cases like "task not found"


### 🛠️	Test Your API

#### Description
Test all your API endpoints using FastAPI's automatic interactive documentation or a tool like curl or Postman. Verify that all CRUD operations work correctly.

#### Requirements
Completed program should:

- Access the automatic API documentation at `/docs` (Swagger UI)
- Successfully create at least 3 tasks using the POST endpoint
- Retrieve all tasks and verify they are returned correctly
- Update at least one task and verify the changes
- Delete at least one task and verify it's removed
- Test error cases (e.g., trying to get a task with an invalid ID)
