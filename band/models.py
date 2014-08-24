from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    instrument = models.CharField(max_length=20)
    join_date = models.DateTimeField('date published')

