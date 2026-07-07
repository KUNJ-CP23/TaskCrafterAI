# 🌸 TaskCrafterAI

TaskCrafterAI is an AI-powered web application that converts meeting notes into structured and actionable tasks using Google's Gemini AI.

The application extracts tasks, assigns owners, detects due dates, prioritizes work, and stores everything in a SQLite database for easy management.

---

## 🚀 Features

- 🤖 AI-powered task extraction using Gemini API
- 📋 Automatic task generation from meeting notes
- 💾 SQLite database integration
- ✏️ Edit existing tasks
- 🗑️ Delete tasks
- 🔍 Search tasks by owner or task name
- 📊 Dashboard statistics
- 🎨 Responsive Bootstrap UI

---

## 🛠 Tech Stack

- Python
- Flask
- Google Gemini API
- SQLite
- Bootstrap 5
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```
TaskCrafterAI
│
├── app.py
├── gemini.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
├── static/
└── screenshots/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/KUNJ-CP23/TaskCrafterAI.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root and add your Gemini API key:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

You can generate your API key from **Google AI Studio**.

Run the project

```bash
python app.py
```

---

## 📸 Screenshots

### Home Page

![Home](./screenshots/Home.png)

![Home2](./screenshots/Home2.png)

### Dashboard

![Dashboard](./screenshots/Dashboard.png)

### Edit Task

![Edit](./screenshots/Edit.png)

### Search

![Search](./screenshots/Search.png)

---


## 🏗️ Application Flow

Meeting Notes
      ↓
Google Gemini AI
      ↓
Structured JSON Tasks
      ↓
SQLite Database
      ↓
Task Dashboard
      ↓
Edit • Delete • Search • Statistics

## 🔮 Future Enhancements

- Task filtering
- Export to CSV
- User authentication
- Email notifications
- Multi-user support

---

## 👨‍💻 Author

**Kunj Ramoliya**

## 💬 Feedback & Contributions

Thank you for checking out **TaskCrafterAI**!

If you have any suggestions, ideas, or find any issues, feel free to:
- ⭐ Star this repository if you found it useful.
- 🐞 Open an issue to report bugs or suggest improvements.
- 🔀 Submit a pull request with enhancements or fixes.

Constructive feedback is always appreciated and will help improve this project.
