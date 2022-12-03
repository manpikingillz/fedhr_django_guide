import graphene

from fedhr.employee.graph.mutations import EmployeeMutations
from fedhr.employee.graph.queries import EmployeeQueries


class Query(EmployeeQueries):
    pass


class Mutation(EmployeeMutations):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
