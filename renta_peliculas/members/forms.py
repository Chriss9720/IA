from django.forms import ModelForm

from .models import Members

class Form(ModelForm):

    class Meta:
        model = Members
        fields = '__all__'
        labels = {
            'firstname': 'Nombre',
            'lastname': 'Apellidos'
        }

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.fields['lastname'].required = False