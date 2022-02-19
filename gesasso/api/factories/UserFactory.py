import factory.django
from oauth_pda_app.models import User


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")

    class Meta:
        model = User
