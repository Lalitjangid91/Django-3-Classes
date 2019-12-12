from django.db import models
class GirlModel(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=128)
    branch=models.CharField(max_length=10)

    def __str__(self):
        return self.name
