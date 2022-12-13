import graphene
from graphql_auth.schema import UserQuery, MeQuery


class UserQueries(UserQuery, MeQuery, graphene.ObjectType):
    pass
