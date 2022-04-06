from django.db import models
from django_extensions.db.models import TimeStampedModel


# Create your models here.
class Department(TimeStampedModel):
    dep = models.CharField(max_length=30)

    def __str__(self):
        return self.dep


class Employee(TimeStampedModel):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.FloatField()
    dep = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="department")

    def __str__(self):
        return self.name
