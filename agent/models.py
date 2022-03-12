import datetime

from django.db import models


# Create your models here.


class Entry(models.Model):
    owner = models.ForeignKey('auth.User', related_name='agent', on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.datetime.now())
    entry_id = models.AutoField(primary_key=True)
    driver_name = models.CharField(max_length=100, default="", blank=True)
    init_load = models.DecimalField(max_digits=6, decimal_places=2)
    init_amount = models.DecimalField(max_digits=8, decimal_places=2)
    init_km = models.DecimalField(max_digits=8, decimal_places=2)
    fin_load = models.DecimalField(max_digits=6, decimal_places=2)
    fin_amount = models.DecimalField(max_digits=8, decimal_places=2)
    fin_km = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.BooleanField(default=True)
    cause = models.TextField()

    def __str__(self):
        return self.driver_name

    class Meta:
        ordering = ['created']
