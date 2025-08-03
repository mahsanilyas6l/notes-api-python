# 📝 Notes API (Flask CRUD App)

## 🔥 Description:
This is a simple Flask-based backend app that provides a CRUD API to create, read, update, and delete notes.

## 📦 Features:
- GET /notes — View all notes  
- GET /notes/<id> — View a single note by ID  
- POST /notes — Create a new note  
- PUT /notes/<id> — Update an existing note  
- DELETE /notes/<id> — Delete a note  

## 🚀 Installation Guide:

1. Make sure Python is installed (version 3.10 or above is recommended)

2. Install Flask:

bash
pip install flask

	3.	Run the app:

python app.py

The API will be available at:
http://127.0.0.1:5000

⸻

📬 API Testing:

Use tools like Postman or Thunder Client in VS Code to test the following API endpoints:

🟢 Create Note (POST)

POST /notes
Content-Type: application/json

{
  "title": "Sample Note",
  "content": "This is a test note"
}

🔵 Read All Notes (GET)

GET /notes

🔵 Read Single Note (GET)

GET /notes/1

🟡 Update Note (PUT)

PUT /notes/1
Content-Type: application/json

{
  "title": "Updated Title",
  "content": "Updated content"
}

🔴 Delete Note (DELETE)

DELETE /notes/1

---

✅ Copy and paste this into your `README.md` file in VS Code or any text editor, then save and commit it with:

bash
git add README.md
git commit -m "Add API documentation to README"
git push