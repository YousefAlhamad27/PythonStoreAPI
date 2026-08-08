# Python Store API

A RESTful Web API built with FastAPI and MongoDB, featuring a layered architecture that cleanly separates routing, business logic, and database access. 

## Tech Stack
* **Framework:** FastAPI
* **Database:** MongoDB (via Beanie ODM)
* **Validation & DTOs:** Pydantic
* **Authentication:** JWT (JSON Web Tokens)
* **Deployment:** Docker & Docker Compose

## Architecture
This project follows a clean `src` layout to ensure maintainability and separation of concerns:
* **`routers/`**: Handles incoming HTTP requests and endpoints (Controllers).
* **`Services/`**: Contains the core business logic and database interactions.
* **`Models/`**: Beanie ODM document definitions mapping to MongoDB collections.
* **`Schemas/`**: Pydantic Data Transfer Objects (DTOs) for strict request/response validation.
* **`Auth/`**: JWT security and dependency injection.

## Setup & Installation

### 1. Environment Variables
Create a `.env` file in the root directory and add your configurations:
```env
TOKEN_SECRET_KEY="your_super_secret_key_here"
MONGO_CONNECTION_STRING="mongodb://localhost:27017"
```


### 2. Local Development
Make sure your virtual environment is activated, then run:

```bash
# Install dependencies
pip install -r requirements.txt

# Start the development server
uvicorn main:app --reload
```

Once running, you can access the interactive API documentation (Swagger UI) at http://127.0.0.1:8000/docs.

### 3. Docker Deployment

To run the application and its dependencies in containers:
```bash

docker compose up --build  
```
 

