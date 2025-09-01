from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory storage
entries = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "Anonymous")
        message = request.form.get("message", "")
        if message.strip():
            entries.append({"name": name, "message": message})
        return redirect("/")
    return render_template("index.html", entries=entries)

@app.route("/healthz")
def healthz():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
