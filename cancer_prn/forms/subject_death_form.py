from ..models import SubjectDeath
from django import forms


class SubjectDeathForm(forms.ModelForm):

    class Meta:
        model = SubjectDeath
        fields = '__all__'
