Smart Task Manager with Real-Time Analytics

This is a Smart Task Manager web application that I built using Flask. The idea was to create something more than just a basic To-Do list. This app not only tracks your tasks but also gives you real-time updates and visual insights into your productivity using Pandas and WebSockets.

What this app does:

User Auth: Secure Login and Registration system (so your tasks stay yours).

Real-Time Updates: Used Flask-SocketIO so that whenever you add or complete a task, the dashboard updates instantly without needing a page refresh.

Data Analytics: Integrated Pandas on the backend to calculate total tasks, completion status, and your overall success rate on the fly.

Database: Powered by PostgreSQL to handle all user and task data reliably.

Tech Stack I used:

Backend: Python (Flask)

Analysis: Pandas, NumPy

Real-Time: Socket.io

Database: PostgreSQL / SQLAlchemy

Frontend: HTML5, CSS3 (Bootstrap), JavaScript

How to run
1 Clone the repo
git clone <repo link>
cd smart-task-manager

2 Set up a Virtual Environment
python -m venv venv
source venv/bin/activate

3 Install Dependencies
pip install -r requirements.txt

4 run
python run.py
