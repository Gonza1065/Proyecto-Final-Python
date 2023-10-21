# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm, CrearProductoForm, ActualizarProductoForm
from .models import Gorra, Remera, Pantalon, Producto


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = SignUpForm()
    return render(request, "proyectoApp/registro.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/inicio.html")
    else:
        form = LoginForm()
    return render(request, "proyectoApp/login.html", {"form": form})


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")


@login_required
def inicio_view(request):
    return render(request, "proyectoApp/inicio.html")


@login_required
def gorras_view(request):
    gorras = Gorra.objects.all()
    return render(request, "proyectoApp/gorras.html", {"gorras": gorras})


@login_required
def remeras_view(request):
    remeras = Remera.objects.all()
    return render(request, "proyectoApp/remeras.html", {"remeras": remeras})


@login_required
def pantalones_view(request):
    pantalones = Pantalon.objects.all()
    return render(request, "proyectoApp/pantalones.html", {"pantalones": pantalones})


@login_required
def ver_detalles_gorras_view(request, id):
    gorra = Gorra.objects.get(id=id)
    return render(request, "proyectoApp/ver_detalles_gorra.html", {"gorra": gorra})


@login_required
def ver_detalles_remeras_view(request, id):
    remera = Remera.objects.get(id=id)
    return render(request, "proyectoApp/ver_detalles_remera.html", {"remera": remera})


@login_required
def ver_detalles_pantalones_view(request, id):
    pantalon = Pantalon.objects.get(id=id)
    return render(
        request, "proyectoApp/ver_detalles_pantalon.html", {"pantalon": pantalon}
    )


@login_required
def crear_producto(request):
    if request.method == "POST":
        form = CrearProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user
            producto.save()
            return redirect("/mis_productos")
    else:
        form = CrearProductoForm()
    return render(request, "proyectoApp/crear_producto.html", {"form": form})


@login_required
def mis_productos_view(request):
    productos = Producto.objects.filter(usuario=request.user)
    username = request.user.username
    return render(
        request,
        "proyectoApp/mis_productos.html",
        {"productos": productos, "username": username},
    )


@login_required
def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == "POST":
        form = ActualizarProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("mis_productos")
    else:
        form = ActualizarProductoForm(instance=producto)

    return render(request, "proyectoApp/actualizar_producto.html", {"form": form})


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == "POST":
        producto.delete()
        return redirect("mis_productos")

    return render(
        request, "proyectoApp/confirmar_eliminar_producto.html", {"producto": producto}
    )


def acerca_de_mi(request):
    return render(request, "proyectoApp/acerca_de_mi.html")
