from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
    }
]

@app.get("/books", summary="Get a list of books", tags=["Books"], response_model=list)
def get_books():
    return books

@app.get("/books/{book_id}", summary="Get a book by ID", tags=["Shelf"], response_model=dict)
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

class NewBook(BaseModel):
    id: int
    title: str
    author: str

@app.post("/books", summary="Add a new book", tags=["Books"], response_model=dict)
def add_book(book: NewBook):
    books.append({
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author,
    })
    return {"success": True}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)