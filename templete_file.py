from flask import Flask, redirect, url_for, render_template
### render_template: grab a html file and render that as a web page
app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index.html",content = name,r=2, cont =['tim','joe','bill'])




if __name__ == '__main__':
    app.run()