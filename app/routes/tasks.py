from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from ..models import Task
from .. import db, socketio

tasks = Blueprint('tasks', __name__)

# dashboard
@tasks.route('/')
@login_required
def dashboard():
    # fetch the all task from db
    user_tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', tasks=user_tasks)

# api

# add task
@tasks.route('/api/tasks', methods=['POST'])
@login_required
def add_task():
    data = request.get_json()
    
    new_task = Task(
        title=data.get('title'),
        description=data.get('description'),
        priority=data.get('priority', 'Medium'),
        status='Pending',
        user_id=current_user.id
    )
    
    db.session.add(new_task)
    db.session.commit()
    
    # WebSocket: Sagle users (kinva specific user) la update pathva
    socketio.emit('task_updated', {'message': 'New task added!', 'task': new_task.to_dict()})
    
    return jsonify({"message": "Task added successfully", "task": new_task.to_dict()}), 201

# update task
@tasks.route('/api/tasks/<int:id>', methods=['PUT'])
@login_required
def update_task(id):
    task = Task.query.get_or_404(id)
    
    # if check this task is real user 
    if task.user_id != current_user.id:
        return jsonify({"error": "Unauthorized"}), 403
        
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.priority = data.get('priority', task.priority)
    task.status = data.get('status', task.status)
    
    db.session.commit()
    
    # main websocket transfer the real data into db 
    socketio.emit('task_updated', {'message': 'Task updated!', 'task': task.to_dict()})
    
    return jsonify({"message": "Task updated successfully"})

# delete task
@tasks.route('/api/tasks/<int:id>', methods=['DELETE'])
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    
    if task.user_id != current_user.id:
        return jsonify({"error": "Unauthorized"}), 403
        
    db.session.delete(task)
    db.session.commit()
    
    # websockert 
    socketio.emit('task_updated', {'message': 'Task deleted', 'task_id': id})
    
    return jsonify({"message": "Task deleted successfully"})

#optional call for AJAx call
@tasks.route('/api/tasks', methods=['GET'])
@login_required
def get_tasks():
    user_tasks = Task.query.filter_by(user_id=current_user.id).all()
    return jsonify([task.to_dict() for task in user_tasks])