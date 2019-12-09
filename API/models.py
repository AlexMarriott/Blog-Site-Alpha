from flask_login import UserMixin

class Post():
    def __int__(self, title, content, author_name, author_id, timestamp, file):
        self.title = title
        self.content = content
        self.author_name = author_name
        self.author_id = author_id
        self.timestamp = timestamp
        self.file = file

#    def __repr__(self):
#        return f"Post('{self.title}', '{self.content}', '{self.author_name}', '{self.author_id}', '{self.timestamp}')"


class User(UserMixin):
    def __init__(self, id, name, email, profile_pic):
        self.id = id
        self.name = name
        self.email = email
        self.profile_pic = profile_pic

    def convert_to_dict(self):
        """
        A function takes in a custom object and returns a dictionary representation of the object.
        This dict representation includes meta data such as the object's module and class names.
        """

        #  Populate the dictionary with object meta data
        obj_dict = {
            "__class__": self.__class__.__name__,
            "__module__": self.__module__
        }

        #  Populate the dictionary with object properties
        obj_dict.update(self.__dict__)

        return obj_dict



class Comment():
    def __init__(self, commenter_id, commenter, profile_pic, comment, timestamp):
        self.commenter_id = commenter_id
        self.commenter = commenter
        self.profile_pic = profile_pic
        self.comment = comment
        self.timestamp = timestamp

#    def __repr__(self):
#        return f"Comment('{self.commenter_id}', '{self.commenter}', '{self.comment}', '{self.timestamp}')"

class Card():
    def __init__(self, title, label, description, user, email):
        self.title = title
        self.label = label
        self.description = description
        self.requesting_user = user
        self.requestin_user_email = email
