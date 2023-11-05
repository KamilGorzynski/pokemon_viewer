import factory
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')


class AccessTokenFactory(factory.Factory):
    class Meta:
        model = AccessToken

    user = factory.SubFactory(UserFactory)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        user = kwargs.get('user')
        access_token = AccessToken.for_user(user)
        return str(access_token)
