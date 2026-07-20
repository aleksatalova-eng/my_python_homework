import requests
import config


class ProjectsClient:
    def __init__(self):
        self.base_url = f"{config.BASE_URL}/api-v2/projects"
        self.headers = config.HEADERS

    def create_project(self, payload: dict, headers: dict = None):
        target_headers = headers if headers is not None else self.headers
        return requests.post(self.base_url, json=payload,
                             headers=target_headers)

    def get_project(self, project_id: str, headers: dict = None):
        target_headers = headers if headers is not None else self.headers
        return requests.get(f"{self.base_url}/{project_id}",
                            headers=target_headers)

    def update_project(self, project_id: str, payload: dict,
                       headers: dict = None):
        target_headers = headers if headers is not None else self.headers
        return requests.put(f"{self.base_url}/{project_id}", json=payload,
                            headers=target_headers)

    def delete_project(self, project_id: str, headers: dict = None):
        """Метод удаления проекта для очистки данных после тестов"""
        target_headers = headers if headers is not None else self.headers
        return requests.delete(f"{self.base_url}/{project_id}",
                               headers=target_headers)
