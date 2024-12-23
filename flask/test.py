from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Manage Page
@app.route('/manage')
def manage():
    return render_template('manage.html')

if __name__ == '__main__':
    app.run(debug=True)
