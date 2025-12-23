from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    if request.method == "POST":
        time.sleep(1.5)
        nama = request.form.get("nama")
        hasil = f"> HALLO :: {nama}"
    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
