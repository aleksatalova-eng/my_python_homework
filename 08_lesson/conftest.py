import pytest
import uuid
from projects_client import ProjectsClient


@pytest.fixture(scope="session")
def api_client():
    return ProjectsClient()


@pytest.fixture
def temp_project(api_client):
    unique_title = f"Autotest Project {uuid.uuid4().hex[:6]}"
    payload = {"title": unique_title}
    response = api_client.create_project(payload)
    assert response.status_code == 201
    project_data = response.json()
    yield project_data
