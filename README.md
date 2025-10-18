# Flask Todo App

A simple yet elegant Todo application built with Flask and SQLAlchemy that helps you manage your daily tasks effectively.

![Flask](https://img.shields.io/badge/Flask-2.3.3-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.23-green)
![Python](https://img.shields.io/badge/Python-3.x-yellow)

## 📝 Features

- **Create Tasks**: Quickly add new tasks with title and description
- **View Tasks**: See all your tasks in a clean, organized list
- **Update Tasks**: Modify existing tasks as your priorities change
- **Delete Tasks**: Remove completed or unnecessary tasks
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Modern UI**: Clean and intuitive user interface with Bootstrap and Font Awesome

## 📸 Screenshot

(Add a screenshot of your application here)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AayushSinghRajput/Todo-App.git
   cd Todo-App
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

## 🚀 Usage

### Standard Method

Run the application with:
```bash
python app.py
```

The app will be available at: http://127.0.0.1:8000/

### Development Mode with Auto-Reload

For development with automatic reloading on code changes:
```bash
python run_dev.py
```

This uses the Watchdog library to monitor file changes and automatically restart the Flask server.

## 📁 Project Structure

```
flask-tutorial/
│
├── app.py                 # Main application file
├── init_db.py             # Database initialization script
├── run_dev.py             # Development server with auto-reload
├── requirements.txt       # Project dependencies
│
├── db/                    # Database directory
│   └── todo.db            # SQLite database file
│
├── static/                # Static files (CSS, JS, images)
│
└── templates/             # HTML templates
    ├── about.html         # About page
    ├── base.html          # Base template with layout structure
    ├── index.html         # Homepage with todo list
    └── update.html        # Task update form
```

## 🧰 Technologies Used

- **Flask**: Web framework for Python
- **SQLAlchemy**: SQL toolkit and ORM
- **SQLite**: Database engine
- **Bootstrap**: Front-end framework for responsive design
- **Font Awesome**: Icon library
- **Watchdog**: File system monitoring for development auto-reload

## 📝 License

[MIT](LICENSE)

## 👤 Author

- [Aayush Singh Rajput](https://github.com/AayushSinghRajput)

---

## 💡 Future Improvements

- User authentication and personal todo lists
- Task categories and tags
- Due dates and reminders
- Task priority levels
- Task completion statistics
- Dark mode toggle

---

*Made with ❤️ using Flask*