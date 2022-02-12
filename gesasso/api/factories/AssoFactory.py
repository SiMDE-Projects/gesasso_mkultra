import factory.django

from proxy_pda.models import Asso


class AssoFactory(factory.django.DjangoModelFactory):
    id = factory.Faker("uuid4")
    shortname = factory.Faker("name")
    login = factory.Faker("name")

    class Meta:
        model = Asso
