from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

task_store = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/timer")
def timer():
    return render_template("timer.html")


@app.route("/checklist")
def checklist():
    return render_template("checklist.html")


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(task_store)


@app.route("/api/tasks", methods=["POST"])
def save_tasks():
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"status": "error", "message": "Invalid data"}), 400
    task_store.clear()
    task_store.update(data)
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)