from django.db import models

class Chat_answers(models.Model):
    Answer = models.CharField(max_length=20000)

# Create your models here.
    