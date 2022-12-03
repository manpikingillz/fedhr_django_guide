import graphene

from fedhr.users.graph.mutations import AuthMutation
from fedhr.users.graph.queries import UserQueries


class Query(UserQueries):
    pass


class Mutation(AuthMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
