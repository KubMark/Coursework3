import pytest
from main import app

# Задаем, какие ключи ожидаем получать
keys_should_be = {"poster_name",
                  "poster_avatar",
                  "pic", "content",
                  "Ага", "likes_count",
                  "pk"},

class Test_api:
    def test_api_posts(self):
        response = app.test_client().get("/api/posts/")
        assert type(response.json) == list, "Возвращает не список"
        assert type(response.json[0]) == dict
        for i in range(len(response.json)):
            assert set(response.json[i].keys()) == set(
                keys_should_be), "Неверный список ключей"

    def test_api_posts_by_pk(self):
        response = app.test_client().get(f"/api/posts/1")
        assert type(response.json) == dict
        assert set(response.json.keys()) == set(
            keys_should_be), "Неверный список ключей"


