from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name