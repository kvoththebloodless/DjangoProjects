from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()
    number=models.IntegerField(blank=True, null=True)

    def __str__(self):
        """A string rep"""

        return self.text[:50]