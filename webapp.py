from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""
    if request.method == "POST":
        idea = request.form.get("idea")

        if request.form.get("action") == "analyze":
            output = f"""
Analyze this software project idea:

{idea}

Give:
- Tech stack
- Difficulty level
- Resume impact
- Improvements
"""
        else:
            output = f"""
Evaluate this project idea honestly:

{idea}

Give:
- Originality score (1-10)
- Market saturation
- Risks
- Unique twist suggestions
"""

    return render_template("index.html", output=output, show_hint=bool(output))


if __name__ == "__main__":
    app.run(debug=True)
