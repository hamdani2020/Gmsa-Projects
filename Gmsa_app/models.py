from django.db import models

# Create your models here.
class Hadith(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateField( auto_now_add=True )

    class Meta:
        pass

    def __str__(self):
        return self.title

