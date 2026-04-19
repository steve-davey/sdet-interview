import requests
import pytest

def test_get_posts_returns_200(base_url):
    r = requests.get(f"{base_url}/posts")
    assert r.status_code == 200

def test_get_posts_returns_list(base_url):
    r = requests.get(f"{base_url}/posts")
    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_single_post(base_url):
    r = requests.get(f"{base_url}/posts/1")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data

def test_create_post(base_url):
    payload = {"title": "Test Post", "body": "Test body", "userId": 1}
    r = requests.post(f"{base_url}/posts", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["title"] == payload["title"]
    assert "id" in data

def test_update_post(base_url):
    payload = {"id": 1, "title": "Updated Title", "body": "Updated body", "userId": 1}
    r = requests.put(f"{base_url}/posts/1", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["title"] == "Updated Title"

def test_delete_post(base_url):
    r = requests.delete(f"{base_url}/posts/1")
    assert r.status_code == 200