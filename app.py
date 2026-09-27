from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# The "vault" password — 3 digits, deliberately weak on purpose for this exercise.
# Change this before you deploy, or read it from an environment variable.
VAULT_PASSWORD = os.environ.get("VAULT_PASSWORD", "482")

PAGE = """
<!DOCTYPE html>
<html>
<head><title>Vault Login</title></head>
<body style="font-family: sans-serif; max-width: 320px; margin: 80px auto; text-align:center;">
  <h2>Enter the Vault</h2>
  <form method="POST" action="/login">
    <input type="text" name="password" maxlength="3" pattern="\\d{3}" placeholder="000" required
           style="font-size:24px; text-align:center; width:100px; letter-spacing:8px;">
    <br><br>
    <button type="submit">Unlock</button>
  </form>
  {% if message %}<p>{{ message }}</p>{% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET"])
def index():
    return render_template_string(PAGE, message=None)


@app.route("/login", methods=["POST"])
def login():
    password = request.form.get("password", "")
    if password == VAULT_PASSWORD:
        return render_template_string(PAGE, message="Correct — vault unlocked."), 200
    return render_template_string(PAGE, message="Incorrect password."), 401


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # most free hosts inject PORT
    app.run(host="0.0.0.0", port=port)
