import json
from typing import List, Dict
class PostsDAO:

    def __init__(self, path):
        self.path = path

    def get_all(self):
        """возвращает посты"""
        with open(f"{self.path}", "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_by_user(self, user_name):
        """
        возвращает посты определенного пользователя
        """
        posts = self.get_all()
        posts_by_user = []

        for post in posts:
            if post["poster_name"] == user_name:
                posts_by_user.append(post)
        return posts_by_user

    def search_for_posts(self, query: str) -> list:
        """
        :return: list of posts, sorted by query
        """
        posts = self.get_all()
        posts_by_query = [post for post in posts if
                          query.lower() in post['content'].lower()]
        return posts_by_query

    def get_post_by_pk(self, post_id: int) -> Dict:
        """
        возвращает пост по его идентификатору
        """
        posts = self.get_all()
        for post in posts:
            if post['pk'] == post_id:
                return post

    def load_comments(self, path="./data/comments.json") -> List[Dict]:
        with open(path, encoding="utf-8") as file:
            return json.load(file)

    def get_comments_by_post_pk(self, post_pk: int) -> List[Dict]:
        comments = self.load_comments()
        post_comments = [comment for comment in comments if
                         comment["post_id"] == post_pk]
        if not post_comments:
            raise ValueError("У поста нет комментариев")
        return post_comments