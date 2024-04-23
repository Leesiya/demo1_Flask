
from flask import Flask , render_template # this is flask package

app=Flask(__name__)

@app.route('/')
def home():
   return render_template("home.html")

@app.route('/s2s/api/signup')
def user_signup():
   return " this is user signup page"

@app.route('/s2s/api/login')
def user_login():
   return "this is my login page"

@app.route('/s2s/api/about')
def off_about():
   return render_template("about.html")

@app.route('/s2s/api/blog')
def off_blob():
   return " It's a blob storage"

@app.route('/s2s/api/contact')
def con_us():
   return " contact us"

if __name__=="__main__":
   app.run(debug=True)