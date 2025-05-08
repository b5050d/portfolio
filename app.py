from flask import Flask, render_template

app = Flask(__name__)
from home_objects import educations
from skills import skill_categories

@app.route('/')
def home():
    return render_template('home.html', educations=educations, skill_categories=skill_categories)

@app.route('/projects')
def projects():
    return render_template('projects.html')
    # return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
