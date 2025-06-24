from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify(status="ok", service="2")

@app.route("/hello")
def hello():
    return jsonify(message="Hello from Service 2 Python")

@app.route("/health")
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    print("Service 2 running on port 8002...")
    app.run(host="0.0.0.0", port=8002)
