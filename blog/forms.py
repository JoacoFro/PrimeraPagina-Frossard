from django import forms

class AutorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    profesion = forms.CharField(max_length=30)

class ArticuloFormulario(forms.Form):
    titulo = forms.CharField(max_length=30)
    seccion = forms.CharField(max_length=40) 
    texto = forms.CharField(widget=forms.Textarea) 
    fecha = forms.DateField(
        widget=forms.TextInput(attrs={'placeholder': 'Ej: AAAA-MM-DD'})
    )
    
class SeccionFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)