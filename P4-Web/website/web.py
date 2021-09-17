from flask import Flask
from flask.templating import render_template  # import class object

app = Flask(__name__) # get the value of name of the python script

@app.route('/') 
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__": # python assign "__main__" to this script
    app.run(debug=True)