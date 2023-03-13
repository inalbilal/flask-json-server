import os

from sqlalchemy import create_engine


class OrmEngine:
    def __init__(self):
        self.engine = create_engine(os.getenv('DATABASE_URL'))
