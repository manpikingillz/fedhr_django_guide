import graphene

from fedhr.users.graph.users_mutations import AuthMutation
from fedhr.users.graph.users_queries import UserQueries


class Query(UserQueries):
    pass


class Mutation(AuthMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
