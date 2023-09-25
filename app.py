
from flask import Flask , render_template
import sys
from housing.logger import logging
from housing.exception import HousingException
app = Flask(__name__, static_folder="static")


@app.route("/",methods = ['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom Exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug = True)


# srinath