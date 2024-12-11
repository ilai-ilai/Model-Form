from raja.models import data
from django import forms

class registerform(forms.ModelForm):
    class Meta:
        model= data
        fields=['name','contact','address','mail']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'mail':forms.TextInput(attrs={'class':'form-control'}),

        }
