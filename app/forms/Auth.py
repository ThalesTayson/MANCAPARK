from django import forms
from django.contrib.auth import authenticate

class formAuthenticate(forms.Form):
    usuario = forms.CharField(max_length=50)
    senha = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(formAuthenticate, self).__init__(*args, **kwargs)

    def clean(self) -> dict[str, any]:
        data = super().clean()
        
        user = authenticate(self.request, username=data.get(
            "usuario"), password=data.get("senha"))
        
        if user is None:
            raise forms.ValidationError("Usuário e/ou senha inválido(s).",
                                        code='usuario_ou_senha_invalidos',
                                        ) 
        self.user = user
        
        return data

    def login(self):
        return self.user
