from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from ..models import Task
import pandas as pd

analytics = Blueprint('analytics', __name__)

@analytics.route('/api/stats')
@login_required
def get_stats():
    # get the all task for user 
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    
    if not tasks:
        return jsonify({"total": 0, "completed": 0, "pending": 0, "percentage": 0})

    #create data frame 
    df = pd.DataFrame([t.to_dict() for t in tasks])

   
    total_tasks = len(df)
    completed_tasks = len(df[df['status'].str.strip().str.lower() == 'completed'])
    pending_tasks = total_tasks - completed_tasks
    
    success_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0

    
    print("data")
    print(f"User: {current_user.username} | Total: {total_tasks} | Done: {completed_tasks}")

    return jsonify({
        "total": int(total_tasks),
        "completed": int(completed_tasks),
        "pending": int(pending_tasks),
        "percentage": round(float(success_rate), 2)
    })