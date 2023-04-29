from django.db import models
from core.mastergpt.Chat import Chat

class ChatDB(models.Model):
    message = models.TextField()
    response = models.TextField()
