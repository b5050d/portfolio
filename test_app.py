import pytest
from app import app

def test_home_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to My Portfolio" in response.data

# TODO - Check that the sections load when loading the home page


# TODO - Test that pressing the View Resume button actually takes you
# to the resume file

