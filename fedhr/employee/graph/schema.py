import graphene

from fedhr.employee.graph.mutations import EmployeeMutations
from fedhr.employee.graph.queries import EmployeeQueries


# mutations

# filters

# resolvers

# sorters

# types

# TODO: Data Validation and Error handling
# TODO: Handling m2m and Reverse relationships
# TODO: Caching
# TODO: Authorization / Permissions
# TODO: Authentication.
# TODO: Filters
# TODO: Pagination


class Query(EmployeeQueries):
    pass


class Mutation(EmployeeMutations):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
