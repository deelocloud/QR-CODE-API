# Made by ProjectRexa
from flask import Flask,request,send_file
from flask_qrcode import QRcode
import re

app = Flask(__name__)

qrcode = QRcode(app)

@app.route('/')
def home():
    query = request.query_string
    query = query.decode('utf-8')
    query = query.replace("%20"," ")
    query = str(re.sub(r"[^a-zA-Zé,.-0123456789';:_()]", ' ', query))
    return send_file(qrcode(query, mode="raw"), mimetype="image/png")

    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
