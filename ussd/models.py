from django.db import models

# Create your models here.


class Sajili(models.Model):
    full_name = models.CharField(max_length=100,)
    phone_number = models.CharField(max_length=15,)
    balance = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    pin = models.CharField(max_length=100,)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = "Sajili"
        verbose_name_plural = "Sajili"

    def __str__(self):
        return self.full_name

    
