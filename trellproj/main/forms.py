from django.forms import ModelForm
from .models import movies

class addmovieform(ModelForm):
    class Meta:
        model=movies
        fields= ['name', 'description', 'direction', 'duration']