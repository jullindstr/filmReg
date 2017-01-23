from django.db import models

class Films(models.Model):
    film_id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    ref_to_img = models.TextField()
    added_date = models.DateField()
    returned_date = models.DateField()
    rating = models.IntegerField(default=0)
    aviable = models.CharField(max_length=30) #name of the user who borrowed the film, or 'yes'

    def __str__(self):
        return self.title

class Users(models.Model):
    user_name = models.CharField(max_length=30, primary_key=True)
    pessword = models.CharField(max_length=30)

    def __str__(self):
        return self.user_name
