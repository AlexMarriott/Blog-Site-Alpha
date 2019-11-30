"""

For all the common functions across the platform.

"""
from flask import current_app

def get_model():
    model_backend = current_app.config['DATA_BACKEND']
    if model_backend == 'datastore':
        from API import model_datastore
        model = model_datastore
    else:
        raise ValueError(
            "No appropriate databackend configured. "
            "Please specify datastore, cloudsql, or mongodb")
    return model

def check_post_author(author_id, current_user_id):
    #Get the owner of the post's user id then compare it with the current user.
    author = get_model().get_user(author_id)
    if author.id == current_user_id:
        return True
    else:
        return False