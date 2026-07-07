import sqlite3

DATABASE_NAME = "tasks.db"


def get_connection():

    connection = sqlite3.connect(DATABASE_NAME)

    connection.row_factory = sqlite3.Row

    return connection

#gave the schema
def create_table():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            task TEXT NOT NULL,

            owner TEXT,

            due_date TEXT,

            priority TEXT,

            status TEXT DEFAULT 'Pending'

        )
    """)

    connection.commit()

    connection.close()
    
    
def save_tasks(tasks):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("DELETE FROM tasks")

    for task in tasks:

        cursor.execute("""
            INSERT INTO tasks
            (task, owner, due_date, priority, status)

            VALUES (?, ?, ?, ?, ?)
        """,
        (
            task["task"],
            task["owner"],
            task["due_date"],
            task["priority"],
            "Pending"
        ))

    connection.commit()

    connection.close()
    
def get_all_tasks():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM tasks
        ORDER BY id
    """)

    tasks = cursor.fetchall()

    connection.close()

    return tasks

def get_task_by_id(task_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    task = cursor.fetchone()

    connection.close()

    return task

def update_task(task_id, task, owner, due_date, priority, status):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tasks

        SET
            task = ?,
            owner = ?,
            due_date = ?,
            priority = ?,
            status = ?

        WHERE id = ?
    """,
    (
        task,
        owner,
        due_date,
        priority,
        status,
        task_id
    ))

    connection.commit()

    connection.close()
    
def delete_task(task_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()

    connection.close()
    
def get_dashboard_stats():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM tasks")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tasks WHERE status='Pending'")
    pending = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tasks WHERE status='Completed'")
    completed = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tasks WHERE priority='High'")
    high = cursor.fetchone()[0]

    connection.close()

    return {
        "total": total,
        "pending": pending,
        "completed": completed,
        "high": high
    }
    
def search_tasks(query):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM tasks
        WHERE task LIKE ?
        OR owner LIKE ?
        ORDER BY id
    """,
    (
        f"%{query}%",
        f"%{query}%"
    ))

    tasks = cursor.fetchall()

    connection.close()

    return tasks