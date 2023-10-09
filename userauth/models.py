from django.db import models

# Create your models here.
class Trader(models.Model):
    name = models.CharField(max_length=400, unique=True)
    balance = models.IntegerField(default=100)

    def __str__(self):
        return self.name






class TraderData(models.Model):
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    profit_loss = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)



    
