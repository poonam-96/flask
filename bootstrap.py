# inherit the template so that we donnot have to repeat it again 
from flask import Flask, redirect,url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("child.html", content="Testing")

if __name__ == '__main__':
    app.run(debug = True) # do not rerun the server. sutomaticlly done

