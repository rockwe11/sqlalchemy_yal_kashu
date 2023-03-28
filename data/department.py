import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):
    __tablename__ = 'department'
    # association_table = sqlalchemy.Table(
    #     'association',
    #     SqlAlchemyBase.metadata,
    #     sqlalchemy.Column('users', sqlalchemy.Integer,
    #                       sqlalchemy.ForeignKey('users.id')),
    #     sqlalchemy.Column('department', sqlalchemy.Integer,
    #                       sqlalchemy.ForeignKey('department.id'))
    # )
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chief = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    members = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user = orm.relationship('User')
