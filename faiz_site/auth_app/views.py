from django.shortcuts import render, redirect
from  django.contrib.auth.forms import UserCreationForm
from .form import CustomUserCreationForm
from django.contrib.auth import login, authenticate ,logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

#Fonction d'inscription 
def inscription(request):#Fonction d'inscription 
    if request.method == 'POST': # Verification si la methode http est de type post 
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): # Si les donnés du formulaire sont valide
            form.save() # Permet  d'enrigister les donnés dans la basse de donné
            return redirect('connexion')
    else :
        form = CustomUserCreationForm() 
    return render(request , 'inscription.html',{'form':form})  



# Fonction de connexion 
def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username , password=password)# LA FONCTION AUTHENTICATE est une fonction deja defiie dans django
        if user is not None :
            login(request , user) # C'est pour connecter l'utilisteur 
            return redirect('acceuil')# rediriger vers acceuil
        else :
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render (request , 'connexion.html')   


@login_required
# Fonction Acceuil
def acceuil(request):
    return render(request,'acceuil.html')


def deconnexion(request):
    logout(request) 
    return redirect('connexion')