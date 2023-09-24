
from flask import Flask , render_template
from housing.logger import logging
app = Flask(__name__, static_folder="static")


@app.route("/",methods = ['GET','POST'])
def index():
    logging.info("We are testing logging module")
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug = True)


# srinath