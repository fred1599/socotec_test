import uuid

import pytest
from django.urls import reverse

from actor.models import Actor
from movie.models import Movie


@pytest.fixture
def test_password():
    return "strong-test-pass"


@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs["password"] = test_password
        if "username" not in kwargs:
            kwargs["username"] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def auto_login_user(db, client, create_user, test_password):
    def make_auto_login(user=None):
        if user is None:
            user = create_user()
        client.login(username=user.username, password=test_password)
        return client, user

    return make_auto_login


@pytest.fixture
def create_movie(db):
    actor = Actor.objects.create(first_name="test", last_name="test")
    movie = Movie.objects.create(
        title="It Must Be Heaven",
        description="mon film",
    )
    movie.actors.add(actor)
    return movie


@pytest.mark.django_db
def test_send_review(auto_login_user, create_movie):
    client, user = auto_login_user()
    url = reverse("add_review")
    test_data = {"grade": 3, "name": "It Must Be Heaven", "text": "C'est un super film"}
    response = client.post(
        url, data=test_data, headers={"content-type: application/json"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == 200
