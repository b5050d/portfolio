from flask import Flask, render_template

app = Flask(__name__)
from home_objects import educations
from skills import skill_categories
from work_experiences import work_experiences
from projects import projects

@app.route('/')
def home():
    return render_template(
        'home.html',
        educations=educations,
        skill_categories=skill_categories,
        work_experiences=work_experiences,
        )

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=projects)
    # return "Hello World"


@app.route('/project/<int:project_id>')
def project_page(project_id):
    project = projects[project_id - 1]
    return render_template('project_page.html', project=project)

if __name__ == '__main__':
    app.run(debug=True)
