from django.db import models

# Create your models here.
class HomePageHeadLine(models.Model):
    brand_name = models.CharField(max_length=200 , null=True , blank=True)
    backgroundimg = models.ImageField(null=True , blank=True)
    head_line = models.CharField(max_length=200, null=True , blank=True)
    p = models.CharField(max_length=200, null=True , blank=True)
    backgroundimg2 = models.ImageField(null=True , blank=True)
    head_line2 = models.CharField(max_length=200, null=True , blank=True)
    p2 = models.CharField(max_length=200, null=True , blank=True)
    backgroundimg3 = models.ImageField(null=True , blank=True)
    head_line3 = models.CharField(max_length=200, null=True , blank=True)
    p3 = models.CharField(max_length=200, null=True , blank=True)
class ShopPageHeadLine(models.Model):
    img = models.ImageField(null=True , blank=True)
    head_line = models.CharField(max_length=200, null=True , blank=True)
    p = models.CharField(max_length=200, null=True , blank=True)   