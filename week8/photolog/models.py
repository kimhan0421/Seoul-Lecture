from django.db import models


class Potolog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/')
