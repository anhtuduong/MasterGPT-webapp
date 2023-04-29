from django.db import models
from MasterGPT.core.Chat import Chat

chat = Chat()
chat.start()

class ChatDB(models.Model):
    message = models.TextField()
    response = models.TextField()
