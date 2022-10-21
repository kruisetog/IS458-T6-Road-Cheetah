import json
from sqlalchemy import create_engine, text
from database import get_session
from crud import new_user

DATABASE_URL = "mysql+pymysql://admin:11111111@database-1-instance-1.cqbbxkouucyk.us-east-1.rds.amazonaws.com:3306/cs301_scis_bank"
engine = create_engine(DATABASE_URL)


def lambda_handler(event, context):
    # TODO implement
    try:
        response = new_user(db=get_session(), user_info=event["user"])
        return response
    except Exception as e:
        print(e)
    return True
