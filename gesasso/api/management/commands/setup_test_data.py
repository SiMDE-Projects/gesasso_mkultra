import random

from django.core.management.base import BaseCommand
from django.db import transaction
from oauth_pda_app.models import User

from gesasso.api.factories import UserFactory, RequestFactory, RequestMessageFactory
from gesasso.api.models import Request, RequestMessage
from gesasso.proxy_pda.models import Asso

NUM_USERS = 10
NUM_REQUESTS = 10
MAX_MESSAGES_PER_REQUEST = 25


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [
            RequestMessage,
            Request,
            User,
            Asso,
        ]
        Asso.objects.all().update(parent=None)
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create all the users
        users = []
        for _ in range(NUM_USERS):
            person = UserFactory()
            users.append(person)

        # Add some requests
        requests = []
        for _ in range(NUM_REQUESTS):
            request = RequestFactory()
            members = random.choices(users, k=random.randint(0, 2))
            request.assignees.add(*members)
            for _ in range(random.randint(0, MAX_MESSAGES_PER_REQUEST)):
                RequestMessageFactory(request=request)
            requests.append(request)
