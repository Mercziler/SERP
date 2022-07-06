from flask import Flask, render_template

SERP = Flask(__name__)

@SERP.route('/')
def index(): 
    return render_template("index.html")



if __name__=="__name__":
        SERP.run(debug=True)