from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True)
    password = models.TextField()
    profilepic= models.ImageField(upload_to="images/profiles")

    def __str__(self):
        return str(self.name)
