from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PizzaFormulario(forms.Form):
    TAMANIO_OPCIONES = (
    (1, "Individual"),
    (2, "Grande"),
    (3, "Familiar"),
    )
  
    nombre = forms.CharField(max_length=30)
    foto = forms.CharField(max_length=9999999)
    tamanio = forms.ChoiceField(choices=TAMANIO_OPCIONES)
    ingredientes = forms.CharField(max_length=60)
    precio = forms.IntegerField() 

class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repite la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        print(model)
        fields = ['username', 'password1', 'password2']
        help_texts= {k:"" for k in fields}