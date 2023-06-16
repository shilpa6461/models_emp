from django.db import models


# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=100)
    id=models.IntegerField(primary_key=True)
    sal=models.IntegerField()

    def __str__(self):
        return self.name

class Dept(models.Model):
    name=models.ForeignKey(Emp,on_delete=models.CASCADE)
    loc=models.CharField(max_length=100)

