from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

Usuario = get_user_model()

def register_user(request): # Registro de usuario
    erro = None
    if request.method == "POST":
        nome = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        numero = request.POST.get("numero")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if not nome or not cpf or not numero or not email or not password1:
            erro = "Preencha todos os campos."
        elif password1 != password2:
            erro = "As senhas não conferem."
        elif Usuario.objects.filter(cpf=cpf).exists():
            erro = "Já existe um usuário com esse CPF."
        elif Usuario.objects.filter(numero=numero).exists():
            erro = "Já existe um usuário com esse número."
        elif Usuario.objects.filter(email=email).exists():
            erro = "Já existe um usuário com esse email."
        else:
            user = Usuario.objects.create_user(
                nome = nome,
                cpf = cpf,
                numero = numero,
                email = email,
                password = make_password(password1)
            )

            user.save()

            login(request, user)
            return redirect("perfil")
        
        return render(request, "enter.html", {"erro": erro})

def login_user(request): # Login de usuario
    erro = None
    if request.method == "POST":
        cpf = request.POST.get("cpf")
        password = request.POST.get("password")

        user = authenticate(request, cpf=cpf, password=password)
        if user is not None:
            login(request, user)
            return redirect("perfil")
        else:
            erro = "Login inválido"

    return render(request, "enter.html", {"erro": erro})

def logout_user(request): # Logout de usuario
    logout(request)
    return redirect("enter")

@login_required
def perfil(request): # Perfil do usuario
    return render(request, "perfil.html")

def home(request):
    return render(request, "home.html")

def enter(request):
    return render(request, "enter.html")