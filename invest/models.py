from django.db import models

# Create your models here.
class Province(models.Model):
    code = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    province = models.CharField(max_length=32, blank=True, null=True,unique=True)
    #city = models.CharField(max_length=32, blank=True, null=True)
    #area = models.CharField(max_length=32, blank=True, null=True)
    #town = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province'


class City(models.Model):
    code = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING,to_field='province')
    city = models.CharField(max_length=32, blank=True, null=True,unique=True)
    #area = models.CharField(max_length=32, blank=True, null=True)
    #town = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'

class Area(models.Model):
    code = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING,to_field='province')
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING,to_field='city')
    area = models.CharField(max_length=32, blank=True, null=True,unique=True)
    #town = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area'        

class Town(models.Model):
    code = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING,to_field='province')
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING,to_field='city')
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING,to_field='area')
    town = models.CharField(max_length=32, blank=True, null=True,unique=True)

    class Meta:
        managed = False
        db_table = 'town'    