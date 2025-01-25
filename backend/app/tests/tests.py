import os
import pytest
from main import app
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    return TestClient(app)

def test_upload(client):
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(curr_dir, "../../sample_data/events.bin")
    with open(file_path, 'rb') as file:
        file_form = {'file': ('events.bin', file, 'application/octet-stream')}
        response = client.post('/upload', files=file_form)
    assert response.status_code == 200

def test_download(client):
    response = client.get('/download_json')
    assert response.status_code == 200