from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Perguntas(models.Model):
    pergunta = models.TextField(null=True, blank=True)
    resposta = models.TextField(null=True, blank=True)
    autor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True, related_name="autor")
    resp = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True, related_name="resp")
 
