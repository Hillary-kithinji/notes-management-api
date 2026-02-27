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

The API provides clear error messages and logging for easier debugging.



## HTTP Status Codes Reference Tested using Postman

The Notes Management System API uses proper HTTP status codes to communicate the result of requests.  

| Status Code | Name | When It Happens | Example Response |
|-------------|------|----------------|----------------|
| **200 OK** | Success | GET request or successful PUT/PATCH | `{ "id": 1, "title": "Note", "content": "Test" }` |
| **201 Created** | Resource Created | POST request successfully creates a new note | `{ "id": 2, "title": "New Note", "content": "Hello" }` |
| **204 No Content** | Success, no data | DELETE request successfully deletes a note | *No body* |
| **400 Bad Request** | Client error | Invalid data in POST/PUT | `{ "title": ["This field is required."] }` |
| **401 Unauthorized** | Authentication error | No token or invalid token | `{ "detail": "Authentication credentials were not provided." }` |
| **403 Forbidden** | Permission error | User tries to access another user's note | `{ "detail": "You do not have permission to perform this action." }` |
| **404 Not Found** | Resource not found | Note ID does not exist | `{ "detail": "Not found." }` |
| **405 Method Not Allowed** | Wrong HTTP method | POST to a GET-only endpoint | `{ "detail": "Method “POST” not allowed." }` |
| **500 Internal Server Error** | Server-side error | Unexpected backend error | `{ "detail": "Internal server error." }` |


## Future Improvements

- Deployment – Production-ready hosting (Heroku, AWS, etc.)  
- Pagination – Limit notes per request  
- Search & filtering – Search notes by keywords  
- Advanced authentication – JWT or OAuth  
- Attachments – Support file uploads in notes
  
##Testing
**All endpoints have been tested using Postman.**
