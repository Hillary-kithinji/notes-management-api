# Notes Management System API

A simple and secure **Notes Management System API** built with Django and Django REST Framework.  
This API allows users to create, view, update, and delete personal notes. Each note is private to the user who created it.

---

## Features

- **User registration & authentication**  
- **Create notes**  
- **View all notes for a user**  
- **Update & delete notes**  
- **Secure access** – users can only access their own notes  

---
## Tech Stack

- Python 3.12.3
- Django  
- Django REST Framework  
- SQLite (default) or other relational databases

##Authentication
- Token-based authentication

  

## Database Structure
Each note has the following fields:

- `id` – Unique note ID  
- `user` – Owner of the note  
- `title` – Note title  
- `content` – Note body  
- `created_at` – Timestamp of creation  
- `updated_at` – Timestamp of last update


  
## Notes Endpoints

| Method | Endpoint            | Description |
|--------|------------------|-------------|
| GET    | `/api/notes/`      | Get all notes for the logged-in user |
| POST   | `/api/notes/`      | Create a new note (`title` and `content`) |
| GET    | `/api/notes/<id>/` | Retrieve a specific note |
| PUT    | `/api/notes/<id>/` | Update a note (title/content) |
| DELETE | `/api/notes/<id>/` | Delete a note |

> Users can only access their own notes.
>   
## Future Improvements

- Deployment – Production-ready hosting (Heroku, AWS, etc.)  
- Pagination – Limit notes per request  
- Search & filtering – Search notes by keywords  
- Advanced authentication – JWT or OAuth  
- Attachments – Support file uploads in notes
  
##Testing
**All endpoints have been tested using Postman.**
