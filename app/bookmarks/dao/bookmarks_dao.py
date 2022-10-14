import json

class BookmarksDAO:

    def __init__(self, path):
        self.path = path

    def load_all_bookmarks(self):
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def add_post_to_bookmark(self, post):
        bookmarks = self.load_all_bookmarks()
        bookmarks_pk = [bookmark["pk"] for bookmark in bookmarks]
        if post["pk"] not in bookmarks_pk:
            with open(self.path, 'w', encoding='utf-8') as file:
                bookmarks.append(post)
                json.dump(bookmarks, fp=file, ensure_ascii=False, indent=4)


    def delete_post_from_bookmarks(self, pk):

        bookmarks: list[dict] = self.load_all_bookmarks()
        for index, bookmark in enumerate(bookmarks):
            if bookmark['pk'] == pk:
                del bookmarks[index]
                break
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(bookmarks, fp=file, ensure_ascii=False, indent=4)