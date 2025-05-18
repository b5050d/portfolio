from app import app


# Check that the sections load when loading the home page
def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"About Me" in response.data
    assert b"Skills" in response.data
    assert b"Work Experience" in response.data
    assert b"Education" in response.data


def test_resume_button():
    client = app.test_client()
    response = client.get("/static/BDyer_Resume_5_25.pdf")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/pdf"


def test_projects_route():
    client = app.test_client()
    response = client.get("/projects")
    assert response.status_code == 200
    assert b"Projects" in response.data


# TODO - Add testing of project pages


def test_cookies_route():
    client = app.test_client()
    response = client.get("/cookies")
    assert response.status_code == 200
    assert b"Northern Colorado Cookies" in response.data
    assert b"Beautifully crafted cookies" in response.data


def test_cookies_shop_route():
    client = app.test_client()
    response = client.get("/cookies/shop")
    assert response.status_code == 200
    # assert b"Shop" in response.data


def test_cookies_cart_route():
    client = app.test_client()
    response = client.get("/cookies/cart")
    assert response.status_code == 200
    assert b"Cart" in response.data


def test_cookie_add_to_cart():
    client = app.test_client()

    # First, send the request
    response = client.get("/cookies/add_to_cart/0")
    assert response.status_code == 302

    # Then, check session after the request
    with client.session_transaction() as sess:
        assert sess["cart"] == [0]

    # send another request
    response = client.get("/cookies/add_to_cart/1")
    assert response.status_code == 302

    # Then, check session after the request
    with client.session_transaction() as sess:
        assert sess["cart"] == [0, 1]

    # send another request
    response = client.get("/cookies/add_to_cart/2")
    assert response.status_code == 302

    # Then, check session after the request
    with client.session_transaction() as sess:
        assert sess["cart"] == [0, 1, 2]
