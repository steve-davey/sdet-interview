import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts_returns_200():
    r = requests.get(f"{BASE_URL}/posts")
    assert r.status_code == 200

def test_get_posts_returns_list():
    r = requests.get(f"{BASE_URL}/posts")
    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_single_post():
    r = requests.get(f"{BASE_URL}/posts/1")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data

def test_create_post():
    payload = {"title": "Test Post", "body": "Test body", "userId": 1}
    r = requests.post(f"{BASE_URL}/posts", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["title"] == payload["title"]
    assert "id" in data

def test_update_post():
    payload = {"id": 1, "title": "Updated Title", "body": "Updated body", "userId": 1}
    r = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["title"] == "Updated Title"

def test_delete_post():
    r = requests.delete(f"{BASE_URL}/posts/1")
    assert r.status_code == 200