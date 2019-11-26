from flask_login import UserMixin

class Post():
    def __int__(self, title, content, user):
        self.title = title
        self.content = content
        self.user = user

    def __repr__(self):
        return f"Post('{self.title}', '{self.content}', '{self.user}')"

class User(UserMixin):
    def __init__(self, user_id, name, email, profile_pic):
        self.id = user_id
        self.name = name
        self.email = email
        self.profile_pic = profile_pic


    def __iter__(self):
        return {'id':self.user_id, 'name':self.name, 'email':self.email, 'profile_pic':self.profile_pic}
