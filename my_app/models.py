from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Restaurants(models.Model):
    title = models.CharField(max_length=155, blank=True, null=True)
    description = models.TextField()
    category_rest = models.ForeignKey('RestaurantCategory', on_delete=models.CASCADE)
    type_rest = models.ManyToManyField('RestaurantType')
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    slug = models.SlugField(max_length=250, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'
        ordering = ['-updated_at']


class RestaurantCategory(models.Model):
    title = models.CharField(max_length=155, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Restaurant Category'
        verbose_name_plural = 'Restaurant Categories'


class RestaurantType(models.Model):
    title = models.CharField(max_length=155, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Restaurant Type'
        verbose_name_plural = 'Restaurant Types'


class Products(models.Model):
    title = models.CharField(max_length=155, blank=True, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    restaurant = models.ForeignKey('Restaurants', on_delete=models.CASCADE, null=False)
    tag = models.ManyToManyField('ProductTag')
    slug = models.SlugField(max_length=250, default=None, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}, {self.price} KZT"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])


class ProductCategory(models.Model):
    title = models.CharField(max_length=155, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'
        ordering = ('title', )
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])


class ProductTag(models.Model):
    title = models.CharField(max_length=155, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product Tag'
        verbose_name_plural = 'Product Tags'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def total(self):
        cart_items = CartItem.objects.filter(cart=self)
        s = 0
        for cart_item in cart_items:
            s = s + cart_item.item.price * cart_item.count

        return s

    def __str__(self):
        return f"Cart of {self.user.username}, total: {self.total()} KZT"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.item}, {self.count} pc"
