import graphene
from movies.api.schema import MovieQuery, MovieMutation


class Query(
    MovieQuery,
):
    pass


class Mutation(
    MovieMutation
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
