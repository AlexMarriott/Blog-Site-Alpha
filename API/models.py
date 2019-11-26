class Post():
    def __int__(self, title, content, user):
        self.title = title
        self.content = content
        self.user = user

    def __repr__(self):
        return f"Post('{self.title}', '{self.content}', '{self.user}')"

class User():
    def __init__(self, user_id, name, email, profile_pic):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.profile_pic = profile_pic

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.profile_pic}')"