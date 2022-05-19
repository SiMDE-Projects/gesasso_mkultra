# Generated by Django 4.0.2 on 2022-05-19 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gesasso.api.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attachement",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("removed", models.DateTimeField(blank=True, default=None, null=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("type", models.TextField()),
                ("data", models.FileField(upload_to="uploads/attachements/")),
                (
                    "request_message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attachements",
                        to="api.requestmessage",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(
                gesasso.api.utils.TimeStampableMixin,
                gesasso.api.utils.GetFreshMixin,
                models.Model,
            ),
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("removed", models.DateTimeField(blank=True, default=None, null=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                (
                    "members",
                    models.ManyToManyField(
                        related_name="teams", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(
                gesasso.api.utils.TimeStampableMixin,
                gesasso.api.utils.GetFreshMixin,
                models.Model,
            ),
        ),
        migrations.RemoveField(
            model_name="request",
            name="actions",
        ),
        migrations.DeleteModel(
            name="Action",
        ),
        migrations.DeleteModel(
            name="ActionType",
        ),
    ]
