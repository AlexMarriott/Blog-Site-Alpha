from flask_login import UserMixin

class Post():
    def __int__(self, title, content, author_name, author_id, timestamp):
        self.title = title
        self.content = content
        self.author_name = author_name
        self.author_id = author_id
        self.timestamp = timestamp

    #def __repr__(self):
    #    return f"Post('{self.title}', '{self.content}', '{self.author_name}', '{self.author_id}', '{self.timestamp}')"

class User(UserMixin):
    def __init__(self, id, name, email, profile_pic):
        self.id = id
        self.name = name
        self.email = email
        self.profile_pic = profile_pic

    #def __repr__(self):
    #    return f"User('{self.id}', '{self.name}', '{self.email}', '{self.profile_pic}')"

class Comment():
    def __init__(self, commenter_id, commenter, profile_pic, comment, timestamp):
        self.commenter_id = commenter_id
        self.commenter = commenter
        self.profile_pic = profile_pic
        self.comment = comment
        self.timestamp = timestamp

    #def __repr__(self):
    #    return f"Comment('{self.commenter_id}', '{self.commenter}', '{self.comment}', '{self.timestamp}')"
