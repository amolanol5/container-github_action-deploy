from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    print("This app is from flask")
    return "<p>This app is from flask</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080" , debug=False)