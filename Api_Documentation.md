# Todo Application - Api Documentation

**API Documentation for Todo-Task Management Service**

## POST  -  **Login a User**

- **Endpoint:** `http://localhost:8000/user/login`
- **Description:** This endpoint allows users to log in and obtain an authentication token.
- **Request:**
  - `username` (string) - User's username
  - `password` (string) - User's password
    
- **Response:**
  - `refreshToken` (string) - Authentication refresh token
  - `accessToken` (string) - Authentication access token
    
- **Example Request:**
  ```json
  POST      http://localhost:8000/user/login
  body = {
    "password": "Demo@4321",
    "username": "demo@gmail.com"
  }
  ```
- **Example Response:**
  ```json
  {
    "error-message": "",
    "results": {
        "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NzM3ODIzNSwiaWF0IjoxNjk3MjkxODM1LCJqdGkiOiI5ZGVlZDljYzNmOWI0YzIxYTBmYWVjMjM4ODViOTNiYiIsInVzZXJfaWQiOjQsImF1ZCI6IlRvZG9Vc2VyIiwiaXNzIjoiT2lzaGlrIn0.BlfAlAO3Ze89x38I4CTJB9VwikBqmsRZj6ZGn2D8w04",
        "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3Mzc0NjM1LCJpYXQiOjE2OTcyOTE4MzUsImp0aSI6IjI5ZDRlYjMwMWM1OTQ1NTZhZTk2YjhiZjg4NzliYzJlIiwidXNlcl9pZCI6NCwiYXVkIjoiVG9kb1VzZXIiLCJpc3MiOiJPaXNoaWsifQ.wQyG-21z8vybiMblToGbGAujGthz_19Mwq1YXtyAqBw"
    }
  }
  ```

<br/>

## POST  -  **Register A New User**

- **Endpoint:** `http://localhost:8000/user/register`
- **Description:** This endpoint allows users to register a new account.
- **Request:**
  - `username` (string) - User's desired username
  - `password` (string) - User's desired password
  - `confirm_password` (string) - confirm password
  - `first_name` (string) - User's desired first name
  - `last_name` (string) - User's desired last name
  - `email` (string) - User's email i'd
    
- **Response:**
  - `results` (string) - A confirmation message
 
- **Example Request:**
  ```json
  POST     http://localhost:8000/user/register
  body = {
    "password": "Demo@4321",
    "confirm_password": "Demo@4321",
    "username": "demo6@demo.com",
    "first_name": "demo1",
    "last_name": "demo1",
    "email": "demo6@demo.com"
  }
  ```
  
- **Example Response:**
  ```json
  {
    "error-message": "",
    "results": "You have registered successfully. Please Login!"
  }
  ```
<br/>

## POST  -  **Create New Todo Task**

- **Endpoint:** `http://localhost:8000/todo/todo-list`
- **Description:** This endpoint allows users to create a new task.

- **Request: headers**
  - `Authorization` (string) - Access token
    
- **Request: body**
  - `name` (string) - Task title
  - `description` (string) - Task description
  - `deadline` (string) - Task deadline
    
- **Response:**
  - `result` (object) - Created success message
    
- **Example Request:**
  ```json
  POST    http://localhost:8000/todo/todo-list
  headers = {
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3Mzc0NjM1LCJpYXQiOjE2OTcyOTE4MzUsImp0aSI6IjI5ZDRlYjMwMWM1OTQ1NTZhZTk2YjhiZjg4NzliYzJlIiwidXNlcl9pZCI6NCwiYXVkIjoiVG9kb1VzZXIiLCJpc3MiOiJPaXNoaWsifQ.wQyG-21z8vybiMblToGbGAujGthz_19Mwq1YXtyAqBw"
  }
  
  body = {
    "name":"assignment submit",
    "description":"submit assignment",
    "deadline" : "2023-03-13 18:25:00"
  }
  ```
  
- **Example Response:**
  ```json
  {
    "error-message": "",
    "results": "Todo Task Created Successfully!"
  }
  ```
