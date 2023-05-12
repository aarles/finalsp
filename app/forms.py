from django.forms import ModelForm
from app.models import Perguntas
# Create the form class.
class PergForm(ModelForm):
        class Meta:
             model = Perguntas
             fields = ["pergunta", "resposta", "autor", "resp"]