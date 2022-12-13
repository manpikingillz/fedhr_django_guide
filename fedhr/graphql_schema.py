import graphene

from fedhr.users.graph.schema import schema as users_schema
from fedhr.employee.graph.schema import schema as employee_schema


class Query(
    users_schema.Query,
    employee_schema.Query
):
    pass


class Mutation(
    users_schema.Mutation,
    employee_schema.Mutation
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
