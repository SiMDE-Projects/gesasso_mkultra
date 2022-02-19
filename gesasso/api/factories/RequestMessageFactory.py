import factory.django

from gesasso.api.models import RequestMessage


class RequestMessageFactory(factory.django.DjangoModelFactory):
    message = factory.Faker("text")
    user = factory.SubFactory("gesasso.api.factories.UserFactory")
    request = factory.SubFactory("gesasso.api.factories.RequestFactory")
    type = factory.Faker("random_element", elements=RequestMessage.Types.values)
    origin = factory.Faker("random_element", elements=RequestMessage.Origin.values)

    class Meta:
        model = RequestMessage
