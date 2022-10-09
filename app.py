from flask import Flask

from app.posts.views import posts_blueprint
# from app.bookmarks.views import bookmarks_blueprint

app = Flask(__name__)

app.register_blueprint(posts_blueprint)
# app.register_blueprint(bookmarks_blueprint)


if __name__ == "__main__":
    app.run()