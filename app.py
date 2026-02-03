import streamlit as st
from database import add_book, get_all_books, update_book, delete_book

st.set_page_config(page_title="Library Management System", layout="centered")

st.title("LIBRARY MANAGEMENT SYSTEM")

# ADD BOOK

st.subheader("Add New Book")

title = st.text_input("Book Title")
author = st.text_input("Author")
isbn = st.text_input("ISBN")
quantity = st.number_input("Quantity", min_value=1, step=1)
category = st.selectbox(
    "Category",
    ["Academic", "Novel", "Infotainment"]
)

# add_book(title, author, isbn, quantity, category)

if st.button("Add Book"):
    if title and author and isbn and category:
        add_book(title, author, isbn, quantity, category)
        st.success("Book added successfully!")
        st.rerun()
    else:
        st.error("All fields are required")

import csv
from database import add_books_bulk

st.divider()
st.subheader("Upload Books Database via CSV")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    decoded_file = uploaded_file.read().decode("utf-8").splitlines()
    reader = csv.DictReader(decoded_file)

    books = []
    for row in reader:
        books.append({
            "title": row["title"].strip(),
            "author": row["author"].strip(),
            "isbn": str(row["isbn"]).strip(),
            "quantity": int(row["quantity"]),
            "category": row["category"].strip()
        })

    if st.button("Upload Books"):
        add_books_bulk(books)
        st.success(f" {len(books)} books uploaded successfully!")
        st.rerun()
st.divider()

# VIEW / UPDATE / DELETE BOOKS

st.subheader("Available Books")

filter_category = st.selectbox(
    "Filter by Category",
    ["All", "Academic", "Novel", "Infotainment"]
)

books = get_all_books()

if filter_category != "All":
    books = [b for b in books if b["category"] == filter_category]


if books:
    for book in books:
        st.write(
            f"**{book['title']}** by {book['author']}    \n"
            f"Category: `{book['category']}` |  ISBN: `{book['isbn']}`    \n  Quantity: `{book['quantity']}`"
        )


        col1, col2 = st.columns(2)

        with col1:
            new_qty = st.number_input(
                "Update Quantity",
                min_value=0,
                value=book["quantity"],
                key="qty" + book["_id"]
            )
            if st.button("Update", key="upd" + book["_id"]):
                update_book(book["_id"], new_qty)
                st.rerun()

        with col2:
            if st.button("Delete", key="del" + book["_id"]):
                delete_book(book["_id"])
                st.rerun()
else:
    st.info("No books available")


