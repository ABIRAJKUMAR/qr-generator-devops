from flask import Flask, render_template, request
import qrcode
import base64
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    qr_code = None

    if request.method == "POST":
        text = request.form["text"]

        img = qrcode.make(text)
        buffer = BytesIO()
        img.save(buffer, format="PNG")

        qr_code = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return render_template("index.html", qr_code=qr_code)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)