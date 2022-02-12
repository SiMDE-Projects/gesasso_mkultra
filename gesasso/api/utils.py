import json
import logging
from datetime import datetime

from django.contrib.admin.models import CHANGE, LogEntry, ADDITION, DELETION
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone

logger = logging.getLogger(__name__)


def print_json(obj):
    print(json.dumps(obj, indent=4, sort_keys=True))


class QuerySet(models.QuerySet):
    def _get_model_field(self, field_name):
        for field in self.model._meta.fields:
            if field.name == field_name:
                return field
        raise AttributeError("%s has no field %r'" % (self.model.__name__, field_name))

    def _field_name_to_column_name(self, field_name):
        field = self._get_model_field(field_name)
        return field.db_column

    def extra_date_trunc(self, trunc, field_name, alias=None):
        column_name = self._field_name_to_column_name(field_name)
        if alias is None:
            alias = field_name + "__trunc__" + trunc
        # db_engine = get_db_engine()
        trunc = trunc.lower()
        # if MYSQL_ENGINE == db_engine:
        #     if 'year' == trunc:
        #         fmt = '%%Y-01-01 00:00:00'
        #     elif 'month' == trunc:
        #         fmt = '%%Y-%%m-01 00:00:00'
        #     elif 'day' == trunc:
        #         fmt = '%%Y-%%m-%%d 00:00:00'
        #     elif 'hour' == trunc:
        #         fmt = '%%Y-%%m-%%d %%H:00:00'
        #     elif 'minute' == trunc:
        #         fmt = '%%Y-%%m-%%d %%H:%%i:00'
        #     else:
        #         raise ValueError("Invalid '%s' value for 'trunc'" % trunc)
        #     sql = "DATE_FORMAT(`%s`, '%s')" % (column_name, fmt)
        # elif PGSQL_ENGINE == db_engine:
        if trunc not in ("year", "month", "day", "hour", "minute"):
            raise ValueError("Invalide step '%s'" % trunc)
        sql = "DATE_TRUNC('%s', \"%s\")" % (trunc, column_name)
        return self.extra({alias: sql})


class Manager(models.Manager.from_queryset(QuerySet)):
    pass


class GetFreshMixin:
    def get_fresh(self):
        """Return the object from the db with the same pk."""
        return self.__class__.objects.get(pk=self.pk)


class Model(GetFreshMixin, models.Model):
    objects = Manager()

    class Meta:
        abstract = True


def filter_active(queryset, prefix=""):
    return queryset.filter((prefix + "removed", None))


class TimeStampableQuerySetMixin:
    def active(self):
        return filter_active(self)

    def delete(self):
        return self.update(removed=timezone.now(), updated=timezone.now())

    def hard_delete(self):
        return super().delete()


class TimeStampableQuerySet(TimeStampableQuerySetMixin, QuerySet):
    pass


# managers
TimeStampableManager = Manager.from_queryset(TimeStampableQuerySet)


class TimeStampableMixin:
    # Do not forget to manually declare at least removed field

    def delete(self):
        self.removed = timezone.now()
        self.updated = timezone.now()
        self.save()

    def hard_delete(self):
        super().delete()

    def is_deleted(self):
        return self.removed is not None and self.removed < timezone.now()


class TimeStampable(TimeStampableMixin, Model):
    objects = TimeStampableManager()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    removed = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        abstract = True


class TrackerMixin:
    def perform_destroy(self, instance):
        """
        Override the create method to log the destruction of the object
        """
        LogEntry.objects.log_action(
            user_id=self.request.user.pk,
            content_type_id=ContentType.objects.get_for_model(self.queryset.model).pk,
            object_id=instance.pk,
            object_repr=repr(instance),
            action_flag=DELETION,
            change_message="Removed by user {}".format(self.request.user.full_name),
        )
        super().perform_destroy(instance)

    def perform_create(self, serializer):
        """
        Override the create method to log the creation of the object
        """
        super().perform_create(serializer)
        LogEntry.objects.log_action(
            user_id=self.request.user.pk,
            content_type_id=ContentType.objects.get_for_model(self.queryset.model).pk,
            object_id=serializer.instance.pk,
            object_repr=repr(serializer.instance),
            action_flag=ADDITION,
            change_message="Created by user {}".format(self.request.user.username),
        )

    def perform_update(self, serializer):
        """
        Override the create method to log the update of the object
        """
        super().perform_update(serializer)
        LogEntry.objects.log_action(
            user_id=self.request.user.pk,
            content_type_id=ContentType.objects.get_for_model(self.queryset.model).pk,
            object_id=serializer.instance.pk,
            object_repr=repr(serializer.instance),
            action_flag=CHANGE,
            change_message="Updated by user {}".format(self.request.user.username),
        )


def date_to_timezone(date: str):
    return timezone.make_aware(datetime.strptime(date, "%Y-%m-%d %H:%M:%S"))
