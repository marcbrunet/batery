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

    def __str__(self):
        return "piles: " + str(self.piles) + ' del: ' + str(self.startDate) +" en la seria: " + str(self.series)

class evaluation(models.Model):
    startDate = models.DateField(auto_now=True)
    pack_id = models.ForeignKey(pack, on_delete=models.CASCADE)
    capacyti = models.IntegerField()

    def __str__(self):
        return 'date: ' + str(self.startDate) + ' pak: ' + str(self.pack_id) + ' capacitat: ' + str(self.capacyti)

