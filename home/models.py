from django.db import models



# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.email)