from django.db import models

class movies(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    direction=models.CharField(max_length=100)
    duration=models.IntegerField()
    startTime=models.TimeField(blank=True, null=True)
    endTime=models.TimeField(blank=True, null=True)
    ticketPrice=models.IntegerField(blank=True, null=True)
    totalTickets=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

        