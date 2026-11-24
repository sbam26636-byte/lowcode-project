
from flask import Flask, request, jsonify
import re
import secrets
from datetime import datetime, timezone

app = Flask(__name__)

_seen = {}


@app.route("/")
def home():
    return "<h1>Hello from Marcela</h1>"

@app.route("/about")
def about():
    return """
    <h1>What I would build in one evening</h1>
    <p>If I could build an application in one evening instead of a quarter, I would create a simple personal learning planner. The application would help students organise their studies, set goals, and track their progress. Users could add tasks, choose deadlines, and mark activities as completed. It would also show a daily checklist and a weekly progress summary.</p>
    <p>I would start with a basic version using Python and Flask, with a simple web interface. I would use AI tools such as ChatGPT to help me understand the code, identify errors, and develop new features. I would test the application with a few real tasks and improve it based on the results.</p>
    <p>My goal would not be to create a perfect product in one evening. Instead, I would focus on solving one small, useful problem. This approach would help me learn by doing, gain confidence in programming, and understand how an idea can become a working application.</p>
    """

@app.post("/hooks/signup")
def signup_hook():
    if not request.is_json:
        return jsonify({"error": "JSON required"}), 415

    data = request.get_json()

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400
    name = data.get("name")
    email = data.get("email")
    company = data.get("company")
    if not all(isinstance(value, str) and value.strip() for value in (name, email, company)):
        return jsonify({"error": "Name, email and company are required"}), 400
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email.strip()):
        return jsonify({"error": "Invalid email address"}), 400
    key = f"{email.strip().lower()}|{company.strip().lower()}"
    if key in _seen:
        return jsonify({"status": "success", "reference": _seen[key]}), 200
    reference = f"CB-{datetime.now(timezone.utc):%Y%m%d}-{secrets.randbelow(10000):04d}"
    _seen[key] = reference
    return jsonify({"status": "success", "reference": reference}), 200    
if __name__ == "__main__":
    app.run(port=5001, debug=False)
