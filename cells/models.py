from django.db import models
import uuid


# Create your models here.
class series(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return 'seria: ' + str(self.number)


class pack(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1(), editable=False)
    piles = models.IntegerField()
    startDate = models.DateField(auto_now=True)
    retiret = models.BooleanField(default=False)
    series = models.ForeignKey(series, on_delete=models.CASCADE)
    capacity = models.IntegerField()


    def __str__(self):
        return "piles: " + str(self.piles) + ' del: ' + str(self.startDate) +" en la seria: " + str(self.series)