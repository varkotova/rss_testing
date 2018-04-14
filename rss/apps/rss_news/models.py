from django.db import models
import datetime


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    date = models.DateField(default=str(datetime.datetime.now())[:10])

    def __str__(self):

        return str(self.id) + "_" + str(self.title)

