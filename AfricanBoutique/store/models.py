from django.db import models
from django.urls import reverse

# Create your models here.
# Create Category Class Model
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    
    class Meta:
        # sort by name
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    # Get category url
    def get_urls(self):
        return reverse('products_by_category', args=[self.slug])
        
    
    # Display output
    def __str__(self):
        return self.name
    
# Create Product Class Model
class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    # Category relationship
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        # sort by name
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    def get_urls(self):
        return reverse('products_detail', args=[self.category.slug, self.slug])

    # Display output
    def __str__(self):
        return self.name
    
# Creaate Cart Product Order  model class
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table ='Cart'
        ordering =['date_added']
        
    # Display output
    def __str__(self):
        return self.cart_id
    
#  Create cart item model class
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    
    class Meta:
        db_table ='CartItem'
        
    # Calculate sub total
    def sub_total(self):
        return self.product.price * self.quantity
    
    # Display output
    def __str__(self):
        return self.product    

