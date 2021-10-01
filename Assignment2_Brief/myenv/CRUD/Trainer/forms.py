from django import forms
from .models import Trainer

#form for trainer connected with model trainer

class TrainerForm(forms.ModelForm):

    class Meta:
        model = Trainer
        fields = ['name', 'lastname', 'subject', 'courses']
