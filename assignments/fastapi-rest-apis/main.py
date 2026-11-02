from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Book Library API")


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


class Book(BookInput):
    id: int


books: dict[int, Book] = {
    1: Book(id=1, title="The Hobbit", author="J.R.R. Tolkien")
}
next_book_id = 2


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    # TODO: Return all books.
    raise NotImplementedError("Complete the list-books endpoint.")


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    # TODO: Return the requested book or raise HTTPException with status 404.
    raise NotImplementedError("Complete the get-book endpoint.")


@app.post(
    "/books",
    response_model=Book,
    status_code=status.HTTP_201_CREATED,
)
def create_book(book_input: BookInput) -> Book:
    global next_book_id

    # TODO: Create, store, and return a book using the next available ID.
    raise NotImplementedError("Complete the create-book endpoint.")


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput) -> Book:
    # TODO: Replace the book's title and author, preserving its ID.
    # Raise HTTPException with status 404 if the ID does not exist.
    raise NotImplementedError("Complete the update-book endpoint.")


@app.delete(
    "/books/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
)
def delete_book(book_id: int) -> Response:
    # TODO: Delete the requested book or raise HTTPException with status 404.
    raise NotImplementedError("Complete the delete-book endpoint.")
