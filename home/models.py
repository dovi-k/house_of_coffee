from django.db import models

# Create your models here.

class HomePage(models.Model):
    title = models.CharField(max_length=64, null=False)
    button_text = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.button_text
