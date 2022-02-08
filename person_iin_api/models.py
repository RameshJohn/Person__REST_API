from django.db import models


class Person(models.Model):

    iin = models.CharField(max_length=12, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.iin