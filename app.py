"""
5.17.2025

The main app page
"""

################################################################
# Imports
################################################################
from flask import (
    Flask,
    render_template,
    request,
    make_response,
    # render_template_string,
    session,
    redirect,
    url_for,
    # # jsonify,
)

import os
from home_objects import educations
from project_objects import my_projects
from skills import skill_categories
from work_experiences import work_experiences
from cookies_objects import cookies_listings
from dotenv import load_dotenv

# import stripe

# Load the secret variable to ensure secure session data
load_dotenv("/home/b5050d/secrets/myapp.env")

# Initialize the app
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-default-key")

################################################################
# Routes for portfolio
################################################################


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
# Routes for Cookies Website
#################################################################


@app.route("/cookies")
def cookies():
    return render_template("cookies.html")


@app.route("/cookies/add_to_cart/<int:cookie_id>")
def cookies_add_to_cart(cookie_id):
    assert cookie_id < len(cookies_listings)
    cart = session.get("cart", [])
    cart.append(cookie_id)
    session["cart"] = cart
    return redirect(url_for("cookies_shop"))


@app.route("/cookies/shop")
def cookies_shop():
    return render_template("cookies_shop.html", cookies=cookies_listings)


@app.route("/cookies/cart")
def cookies_cart():
    cart = session.get("cart", [])
    cart_items = [cookies_listings[i] for i in cart]
    return render_template("cookies_cart.html", cart_items=cart_items)


# @app.route("/checkout", methods=["POST"])
# def checkout():
#     session = stripe.checkout.Session.create(
#         payment_method_types=["card"],
#         line_items=[
#             {
#                 "name": "Cookie",
#                 "description": "Cookie",
#                 "images": ["https://via.placeholder.com/150"],
#                 "amount": 2000,
#                 "currency": "usd",
#                 "quantity": 1,
#             }
#         ],
#         mode="payment",
#         success_url="http://localhost:5000/success",
#         cancel_url="http://localhost:5000/cancel",
#     )
#     return jsonify({"id": session.id})
#     # return render_template("checkout.html", session=session)


#################################################################
# Debugging / Scratch
#################################################################


@app.route("/test")
def test():
    return render_template("test.html")
    # count = int(request.cookies.get("count", 0))
    # html = f"""
    #     <h1>Button clicked {count} times</h1>
    #     <form method="POST" action="/increment">
    #         <button type="submit">Click Me</button>
    #     </form>
    # """
    # return render_template_string(html)


@app.route("/test2")
def test2():
    return render_template("test2.html")


@app.route("/increment", methods=["POST"])
def increment():
    count = int(request.cookies.get("count", 0)) + 1
    resp = make_response("", 303)
    resp.headers["Location"] = "/test"
    resp.set_cookie("count", str(count))
    return resp


if __name__ == "__main__":
    app.run(debug=True)
