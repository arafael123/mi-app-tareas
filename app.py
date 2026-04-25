from flask import Flask, request, jsonify, render_template
from database import init_db, get_connection


app = Flask(__name__)
init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()

    return jsonify([
        {"id": t[0], "title": t[1], "completed": bool(t[2])}
        for t in tasks
    ])


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    conn = get_connection()
    conn.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (data["title"],)
    )
    conn.commit()
    conn.close()

    return {"message": "Task created"}, 201


@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    conn = get_connection()
    conn.execute(
        "UPDATE tasks SET completed = 1 WHERE id = ?",
        (id,)
    )
    conn.commit()
    conn.close()

    return {"message": "Task updated"}


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    conn = get_connection()
    conn.execute(
        "DELETE FROM tasks WHERE id = ?",
        (id,)
    )
    conn.commit()
    conn.close()

    return {"message": "Task deleted"}


if __name__ == "__main__":
    app.run(debug=True)