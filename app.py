from flask import Flask, render_template

from home_objects import educations
from projects import my_projects
from skills import skill_categories
from work_experiences import work_experiences

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "home.html",
        educations=educations,
        skill_categories=skill_categories,
        work_experiences=work_experiences,
    )


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=my_projects)
    # return "Hello World"


@app.route("/project/<int:project_id>")
def project_page(project_id):
    project = my_projects[project_id]
    return render_template("project_page.html", project=project)


if __name__ == "__main__":
    app.run(debug=True)
