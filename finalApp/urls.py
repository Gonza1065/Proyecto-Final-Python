from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static

from .views import (
    login_view,
    signup_view,
    inicio_view,
    gorras_view,
    ver_detalles_gorras_view,
    remeras_view,
    ver_detalles_remeras_view,
    pantalones_view,
    ver_detalles_pantalones_view,
    crear_producto,
    mis_productos_view,
    actualizar_producto,
    eliminar_producto,
    CustomLogoutView,
    acerca_de_mi,
)

urlpatterns = [
    path("", login_view, name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("signup/", signup_view, name="signup"),
    path("inicio/", inicio_view, name="inicio"),
    path("inicio.html", inicio_view),
    path("gorras/", gorras_view, name="gorras"),
    path(
        "ver-detalles_gorra/<int:id>/",
        ver_detalles_gorras_view,
        name="ver_detalles_gorra",
    ),
    path("remeras/", remeras_view, name="remeras"),
    path(
        "ver-detalles-remera/<int:id>/",
        ver_detalles_remeras_view,
        name="ver_detalles_remera",
    ),
    path("pantalones/", pantalones_view, name="pantalones"),
    path(
        "ver-detalles-pantalon/<int:id>/",
        ver_detalles_pantalones_view,
        name="ver_detalles_pantalon",
    ),
    path("productos/crear/", crear_producto, name="crear_producto"),
    path("mis_productos/", mis_productos_view, name="mis_productos"),
    path(
        "productos/actualizar/<int:id>/",
        actualizar_producto,
        name="actualizar_producto",
    ),
    path("productos/eliminar/<int:id>/", eliminar_producto, name="eliminar_producto"),
    path("acerca_de_mi/", acerca_de_mi, name="acerca_de_mi"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
