from django.db import models

# Create your models here.
class News(models.Model):
    headlines = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.headlines

