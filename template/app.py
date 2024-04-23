
from flask import Flask # this is flask package

app=Flask(__name__)

@app.route('/')# default api view fuction
def home():
   return "welcome to Azure and flask web app"

@app.route('/s2s/api/signup')
def user_signup():
   return " this is user signup page"


if __name__=="__main__":
   app.run(debug=True)