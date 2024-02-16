from uuid import uuid4

from django.db import models


class ActivatableFalseMixin(models.Model):
    """
    Mixin to add activation functionality to models.
    """
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True


class TimestampedModel(models.Model):
    """
    Abstract model providing fields for creation and update times.
    """
    creat_time = models.DateField(auto_now_add=True, editable=False)
    update_time = models.DateField(auto_now=True, editable=False)

    class Meta:
        abstract = True
        ordering = ['-update_time']


class BaseModel(models.Model):
    """
    Abstract model with UUID primary key and a name field.
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, auto_created=True)
    name = models.CharField(max_length=200)

    @property
    def title(self):
        return self.name.title()

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        abstract = True
        ordering = ['-name']
