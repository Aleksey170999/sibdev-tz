from django.db import models


class Deal(models.Model):
    customer = models.CharField(max_length=50,
                                blank=False,
                                null=False)
    item = models.CharField(max_length=50,
                            blank=False,
                            null=False)
    total = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField()
