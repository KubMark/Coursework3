from flask import Blueprint, render_template, redirect
from app.posts.views import posts_dao
from app.bookmarks.dao.bookmarks_dao import BookmarksDAO

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates')

bookmarks_dao = BookmarksDAO('./data/bookmarks.json')

@bookmarks_blueprint.route('/')
def load_all_bookmarks():
    bookmarks = bookmarks_dao.load_all_bookmarks()
    return render_template('bookmarks.html', title='Bookmarks',
                           bookmarks=bookmarks)


@bookmarks_blueprint.route('/add/<int:pk>', methods=['GET'])
def add_post_to_bookmark(pk):
    post_by_pk = posts_dao.get_by_pk(pk)
    bookmarks_dao.add_post_to_bookmarks(post_by_pk)
    return redirect('posts_blueprint.main_page')


@bookmarks_blueprint.route('/remove/<int:post_id>')
def remove_post_from_bookmark(post_id):
    bookmarks_dao.delete_post_from_bookmarks(post_id)
    return redirect("/", code=302)