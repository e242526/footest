from django.db import models
from django.urls import reverse

# Create your models here.

class Biz(models.Model):
    """Biz class model."""

    title = models.CharField(max_length=200)                                     

    def __str__(self):                                                           
        """String for representing the Task object."""                               

        return self.title                                                        

    # Todo: Is this really needed?                                               
    def display_title(self):                                                     
        """Creates a string for the Title. This is required to display title in Admin."""    

        return self.title                                                        

