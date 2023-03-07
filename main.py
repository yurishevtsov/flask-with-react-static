from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")

def my_index():
    return render_template("index.html", flask_token="Hello there!")
    
app.run(host='0.0.0.0', debug=True)