from django import forms
from .models import Army

class ArmyForm(forms.ModelForm):
    class Meta:
        model = Army
        fields = ['commander_name', 'faction', 'left_army', 'center_army', 'right_army']
