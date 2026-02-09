from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Testing my code to see if it triggers automatically"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
