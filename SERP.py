from flask import Flask

SERP = Flask(__name__)

@SERP.route('/')
def index(): 
    return('This is index')



if __name__=="__name__":
        SERP.run(debug=True)