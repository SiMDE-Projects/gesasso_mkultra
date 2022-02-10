# Generated by Django 3.2 on 2022-02-10 18:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import gesasso.api.utils


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("proxy_pda", "__first__"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Action",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("removed", models.DateTimeField(blank=True, default=None, null=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=150, unique=True)),
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
            name="Request",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("removed", models.DateTimeField(blank=True, default=None, null=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=150)),
                ("description", models.TextField()),
                ("due_date", models.DateTimeField(blank=True, null=True)),
                ("user", models.CharField(max_length=150)),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "OPEN"),
                            (2, "ASSIGNED"),
                            (3, "CLOSED"),
                            (4, "DONE"),
                            (5, "WAITING_TECH"),
                            (6, "WAITING_FOR_TIERS_SERVICE"),
                            (7, "WAITING_FOR_CUSTOMER"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "origin",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "WEB"), (2, "MAIL"), (3, "DIRECT"), (4, "MERGE")],
                        default=3,
                    ),
                ),
                ("actions", models.ManyToManyField(to="api.Action")),
                (
                    "asso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="proxy_pda.asso"
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
            name="TaskType",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("removed", models.DateTimeField(blank=True, default=None, null=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=150, unique=True)),
                ("target", models.CharField(max_length=150)),
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
            name="Task",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("removed", models.DateTimeField(blank=True, default=None, null=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("params", models.JSONField()),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.tasktype"
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
            name="RequestMessage",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("removed", models.DateTimeField(blank=True, default=None, null=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("message", models.TextField()),
                (
                    "type",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "PUBLIC"),
                            (2, "INTERNAL"),
                            (3, "SUCCESS"),
                            (4, "ERROR"),
                            (5, "INFO"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "origin",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "MAIL"), (2, "DIRECT")], default=2
                    ),
                ),
                (
                    "request",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.request"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
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
            name="ActionType",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("removed", models.DateTimeField(blank=True, default=None, null=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=150, unique=True)),
                ("tasks_types", models.ManyToManyField(to="api.TaskType")),
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
        migrations.AddField(
            model_name="action",
            name="type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.actiontype"
            ),
        ),
    ]
