from django import forms
from .models import User

class RegisterForm(forms.Form): 
    email = forms.EmailField(label='Email:',
                    required=True,
                    widget=forms.EmailInput(attrs={
                            'class':'form-control', 
                            'placeholder':'example@ucab.edu.ve',
                        }
                        ))

    password = forms.CharField(label='Contraseña:',
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class':'form-control',
                                }
                                ))

    password2 = forms.CharField(label='Confirma la contraseña:',
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class':'form-control',
                                }
                                ))



    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo ya se encuentra en uso')
        return email
   

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') !=  cleaned_data.get('password'):
            self.add_error('password2', 'La contraseña no coincide')

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),)

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email:',
                                required=True,
                                widget=forms.EmailInput(attrs={
                                    'class':'form-control', 
                                })
    )

    password = forms.CharField(label='Contraseña:',
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class':'form-control',
                                })
    )