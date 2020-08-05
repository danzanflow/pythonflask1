from flask import Flask, render_template

app = Flask(__name__)

app = Flask(__name__, static_url_path='/static')

# Creating simple Routes 
@app.route('/test')
def test():
    return "Home Page"

@app.route('/test/about/')
def about_test():
    return "About Page"

@app.route('/test/blog/')
def blog_test():
    return "Blog"

@app.route('/test/services')
def services_test():
    return "Services"

# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

@app.route('/blog', strict_slashes=False)
def blog():
    return render_template("blog.html")

@app.route('/services', strict_slashes=False)
def services():
    return render_template("services.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)