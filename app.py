from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        n1 = float(request.form.get("n1", 0))
        n2 = float(request.form.get("n2", 0))
        result = n1 + n2
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
