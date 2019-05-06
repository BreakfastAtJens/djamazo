from django.forms import ModelForm, TextInput
from .models import Ip 

class IpForm(ModelForm):
    class Meta:
        model = Ip 
        fields = ['address']
        widgets = {'address' : TextInput(attrs={'class' : 'input', 'placeholder' : 'IP Address'})}
