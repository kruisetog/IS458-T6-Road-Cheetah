""" Starts a session for the DB call """

# from pgsql.database import SessionLocal
from datetime import datetime
from database import User
import uuid


def new_user(db, user_info):
    """ posts a single notification to the database """
    try:
        print(user_info)
        user_entity = User(**user_info)
        user_id = str(uuid.uuid4().hex.upper())
        user_entity.User_ID = user_id
        print('User: ', user_entity.__dict__)
        db.add(user_entity)
        db.commit()

        response = db.query(User).filter(
            User.User_ID == user_id).one().__dict__
        response.pop('_sa_instance_state')
        return response

    except Exception as err:
        db.rollback()
        raise err
