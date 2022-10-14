from flask import Flask

from app.posts.views import posts_blueprint
from app.bookmarks.views import bookmarks_blueprint
from app.api.views import api_blueprint
from logger import config

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(posts_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(api_blueprint)
config()


if __name__ == "__main__":
    app.run()