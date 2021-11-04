import factory.django

from gesasso.api.models import Request, Asso, User


class AssoFactory(factory.django.DjangoModelFactory):
    id = factory.Faker("uuid4")
    shortname = factory.Faker("name")
    login = factory.Faker("name")

    class Meta:
        model = Asso


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")

    class Meta:
        model = User


class RequestFactory(factory.django.DjangoModelFactory):
    asso = factory.SubFactory(AssoFactory)
    user = factory.SubFactory(UserFactory)
    title = factory.Faker("name")
    description = factory.Faker("text")
    status = factory.Faker("random_element", elements=Request.Status.values)

    class Meta:
        model = Request
