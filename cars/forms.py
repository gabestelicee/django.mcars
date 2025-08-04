from django import forms 
from cars.models import Car

    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


def clean_value(self):
    value = self.cleaned_data.get('value')
    if value is None:
        self.add_error('value', 'Erro. Digite novamente o valor do carro.')
    return value
