from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from servise.service import upload_image_product


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'category_product',
            kwargs={
                'category_slug': self.slug
            }
        )


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(upload_to=upload_image_product,
                              blank=True)
    description = models.TextField(max_length=1000)
    aviable = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    measure = models.CharField(max_length=50, null=True, default='unit')
    amount = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('title',)
        index_together = ('id', 'slug')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'product_detail',
            kwargs={
                # 'id': self.id,
                'slug': self.slug
            }
        )
