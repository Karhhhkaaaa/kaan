from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="images")
