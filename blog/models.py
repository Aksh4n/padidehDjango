from django.db import models
from store.models import Customer
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=400)
    short_info = models.CharField(max_length=400)
    posted_by = models.CharField(max_length=400)
    date = models.DateField(auto_now_add=True)
    main_img = models.ImageField()
    text = models.TextField()
    title2 = models.CharField(max_length=400, null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    img2 = models.ImageField(null=True, blank=True)
    img2alt = models.CharField(max_length=400, null=True, blank=True)
    title3 = models.CharField(max_length=400, null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)
    img3 = models.ImageField(null=True, blank=True)
    img3alt = models.CharField(max_length=400, null=True, blank=True)
    def __str__(self):
        return self.title
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url     

class Comment(models.Model):
    post = models.OneToOneField(Post,on_delete=models.CASCADE)        
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE)
    comment = models.TextField()
    def __str__(self):
        return self.customer








