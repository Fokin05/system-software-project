from flask import Flask, request, render_template_string

app = Flask(__name__)
tasks = []

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>System Software - ToDo List</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
        .container { max-width: 600px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; text-align: center; }
        .form { display: flex; margin-bottom: 20px; }
        input[type="text"] { flex: 1; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }
        button { padding: 10px 20px; background: #007cba; color: white; border: none; border-radius: 5px; cursor: pointer; margin-left: 10px; }
        .task { padding: 10px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; }
        .task:last-child { border-bottom: none; }
        .delete { color: red; cursor: pointer; }
        .info { background: #e7f3ff; padding: 10px; border-radius: 5px; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>✅ To-Do List</h1>
        <p><strong>System Software Project</strong></p>
        
        <form method="POST" class="form">
            <input type="text" name="task" placeholder="Введите новую задачу..." required>
            <button type="submit">Добавить</button>
        </form>

        <div class="tasks">
            {% if tasks %}
                {% for task in tasks %}
                    <div class="task">
                        <span>{{ task }}</span>
                        <a href="/delete/{{ loop.index0 }}" class="delete">❌ Удалить</a>
                    </div>
                {% endfor %}
            {% else %}
                <p>Нет задач. Добавьте первую задачу!</p>
            {% endif %}
        </div>

        <div class="info">
            <p><strong>Статус:</strong> 🟢 Приложение работает</p>
            <p><strong>Всего задач:</strong> {{ tasks|length }}</p>
        </div>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('task')
        if task and task not in tasks:
            tasks.append(task)
    return render_template_string(HTML_TEMPLATE, tasks=tasks)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return render_template_string(HTML_TEMPLATE, tasks=tasks)

@app.route('/health')
def health():
    return {
        "status": "healthy", 
        "service": "todo-app",
        "task_count": len(tasks)
    }

@app.route('/info')
def info():
    return {
        "app_name": "System Software ToDo List",
        "version": "1.0",
        "total_tasks": len(tasks)
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
