from django.db import models
class BoyModel(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=256)
    branch=models.CharField(max_length=10)

    def __str__(self):
        return self.name
