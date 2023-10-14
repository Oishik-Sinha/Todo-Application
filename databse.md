# Data Persistence:
When implementing data persistence for the todo tasks using the Adjacency List Model in an RDBMS like MySQL, you can follow these guidelines:

### 1. Database Selection :
 - Choose MySQL as the database management system for your application.

### 2. Data Schema Design :
 - Design your table schema to accommodate the todo tasks.
 - Create a table with columns such as id, name, description, deadline, user, one_day_notification, createdAt, updatedAt to store the todo tasks.
 - The id column will serve as the primary key for each todo tasks.
 - The name column will hold the name of each todo tasks.
 - The user_id column will store the reference to the user's id associated with the task. 

### 3. Table Creation :
> __Warning__ &nbsp;&nbsp;&nbsp; We Don't need to do this as we using Django ORM (Object-Relational Mapping).

   <br/>For this Django ORM models look like 

   ```python
        class todoTaskList(models.Model):
            id = models.AutoField(auto_created=True, primary_key=True)
            name = models.CharField(max_length=500, null=False)
            description = models.CharField(max_length=5000)
            deadline = models.DateTimeField(null=False)
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            one_day_notification = models.BooleanField(default=False)
            createdAt = models.DateTimeField(auto_now_add=True)
            updatedAt = models.DateTimeField(auto_now=True)

            class Meta:
                db_table = "todo_task_list"
   ``` 

### 4. Retrieving Todo Tasks :
Implement queries or methods to retrieve nodes based on different criteria.
- To retrieve all nodes of the todo, 
  
  Django ORM models code look like this: <br/>
  ```python
  todoTaskList.objects.all()
  ```

  MySQL query might look like this: <br/>
  ```sql
  SELECT * FROM todo_task_list;
  ```

- To retrieve all child nodes of a particular user, 
  
  Django ORM models code look like this: <br/>
  ```python
  todoTaskList.objects.filter(user=<user_id>)
  # Example: Animals.objects.filter(parent=2)
  ```

  MySQL query might look like this: <br/>
  ```sql
  SELECT * FROM todo_task_list WHERE user_id = <user_id>;
  ```

By following these guidelines, you can implement data persistence for a todo tasks