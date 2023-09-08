from django import forms

class ContactForm(forms.Form):
    firstname=forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'placeholder':'Nombre...'}
    ))
    lastname=forms.CharField(label="Apellido", required=True, widget=forms.TextInput(
        attrs={'placeholder':'Apellido...'}
    ))
    email=forms.EmailField(label="Correo", required=True, widget=forms.EmailInput(
        attrs={'placeholder':'Correo...'}
    ))
    nickname=forms.CharField(label="Apodo", required=True, widget=forms.TextInput(
        attrs={'placeholder':'Apodo...'}
    ))
    commentary=forms.CharField(label="Comentarios", required=True, widget=forms.Textarea(
        attrs={'placeholder':'Comentarios...'}
    ), min_length=10, max_length=1000)
