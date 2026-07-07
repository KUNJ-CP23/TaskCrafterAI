from gemini import extract_tasks
from dotenv import load_dotenv
import os
import json
from flask import Flask, render_template, request
from database import (
    create_table,
    save_tasks,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task,
    get_dashboard_stats,
    search_tasks
)

app = Flask(__name__)
#app.secret_key = "taskcrafterai_secret"

load_dotenv()

create_table()

@app.route("/")
def home():

    meeting_notes = request.args.get("notes", "")

    return render_template(
        "index.html",
        meeting_notes=meeting_notes
    )
    
@app.route("/generate", methods=["POST"])
def generate():
    meeting_notes = request.form["meeting_notes"]

    try:
        response = extract_tasks(meeting_notes)

    except Exception:

        return """
        <h2>⚠️ AI service is temporarily unavailable.</h2>

        <p>Please wait a few seconds and try again.</p>

        <br>

        <a href="/">← Back</a>
        """

    response = response.replace("```json", "").replace("```", "").strip()

    tasks = json.loads(response)
    
    save_tasks(tasks)
    
    tasks = get_all_tasks()

    stats = get_dashboard_stats()

    print(stats)
    return render_template(
        "dashboard.html",
        tasks=tasks,
        stats=stats,
        meeting_notes=meeting_notes
    )
    
@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):

    if request.method == "POST":

        update_task(
            task_id,
            request.form["task"],
            request.form["owner"],
            request.form["due_date"],
            request.form["priority"],
            request.form["status"]
        )

        tasks = get_all_tasks()

        stats = get_dashboard_stats()

        return render_template(
            "dashboard.html",
            tasks=tasks,
            stats=stats,
            meeting_notes=""
        )

    task = get_task_by_id(task_id)

    return render_template(
        "edit_task.html",
        task=task
    )
    
@app.route("/delete/<int:task_id>")
def delete(task_id):

    delete_task(task_id)

    tasks = get_all_tasks()

    stats = get_dashboard_stats()

    return render_template(
        "dashboard.html",
        tasks=tasks,
        stats=stats,
        meeting_notes=""
    )
    
@app.route("/search")
def search():

    query = request.args.get("query", "").strip()

    tasks = search_tasks(query)

    stats = get_dashboard_stats()

    return render_template(
        "dashboard.html",
        tasks=tasks,
        stats=stats,
        query=query,
        meeting_notes=""
    )
    
if __name__ == "__main__":
    app.run(debug=True)