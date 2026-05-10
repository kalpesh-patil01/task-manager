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

// 2. Add Task (REST API)
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
            // socket.emit karnyachi garaj nahi, backend 'emit' karel.
        }
    });
}

// 3. Delete Task
function deleteTask(id) {
    if(confirm("Are you sure?")) {
        fetch(`/api/tasks/${id}`, { method: 'DELETE' });
    }
}

// 4. Complete Task
function completeTask(id) {
    fetch(`/api/tasks/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status: 'Completed' })
    });
}

// ==========================================
// WEBSOCKET LISTENERS
// ==========================================

socket.on('task_updated', (data) => {
    console.log("Real-time Update:", data.message);
    
    // 1. Stats update kara
    refreshAnalytics();
    
    // 2. Page reload na karta fakt table refresh karaycha asel tar:
    // Pan tula jar table code lihaycha nase tar reload thevle tari chalel.
    // location.reload(); 
    
    // Dashboard var aslelya table la refresh karnya sathi he vapru shakto:
    fetchTasksTable(); 
});

// Table dynamically load karnyacha function (Optional)
function fetchTasksTable() {
    // Jar tu dashboard page var asashil tar hya function mule page reload na karta
    // fakt table cha part refresh hou shakto (AJAX vaprun)
    // Sadhyasathi location.reload() pan chalel.
}