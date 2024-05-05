from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label= "Password",
         strip= False, #Pour desactiver la suppression automatique des spaces au tour du MDP 
        widget=forms.PasswordInput(attrs={'autocomplete' : 'new-password'}),
)  
    password2 = forms.CharField(
        label="Password confirmation",#Confirmation du MDP
        widget= forms.PasswordInput(attrs={'autocomplete' : 'new-password'}),
        strip=False,
 )
    class Meta(UserCreationForm.Meta):#Pour personnaliser les options du formulaire 
        fields = UserCreationForm.Meta.fields + ("password1","password2")