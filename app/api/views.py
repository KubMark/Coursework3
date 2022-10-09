from flask import Blueprint, jsonify
from app.posts.dao.posts_dao import PostsDAO


api_blueprint = Blueprint("api_blueprint", __name__)
posts = PostsDAO("./data/posts.json")

@api_blueprint.route("/posts/")
def get_all_posts():
    all_posts = posts.get_all()
    return jsonify(all_posts)


# Create post by pk view
@api_blueprint.route("/posts/<int:post_id>")
def get_post_by_pk(pk):
    post = posts.get_post_by_pk(pk)
    return jsonify(post)