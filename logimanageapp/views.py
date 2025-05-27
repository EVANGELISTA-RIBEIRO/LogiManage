from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from logimanageapp.forms import LoginForm, RegistroForm

def registro_view(request):
    form = RegistroForm(
        initial={
            "username": "",
            "email": "",
            "senha": "",
            "confirmar_senha": ""
        })
    return render(request, "logimanageapp/views/registro.html", {"form": form})

def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["senha"])
            user.save()
            login(request, user)
            return redirect("login")
    else:
        form = RegistroForm()

    return render(request, "logimanageapp/views/registro.html", {"form": form})

def login_view(request):
    form = LoginForm(
        initial={
            "email": "",
            "password": ""
        })
    return render(request, "logimanageapp/views/login.html", {"form": form})

def logar_usuario(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                form.add_error(None, "Usuário ou senha inválidos")

    else:
        form = LoginForm()

    return render(request, "logimanageapp/views/login.html", {"form": form})

def home_view(request):
    return render(request, "logimanageapp/views/home.html")

def requisicao_view(request):
    return render(request, "logimanageapp/views/requisicao.html")