from flask import Flask
from mushroom.logger import logging
import sys
from mushroom.exception import CustomException

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
    try:
        raise Exception("Testing Custom Exception.")
    except Exception as e:
        error = CustomException(e, sys)
        logging.info(error)

    return "Home Page"

if __name__ == "__main__":
    app.run('0.0.0.0')