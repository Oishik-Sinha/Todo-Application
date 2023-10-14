# Python - Django

#### Before you get started, make sure you have Python 3.9 and mysql installed and configured correctly.

---

## Project Details
This Django project is a basic web application that incorporates the following features:

1. **_Django REST Framework_** : <br/>
 >  _The project utilizes the Django REST framework, which allows for the creation of powerful and flexible APIs. This framework provides a wide range of tools and functionalities for building RESTful services, such as serializers, viewsets, and authentication mechanisms._

2. **_Custom Middleware for Request Tracking_** : <br/>
 >  _A custom middleware named `ServiceMiddleware` (which you can find in the settings file of this project) has been implemented to track and log incoming requests. This middleware captures relevant information about each request, such as the requested URL, timestamp, user IP address. This tracking mechanism can be useful for monitoring and analyzing traffic patterns, debugging issues, and ensuring security._

3. **_Logging and Backup_** : <br/>
 >  _The project has a well-defined logging mechanism in place. Log files are created and organized based on the date, allowing for easy tracking and analysis of application events. This logging system ensures that critical information, warnings, and errors are properly recorded, aiding in troubleshooting and debugging efforts. Regular backups of logs are performed to ensure data integrity and prevent loss of valuable information._

4. **_Django ORM for Database Operations_** : <br/>
 >  _The project utilizes the Django ORM (Object-Relational Mapping) to handle database operations. The ORM provides a high-level abstraction for interacting with the database, allowing developers to define models and perform CRUD (Create, Read, Update, Delete) operations without writing raw SQL queries. The ORM simplifies the process of creating and maintaining database tables, managing relationships between models, and executing queries efficiently._

The combination of the Django REST framework, custom middleware for request tracking, robust logging with regular backups, and the Django ORM for managing database operations ensures the project's reliability, scalability, and maintainability.

---

## Setup
Follow these steps to set up and run the Django project:
### 1. Clone the project repository to your local machine.

### 2. Install project dependencies.
- Open your terminal and navigate to the project directory and run <br/>
  `pip install -r requirements.txt`

### 3. Configure the .env file.
- Navigate to the project directory. In the Project directory navigate to the folder `todoApplication` where you can find a file with the name `.env.rename`
- Rename the provided `.env.rename` file to `.env`.
- Open the `.env` file in a text editor and provide the necessary database credentials and informations. <br/>
  For example:
  ```env
  SECRET_KEY=your_secret_key
  DATABASE_ENGINE=django.db.backends.mysql  
  DATABASE_NAME=your_database_name
  DATABASE_USER=your_database_username
  DATABASE_PASSWORD=your_database_password
  DATABASE_HOST=your_database_host
  DATABASE_PORT=your_database_port
  ```
  ###### *Note: you can use different database engine, here mysql database is being used.*

### 4. Apply database migrations and initialize data.
- Open your terminal and navigate to the project directory and run the following commands one by one<br/>
  i. `python manage.py makemigrations` <br/>
  ii. `python manage.py migrate` <br/>

<br/><br/>
---
<br/>

## Running the Project
Once you have completed the setup process, you can now run the Django project. Open a terminal, navigate to the project directory, and run the following command: <br/>
`python manage.py runserver 8000`<br/>
###### *Note: Here the development server will start by using port 8000. You can change it as per your requirement.*
<br/>

This will start the development server, and you should see output similar to the following:<br/>
```cmd
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
<br/>

You can now access the Django project.<br/>

### Please follow the Api Documentation to Access the APIs
- Api_Documentation.md ( https://github.com/Oishik-Sinha/Todo-Application/blob/main/Api_Documentation.md )

---

## Additional Notes
- If you encounter any issues during the setup process or while running the project, please refer to the project's documentation.
- Make sure to keep the .env file secure and not include it in version control or share it with others. It contains sensitive information like database credentials.