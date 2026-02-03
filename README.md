# Library-Management-System
A simple Library Management System built using Streamlit and MongoDB Atlas.
The application allows managing books across different categories with support for bulk uploads and real-time updates.

This project was developed to understand how a lightweight frontend can interact with a cloud database and handle basic CRUD operations.



## Features:
1. Add new books with details like title, author, ISBN, quantity, and category
2. Categories supported:
  - Academic
  - Novel
  - Infotainment
3. View all books in an alphabetically sorted list
4. Filter books by category
5. Update available quantity of books
6. Delete books from the database
7. Upload multiple books at once using a CSV file
8. MongoDB Atlas used as a cloud database backend



## Screenshots:
<img width="1100" height="795" alt="image" src="https://github.com/user-attachments/assets/e9dcc984-db99-44b8-8315-7a6b655d995f" />
<img width="1060" height="771" alt="image" src="https://github.com/user-attachments/assets/f19273b2-219d-4920-9a84-b057308d2f5c" />



## Live Demo:
https://librarymanagementsystemlms.streamlit.app/



## Tech Stack:
Frontend: Streamlit (Python)  
Backend / Database: MongoDB Atlas  
Language: Python  
Hosting: Streamlit Community Cloud


## Project Structure:
Library-Management-System/  
│  
├── app.py           # Streamlit frontend  
├── database.py      # MongoDB connection & CRUD logic  
├── requirements.txt # Project dependencies  
└── README.md



## Working:
app.py handles the user interface and user interactions  
database.py contains all MongoDB-related logic (connection and CRUD operations)  
The frontend communicates with the database only through defined functions  
CSV upload allows bulk insertion instead of manual entry  



## CSV Upload Format:
title,author,isbn,quantity,category



## Environment Variables:
Mongo credentials are not hard-coded.  
The application reads the database connection string from MONGO_URI  
When deployed on Streamlit Cloud, this is configured using Streamlit Secrets.  



#### Author: Kamya Mehra
#### Published on February 2026


































