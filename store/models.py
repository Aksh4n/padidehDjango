from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    last = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200 , null=True)
    email = models.CharField(max_length=200 , null=True)
    def __str__(self):
        return str(self.user)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

post_save.connect(create_customer, sender=User)

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

    def __str__(self):
        return self.description


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    price_before = models.FloatField(null=True, blank=True)
    inventory = models.IntegerField(default=0)
    info = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True)
    last_update = models.DateTimeField()
    image = models.ImageField(null=True,blank=True)
    
    promotions = models.ForeignKey(Promotion , blank=True , null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url            
            

class ExtraImage(models.Model):
    rel = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField()
    def __str__(self):

        return str(self.rel)


class Option(models.Model):
    rel = models.ForeignKey(Product, on_delete=models.CASCADE)
    op1 = models.CharField(max_length=200, null=True, blank=True) 
    op2 = models.CharField(max_length=200, null=True, blank=True)
    op3 = models.CharField(max_length=200, null=True, blank=True)
    op4 = models.CharField(max_length=200, null=True, blank=True)
    op5 = models.CharField(max_length=200, null=True, blank=True)   
    def __str__(self):
        return str(self.rel)



class Order(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.TextField(max_length=1000)
    postal_code = models.CharField(max_length=200)
    items = models.TextField(max_length=1000)
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.DecimalField(null=True, decimal_places=12 , max_digits=24)
    complete = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total        
    @property
    def get_cart_options(self):
        orderitems = self.orderitem_set.all()
        total = (item.product.option_set.all() for item in orderitems)
        return total            

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    option = models.CharField(max_length=200, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str([self.product , self.quantity , self.option])
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
class Star(models.Model):
    star = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return str(self.star)
class Contact(models.Model):
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)



    def __str__(self):

        return self.subject  

class CustomOrder(models.Model):
    phone = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True)
    message = models.TextField(max_length=1000)
    image = models.ImageField()



    def __str__(self):

        return self.name  
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url            

class Honor(models.Model):
    subject = models.CharField(max_length=200)
    img = models.ImageField()


    def __str__(self):

        return self.subject  
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url            
class Project(models.Model):
    subject = models.CharField(max_length=200)
    img = models.ImageField()


    def __str__(self):

        return self.subject  
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url            
