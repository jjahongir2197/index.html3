from flask import Flask, render_template, request

app = Flask(__name__)

scores = []

@app.route("/", methods=["GET","POST"])
def average():

    if request.method == "POST":

        score = int(request.form["score"])
        scores.append(score)

        avg = sum(scores) / len(scores)

        return f"O‘rtacha: {avg}"

    return render_template("index.html")

app.run(debug=True)
