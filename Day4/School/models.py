from django.db import models
class College(models.Model):
    name=models.CharField(max_length=256)
    principal=models.CharField(max_length=256)
    location=models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=128)
    college=models.ForeignKey(College,on_delete=models.CASCADE)
    branch=models.CharField(max_length=256)
    semester=models.IntegerField()
    def __str__(self):
        return self.name
