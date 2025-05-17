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
