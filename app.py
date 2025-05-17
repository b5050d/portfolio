from flask import (
    Flask,
    render_template,
    request,
    make_response,
    render_template_string,
    # session,
)

import os

from home_objects import educations
from project_objects import my_projects
from skills import skill_categories
from work_experiences import work_experiences
from cookies_objects import cookies

from dotenv import load_dotenv

load_dotenv("/home/b5050d/secrets/myapp.env")

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-default-key")


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


#################################################################
# On Call wCookies
#################################################################


@app.route("/cookies")
def cookies_home():
    print(cookies)
    return render_template("cookies_home.html", cookies=cookies)


@app.route("/cookie/<int:cookie_id>")
def cookie(cookie_id):
    cookie = cookies[cookie_id]
    return render_template("cookie_page.html", cookie=cookie)


#################################################################
# Debugging / Scratch
#################################################################

"""
Alright now I need to implment a cart on this guy

so how would a cart work? Certain actions would add something to the cart
"""


@app.route("/test")
def test():
    count = int(request.cookies.get("count", 0))
    html = f"""
        <h1>Button clicked {count} times</h1>
        <form method="POST" action="/increment">
            <button type="submit">Click Me</button>
        </form>
    """
    return render_template_string(html)


@app.route("/increment", methods=["POST"])
def increment():
    count = int(request.cookies.get("count", 0)) + 1
    resp = make_response("", 303)
    resp.headers["Location"] = "/test"
    resp.set_cookie("count", str(count))
    return resp


if __name__ == "__main__":
    app.run(debug=True)
