from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/ready")
def ready():
    return "I am ready!"

@application.route("/health")
def health():
    return "I am healthy!"

if __name__ == "__main__":
    application.run()
