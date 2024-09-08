from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    category = models.CharField(max_length=100)  # restaurant, doctor, lawyer

    def __str__(self):
        return self.name
