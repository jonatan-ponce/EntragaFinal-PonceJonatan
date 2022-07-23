from django.urls import path
from PizzeriaManuel import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('pizzas', views.pizzas, name="Pizzas"),
    path('formulario', views.crearPizza, name="Formulario"),
    path('buscarPizza',views.buscarPizza, name="BuscarPizza"),
    path('buscar/',views.buscar),
    path('login',views.login_request, name='login'),
    path('register',views.register, name='register'),
    path('about',views.about,name="about"),
    ]