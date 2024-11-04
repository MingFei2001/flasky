from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)

# Route for each pages
# TODO: move this out into another file
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/template')
def template():
    return render_template("template.html")

# Only run if this file not used as a lib
if __name__ == "__main__":
    app.run(debug=True)
