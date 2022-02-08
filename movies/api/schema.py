import graphene
import graphql_jwt
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required
from .models import Director, Movie


class DirectorType(DjangoObjectType):
    class Meta:
        model = Director


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

    movie_age = graphene.String()

    def resolve_movie_age(self, info, **kwargs):
        return "Old movie" if self.year < 2000 else "New Movie"


class MovieQuery(graphene.ObjectType):
    all_movies = graphene.List(MovieType)
    movie = graphene.Field(MovieType, id=graphene.Int(), title=graphene.String())

    def resolve_all_movies(self, info, **kwargs):
        return Movie.objects.all()

    def resolve_movie(self, info, **kwargs):
        if kwargs.get('id'):
            return Movie.objects.get(pk=kwargs['id'])

        if kwargs.get('title'):
            return Movie.objects.get(title=kwargs['title'].lower())

        return None


class MovieCreateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        year = graphene.Int(required=True)

    movie = graphene.Field(MovieType)

    def mutate(self, info, title, year):
        movie = Movie.objects.create(title=title, year=year)

        return MovieCreateMutation(movie=movie)


class MovieUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        year = graphene.Int()

    movie = graphene.Field(MovieType)

    def mutate(self, info, id, **kwargs):
        movie = Movie.objects.filter(pk=id).first()

        if movie is None:
            return None

        if kwargs.get('title'):
            movie.title = kwargs.get('title')

        if kwargs.get('year'):
            movie.year = kwargs.get('year')

        movie.save()

        return MovieUpdateMutation(movie=movie)


class MovieDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    movie = graphene.Field(MovieType)

    def mutate(self, info, id):
        movie = Movie.objects.filter(pk=id).delete()

        return MovieDeleteMutation(movie=None)


class MovieMutation(graphene.ObjectType):
    # JWT authentication
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


    # CRUD Mutations
    create_movie = MovieCreateMutation.Field()
    update_movie = MovieUpdateMutation.Field()
    delete_movie = MovieDeleteMutation.Field()
