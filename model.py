class Post():
    def __int__(self, title, content, user):
        self.title = title
        self.content = content
        self.user = user

    def __repr__(self):
        return f"Post('{self.title}', '{self.content}', '{self.user}')"