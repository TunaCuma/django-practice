from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name} - {self.price} TL'

    class Meta:
        verbose_name_plural = 'Foods'
        ordering = ['-created_at']

class Category(models.Model):
    name = models.CharField(max_length=50)
    foods = models.ManyToManyField(Food, related_name='categories')

    def __str__(self):
        return self.name
    
    def food_count(self):
        return self.foods.count()
    
    food_count.short_description = 'Number of Foods'

    class Meta:
        verbose_name_plural = 'Categories'
    
    