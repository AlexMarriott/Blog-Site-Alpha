from flask import current_app
from flask_login import login_manager
from google.cloud import datastore

from API.models import User

builtin_list = list


def get_client():
    return datastore.Client(current_app.config['PROJECT_ID'])


def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        {id: id, prop: val, ...}
    """
    if not entity:
        return None
    if isinstance(entity, builtin_list):
        entity = entity.pop()

    entity['id'] = entity.key.id
    return entity


def list(limit=10, cursor=None):
    ds = get_client()

    query = ds.query(kind='Post', order=['title'])
    query_iterator = query.fetch(limit=limit, start_cursor=cursor)
    page = next(query_iterator.pages)

    entities = builtin_list(map(from_datastore, page))
    next_cursor = (
        query_iterator.next_page_token.decode('utf-8')
        if query_iterator.next_page_token else None)

    return entities


def read(id, kind='Post'):
    ds = get_client()
    # Select * from `Comment` where Key(Post, 5081456606969856) HAS DESCENDANT __key__
    if kind == 'Comment':
        comments = []
        # Getting all the comments attached to a post.
        post_key = ds.key('Post', int(id))
        comment_query = ds.query(kind=kind, ancestor=post_key)
        results = comment_query.fetch()
        for entity in results:
            comments.append(from_datastore(entity))
        return comments
    elif kind == 'Post':
        key = ds.key(kind, int(id))
        results = ds.get(key)
        return from_datastore(results)
    else:
        return False


def update(data, id=None, kind='Post'):
    ds = get_client()
    if id and kind == 'Comment':
        # create comment
        parent_key = ds.key('Post', int(id))
        key = ds.key('Comment', parent=parent_key)
    elif id:
        # edit post
        key = ds.key(kind, int(id))
    else:
        # create post
        key = ds.key(kind)

    entity = datastore.Entity(
        key=key)

    entity.update(data)
    ds.put(entity)
    return from_datastore(entity)


create = update


def delete(id):
    ds = get_client()
    key = ds.key('Post', int(id))
    ds.delete(key)

def get_user(id):
    ds = get_client()
    query = ds.query(kind='User')
    query.add_filter('user_id', '=', id)
    results = query.fetch()
    print(id)
    for i in results:
        print(from_datastore(i)['id'])
        if from_datastore(i)['user_id'] == id:
            print(from_datastore(i)['id'])
            print(from_datastore(i)['name'])
            print(from_datastore(i)['email'])
            print(from_datastore(i)['picture'])
            return User(id=from_datastore(i)['id'],name=from_datastore(i)['name'],email=from_datastore(i)['email'],profile_pic=from_datastore(i)['picture'])
    return False

def create_user(user = None):
    if user is None:
        return 'Cannot add user'
#TODO the way I add the id is crap, check.
    ds = get_client()
    key = ds.key('User')

    entity = datastore.Entity(
            key=key)
    entity.update({'user_id':user.id,'name':user.name,'email':user.email,'picture':user.profile_pic})
    ds.put(entity)
