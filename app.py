from flask import Flask, redirect, url_for

app = Flask(__name__)  # instance of flask application


# define how to acess specific page(eg: home page)
@app.route("/") # path we want to use to get to the function(/ : go to default home page)
# create page
def home():
    return "Hello Welcome <h1>HELLO</h1>"

# create another page
@app.route("/<name>")  # here in the thing what i write inside will be passed as a parameter to below user function
def user(name):  # redirect us directly to home page
    return f'HELLO {name}!'

@app.route("/admin")
def admin():
    return redirect(url_for("home")) 

# redirect pages :
if __name__=="__main__":
    app.run()
