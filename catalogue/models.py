from django.db import models

class Opus(models.Model):
    opus_title = models.CharField(max_length=200)
    opus_description = models.TextField()
    opus_image = models.ImageField(upload_to='opus_image', null=True)

    class Meta:
        verbose_name_plural = 'Opuses'

    def __str__(self):
        return self.opus_title
