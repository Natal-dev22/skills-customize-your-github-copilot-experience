# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for a small book library using FastAPI. Practice defining endpoints, validating request data, and returning appropriate HTTP status codes.

## 📝 Tasks

### 🛠️ Create the API and Read Books

#### Description
Complete the starter application to expose book data through read-only API endpoints. The application stores books in memory, so its data resets when the server restarts.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn with `python -m pip install fastapi uvicorn`.
- Use the provided Pydantic models and FastAPI app to represent books with an ID, title, and author.
- Implement `GET /books` to return all books as JSON and `GET /books/{book_id}` to return one book.
- Return HTTP `404 Not Found` when a requested book ID does not exist.
- From the assignment folder, run `uvicorn main:app --reload` and open `/docs` to explore and test the API.


### 🛠️ Add Create, Update, and Delete Endpoints

#### Description
Extend the API so clients can add books, replace a book's details, and remove books from the in-memory collection.

#### Requirements
Completed program should:

- Implement `POST /books` to validate book data, assign a unique ID, and return the created book with HTTP `201 Created`.
- Implement `PUT /books/{book_id}` to replace a book's title and author while preserving its ID; return `404 Not Found` if the ID does not exist.
- Implement `DELETE /books/{book_id}` to remove a book and return HTTP `204 No Content`; return `404 Not Found` if the ID does not exist.
- Use `/docs` to test successful requests and requests for IDs that do not exist.
