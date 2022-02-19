import factory.django

from api.factories import AssoFactory, UserFactory
from gesasso.api.models import Request


class RequestFactory(factory.django.DjangoModelFactory):
    asso = factory.SubFactory(AssoFactory)
    user = factory.SubFactory(UserFactory)
    title = factory.Faker("name")
    description = factory.Faker("text")
    status = factory.Faker("random_element", elements=Request.Status.values)

    class Meta:
        model = Request
