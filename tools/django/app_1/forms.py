from django import forms
from django.core.validators import RegexValidator, MinLengthValidator



class CreatNewTask(forms.Form):
    
    #validation oh the title
    title = forms.CharField(
        label="Títle",
        max_length=100,
        validators=[
            MinLengthValidator(
                3, 
                message="El título debe tener al menos 3 caracteres"
            ),
            RegexValidator(
                regex='^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s,.!?-]+$',
                message="El título contiene caracteres no permitidos",
                code='invalid_title'
            )
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el título de la tarea'
        })
    )
    
    description = forms.CharField(
        label="Descriptión",
        required=True,  # Opcional si quieres que no sea obligatorio
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s,.!?@#$%&*()-]+$',
                message="La descripción contiene caracteres no permitidos",
                code='invalid_description'
            )
        ],
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Ingrese una descripción detallada'
        })
    )