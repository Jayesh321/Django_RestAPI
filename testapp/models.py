from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    auther = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


