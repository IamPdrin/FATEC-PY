from django import forms 
from appHome.models import Usuario

#define o formulário
class FormUsuario(forms.ModelForm):
    #dados do formulário
    class Meta:
        #modelo utilizado
        model = Usuario
        #campos que devem aparecer no form
        fields = ('nome', 'email')
