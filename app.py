from flask import Flask, render_template, request

app = Flask(__name__)

messages = [
    "You are healing every day 🌱",
    "I am proud of you ❤️",
    "This pain is temporary, my love 💕",
    "You are never alone 🌍",
    "Rest today, rise stronger tomorrow 🌸"
]

@app.route("/", methods=["GET", "POST"])
def home():
    mood = None
    pain = None

    if request.method == "POST":
        mood = request.form.get("mood")
        pain = request.form.get("pain")

    return render_template(
        "index.html",
        message=messages[0],
        mood=mood,
        pain=pain
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
