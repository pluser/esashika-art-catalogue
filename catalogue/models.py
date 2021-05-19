from django.db import models

class Opuses(models.Model):
    opus_title = models.CharField(max_length=200)
    opus_description = models.TextField()
