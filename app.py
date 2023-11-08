from flask import Flask
from mushroom.logger import logging

app = Flask(__name__)

logging.info("Log file testing")
@app.route('/',methods=["GET","POST"])
def home():
    logging.info("Successfully Tested.")
    return "Home Page"

if __name__ == "__main__":
    app.run('0.0.0.0')