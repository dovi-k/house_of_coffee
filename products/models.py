from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
     
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Syrup(models.Model):
      
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Origin(models.Model):
      
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    syrup = models.ForeignKey('Syrup', null=True, blank=True,
                              on_delete=models.SET_NULL)
    origin = models.ForeignKey('Origin', null=True, blank=True,
                              on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=254, blank=True)
    description = models.TextField()
    cup_size = models.BooleanField(default=False, null=True, blank=True)
    group = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    unit_of_measure = models.CharField(max_length=25, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
