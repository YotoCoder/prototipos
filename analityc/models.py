from django.db import models

# Create your models here.

class Sell(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField()

    def __str__(self):
        return f'{self.amount} - {self.created_at}'