<br/>

## GET  -  **Get All Todo Task List For A User**

- **Endpoint:** `http://localhost:8000/todo/todo-list`
- **Description:** This endpoint retrieves a list of all tasks of the logged-in User.
  
- **Request: headers**
  - `Authorization` (string) - Access token
    
- **Response:**
  - `results` (array of objects) - List of tasks
    
- **Example Request:**
  ```json
  GET     http://localhost:8000/todo/todo-list
  headers = {
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3Mzc0NjM1LCJpYXQiOjE2OTcyOTE4MzUsImp0aSI6IjI5ZDRlYjMwMWM1OTQ1NTZhZTk2YjhiZjg4NzliYzJlIiwidXNlcl9pZCI6NCwiYXVkIjoiVG9kb1VzZXIiLCJpc3MiOiJPaXNoaWsifQ.wQyG-21z8vybiMblToGbGAujGthz_19Mwq1YXtyAqBw"
  }
  ```
  
- **Example Response:**
  ```json
  {
    "error-message": "",
    "results": [
        {
            "createdAt": "2023-10-14 17:16:23.988763+00:00",
            "deadline": "2023-03-13 12:55:00+00:00",
            "description": "submit assignment",
            "id": 10,
            "name": "assignment submit",
            "one_day_notification": false,
            "updatedAt": "2023-10-14 17:16:23.988763+00:00",
            "user_id": 4
        }
    ]
  }
  ```
 <br/>

## PUT  -  **Update a Existing Todo Task**

- **Endpoint:** `http://localhost:8000/todo/todo-list`
- **Description:** This endpoint allows users to update the details of a specific task.
  
- **Request: headers**
  - `Authorization` (string) - Access token
    
- **Request: body**
  - `todo_id` (string) - Task id
  - `name` (string) - Task title
  - `description` (string) - Task description
  - `deadline` (string) - Task deadline
    
- **Response:**
  - `results` (object) - Updated success message
    
- **Example Request:**
  ```json
  PUT      http://localhost:8000/todo/todo-list
  headers = {
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3Mzc0NjM1LCJpYXQiOjE2OTcyOTE4MzUsImp0aSI6IjI5ZDRlYjMwMWM1OTQ1NTZhZTk2YjhiZjg4NzliYzJlIiwidXNlcl9pZCI6NCwiYXVkIjoiVG9kb1VzZXIiLCJpc3MiOiJPaXNoaWsifQ.wQyG-21z8vybiMblToGbGAujGthz_19Mwq1YXtyAqBw"
  }
  
  body = {
    "todo_id": 10,
    "name":"assignment",
    "description":"submit  all assignment",
    "deadline" : "2023-03-13 18:25:00"
  }
  ```

- **Example Response:**
  ```json
  {
    "error-message": "",
    "results": "Todo Task Update Successfully!"
  }
  ```
<br/>

## DELETE  -  **Delete a Existing Todo Task**

- **Endpoint:** `http://localhost:8000/todo/todo-list`
- **Description:** This endpoint allows users to delete a specific task.
  
- **Request: headers**
  - `Authorization` (string) - Access token
    
- **Request: body**
  - `todo_id` (string) - Task id
    
- **Response:**
  - `results` (object) - Updated success message
    
- **Example Request:**
  ```json
  DELETE     http://localhost:8000/todo/todo-list
  headers = {
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3Mzc0NjM1LCJpYXQiOjE2OTcyOTE4MzUsImp0aSI6IjI5ZDRlYjMwMWM1OTQ1NTZhZTk2YjhiZjg4NzliYzJlIiwidXNlcl9pZCI6NCwiYXVkIjoiVG9kb1VzZXIiLCJpc3MiOiJPaXNoaWsifQ.wQyG-21z8vybiMblToGbGAujGthz_19Mwq1YXtyAqBw"
  }
  
  body = {
    "todo_id": 5
  }
  ```
  
- **Example Response:**
  ```json
  {
    "error-message": "",
    "results": "Todo Task Deleted Successfully!"
  }
  ```
