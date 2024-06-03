import mysql.connector

# Establishing the connection to MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="",  # Replace with your MySQL username
        password="",  # Replace with your MySQL password
        database="taskmanager"
    )

    cursor = conn.cursor()

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")
    exit(1)

# Function to add multiple new tasks
def add_tasks(tasks):
    try:
        sql = "INSERT INTO tasks (task_id, title, description, priority, status) VALUES (%s, %s, %s, %s, %s)"
        cursor.executemany(sql, tasks)
        conn.commit()
        print(f"{len(tasks)} tasks added successfully!")

    except mysql.connector.Error as err:
        print(f"Error adding tasks: {err}")

# Function to view all tasks
def view_tasks():
    try:
        cursor.execute("SELECT * FROM tasks")
        result = cursor.fetchall()
        for row in result:
            print(row)

    except mysql.connector.Error as err:
        print(f"Error viewing tasks: {err}")

# Function to update a task's details
def update_task(task_id, title, description, priority, status):
    try:
        sql = "UPDATE tasks SET title = %s, description = %s, priority = %s, status = %s WHERE task_id = %s"
        val = (title, description, priority, status, task_id)
        cursor.execute(sql, val)
        conn.commit()
        print(f"Task {task_id} updated successfully!")

    except mysql.connector.Error as err:
        print(f"Error updating task: {err}")

# Function to delete a task
def delete_task(task_id):
    try:
        sql = "DELETE FROM tasks WHERE task_id = %s"
        val = (task_id,)
        cursor.execute(sql, val)
        conn.commit()
        print(f"Task {task_id} deleted successfully!")

    except mysql.connector.Error as err:
        print(f"Error deleting task: {err}")

# Menu for the Task Management System
def menu():
    while True:
        print("\nTask Management System")
        print("1. Add tasks")
        print("2. View tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            tasks = []
            n = int(input("Enter number of tasks to add: "))
            for _ in range(n):
                task_id = input("Enter Task ID: ")
                title = input("Enter Title: ")
                description = input("Enter Description: ")
                priority = input("Enter Priority(High,Medium,Low): ")
                status = input("Enter Status(In Process,pending,Completed): ")
                tasks.append((task_id, title, description, priority, status))
            add_tasks(tasks)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = input("Enter Task ID to update: ")
            title = input("Enter new title: ")
            description = input("Enter new description: ")
            priority = input("Enter new priority(High,Medium,Low): ")
            status = input("Enter new status(In Process,pending,Completed): ")
            update_task(task_id, title, description, priority, status)
        elif choice == '4':
            task_id = input("Enter Task ID to delete: ")
            delete_task(task_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

# Run the menu
menu()

# Close the connection
conn.close()
