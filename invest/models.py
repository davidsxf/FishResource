from django.db import models

# Create your models here.
class Province(models.Model):
    code = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    province = models.CharField(max_length=32, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    area = models.CharField(max_length=32, blank=True, null=True)
    town = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province'


