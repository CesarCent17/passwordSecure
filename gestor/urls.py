from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='gestor/login.html'), name='login'),
    path('logout/',logout_then_login, name='logout'),
    path('registro/',views.registro, name='registro'),
    path('nuevacontrasena/', views.nueva_passw, name='nuevacontrasena'),
    path('edicioncontrasena/<int:id_contrasena>', views.edicion_passw, name='edicioncontrasena'),
    path('editarcontrasena/<int:id_contrasena>', views.editar_passw, name='editarcontrasena'),
    path('eliminarcontrasena/<int:id_contrasena>', views.eliminar_passw, name='eliminarcontrasena'),
    #path('logout/', LogoutView.as_view(template_name='gestor/logout.html'), name='logout'),
]
