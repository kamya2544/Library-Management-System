from pymongo import MongoClient
from bson.objectid import ObjectId

# MongoDB Connection

MONGO_URI = "mongodb+srv://user:pswd@cluster0.xxxx.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["library_db"]
collection = db["books"]


# BOOK CRUD OPERATIONS

def add_book(title, author, isbn, quantity, category):
    book = {
        "title": title.strip(),
        "author": author.strip(),
        "isbn": str(isbn).strip(),
        "quantity": quantity,
        "category": category
    }
    collection.insert_one(book)

def get_all_books():
    books = []
    for book in collection.find().sort("title", 1):  
        book["_id"] = str(book["_id"])
        books.append(book)
    return books

def update_book(book_id, quantity):
    collection.update_one(
        {"_id": ObjectId(book_id)},
        {"$set": {"quantity": quantity}}
    )

def delete_book(book_id):
    collection.delete_one({"_id": ObjectId(book_id)})
        
def add_books_bulk(books):
    collection.insert_many(books)

##collection.delete_many({})

##print("✅ All books deleted")
