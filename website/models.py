from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    content = models.TextField()
    deleted = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='posts', blank=True, null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name 


class Experience(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50)
    description = models.TextField()
    yers = models.CharField(max_length=50)

    def __str__(self):
        return self.title 