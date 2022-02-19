import factory.django
from django.utils import timezone

from gesasso.api.factories import AssoFactory
from gesasso.api.models import Request


class RequestFactory(factory.django.DjangoModelFactory):
    asso = factory.SubFactory(AssoFactory)
    user = factory.SubFactory("gesasso.api.factories.UserFactory")
    # assignees = factory.LazyAttribute(lambda o: [o.user])
    due_date = factory.Faker(
        "date_time_this_year", tzinfo=timezone.get_current_timezone()
    )
    title = factory.Faker("name")
    status = factory.Faker("random_element", elements=Request.Status.values)
    origin = factory.Faker("random_element", elements=Request.Origin.values)

    # messages = factory.SubFactory("gesasso.api.factories.RequestMessageFactory")

    class Meta:
        model = Request
