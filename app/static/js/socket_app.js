const socket = io();

document.addEventListener('DOMContentLoaded', () => {
    refreshAnalytics();
});

function refreshAnalytics() {
    fetch('/api/stats')
        .then(response => response.json())
        .then(data => {
            document.getElementById('stat-total').innerText = data.total;
            document.getElementById('stat-completed').innerText = data.completed;
            document.getElementById('stat-pending').innerText = data.pending;
            document.getElementById('stat-percent').innerText = data.percentage + '%';
        })
        .catch(err => console.error("Analytics Error:", err));
}

// Add Task rest api
function submitTask() {
    const title = document.getElementById('taskTitle').value;
    const priority = document.getElementById('taskPriority').value;

    fetch('/api/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: title, priority: priority })
    })
    .then(response => {
        if(response.ok) {
            bootstrap.Modal.getInstance(document.getElementById('addTaskModal')).hide();
            document.getElementById('taskTitle').value = '';
            // backend emit automatically 
        }
    });
}

// delete task
function deleteTask(id) {
    if(confirm("Are you sure?")) {
        fetch(`/api/tasks/${id}`, { method: 'DELETE' });
    }
}

// complete task
function completeTask(id) {
    fetch(`/api/tasks/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status: 'Completed' })
    });
}

//websocket listner 
socket.on('task_updated', (data) => {
    console.log("Real-time Update:", data.message);
    
    // stats update 
    refreshAnalytics();
    
    //refresh dashbboard content 
    fetchTasksTable(); 
});

//table dynamically loader function
function fetchTasksTable() {
   
}
