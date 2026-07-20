import uuid

# --- ПОЗИТИВНЫЕ ТЕСТЫ ---


def test_create_project_positive(api_client):
    """Успешное создание проекта с валидным именем."""
    unique_title = f"Project_{uuid.uuid4().hex[:8]}"
    payload = {"title": unique_title}

    response = api_client.create_project(payload)

    assert response.status_code == 201
    assert "id" in response.json()
    project_id = response.json()["id"]
    get_response = api_client.get_project(project_id)
    assert get_response.json().get("title") == unique_title


def test_get_project_positive(api_client, temp_project):
    project_id = temp_project["id"]

    response = api_client.get_project(project_id)

    assert response.status_code == 200
    assert response.json()["id"] == project_id
    assert "title" in response.json()


def test_update_project_positive(api_client, temp_project):
    project_id = temp_project["id"]
    new_title = f"Updated_Project_{uuid.uuid4().hex[:8]}"
    payload = {"title": new_title}

    response = api_client.update_project(project_id, payload)

    assert response.status_code == 200
    get_response = api_client.get_project(project_id)
    assert get_response.json().get("title") == new_title

# --- НЕГАТИВНЫЕ ТЕСТЫ ---


def test_create_project_negative_missing_title(api_client):
    """Ошибка при создании проекта без обязательного поля title."""
    payload = {}  # Пустой запрос

    response = api_client.create_project(payload)

    assert response.status_code == 400
    assert "title" in response.text


def test_get_project_negative_invalid_id(api_client):
    """Ошибка при запросе несуществующего или невалидного ID проекта."""
    invalid_id = "non-existent-id-12345"

    response = api_client.get_project(invalid_id)

    assert response.status_code == 404
    assert "not found" in response.text.lower()


def test_update_project_negative_unauthorized(api_client, temp_project):
    """Ошибка авторизации (401) при обновлении проекта с неверным токеном."""
    project_id = temp_project["id"]
    payload = {"title": "Unauthorized Update"}
    bad_headers = {"Authorization": "Bearer INVALID_TOKEN",
                   "Content-Type": "application/json"}

    response = api_client.update_project(project_id, payload,
                                         headers=bad_headers)

    assert response.status_code == 401
    assert "auth" in response.text.lower() or "token" in response.text.lower()
