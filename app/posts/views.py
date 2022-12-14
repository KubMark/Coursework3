from flask import Blueprint, render_template, request

from app.posts.dao.posts_dao import PostsDAO
from app.bookmarks.dao.bookmarks_dao import BookmarksDAO

posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder='templates')

posts_dao = PostsDAO('./data/posts.json')
bookmarks_dao = BookmarksDAO('./data/bookmarks.json')

@posts_blueprint.route('/')
def home_page():
    posts = posts_dao.get_all()
    return render_template('index.html', posts=posts)


@posts_blueprint.route('/users/<user_name>', methods=['get'])
def get_posts_by_user(user_name):
    posts = posts_dao.get_by_user(user_name)
    return render_template('user-feed.html', posts=posts)


@posts_blueprint.route('/posts/<post_id>', methods=['get'])
def get_post_by_id(post_id):
    post = posts_dao.get_post_by_pk(post_id)
    comments = posts_dao.get_comments_by_post_pk(post_id)
    return render_template('post.html', post=post, title=post_id,
                           comments=comments)


@posts_blueprint.route('/search')
def get_posts_by_query():
    query = request.args.get('s')
    posts_with_query: list[dict] = posts_dao.search_for_posts(query)
    return render_template('search.html', title=query,
                           posts_with_query=posts_with_query)
