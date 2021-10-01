from django.db import models

#model for the trainer

class Trainer(models.Model): 
    name = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 150)
    courses = models.CharField(max_length = 300)
