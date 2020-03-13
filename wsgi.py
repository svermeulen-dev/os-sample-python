import socket
import datetine

from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    currentDT = datetime.datetime.now()
    currentDT_formatted = currentDT.strftime("%Y-%m-%d %H:%M:%S")
    return currentDT_formatted +": Hello World! This is a message from host: " + hostname + " (" + host_ip + ")"

@application.route("/ready")
def ready():
    return "I am ready!"

@application.route("/health")
def health():
    return "I am healthy!"

if __name__ == "__main__":
    application.run()
