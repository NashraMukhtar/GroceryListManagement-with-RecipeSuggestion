from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Product)
    instructions = models.TextField()
