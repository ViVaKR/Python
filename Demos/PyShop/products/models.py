from django.db import models


# Create your models here.
# id field 는 자동 생성됨
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    discription = models.CharField(max_length=255)
    discount = models.FloatField()




