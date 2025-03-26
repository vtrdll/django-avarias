from django import forms
from avarias.models import Avaria

class AvariasModelForm(forms.ModelForm):

   
    class Meta:
        model = Avaria
        fields = '__all__'
    

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 1000:
            self.add_error('valor minimo deve ser de R$ 1000,00 ')
        return value



