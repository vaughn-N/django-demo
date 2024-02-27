from django.db import models

class Developer(models.Model):
    firstname = models.CharField(max_length=25)
    middlename = models.CharField(max_length=25, blank=True, null=True)
    birthdate = models.DateField()


class Tester(models.Model):
    developer = models.ForeignKey(Developer, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=25)