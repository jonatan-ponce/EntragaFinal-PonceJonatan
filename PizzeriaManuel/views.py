from django.http import HttpResponse
from django.shortcuts import render
from PizzeriaManuel.models import Pizzas
from PizzeriaManuel.forms import PizzaFormulario, UserRegisterForm

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def pizzas(self):

    pizza =  Pizzas(nombre="Especial", tamanio="Familiar", ingredientes= "Jamon , Morron, Ajo y albahaca", precio= 1300)
    pizza.save()
    documento = f"Pizza: {pizza.nombre}, Tamaño: {pizza.tamanio}, Ingredientes: {pizza.ingredientes}, Precio:{pizza.precio}"

    return HttpResponse(documento)

def inicio(request):
    pizzeriamanuel = Pizzas.objects.all()
    contexto= {'pizzas':pizzeriamanuel}   
    return render(request,"PizzeriaManuel/inicio.html",contexto)

def about(request):

    return render(request,"PizzeriaManuel/about.html")

def pizzas(request):

    pizzeriamanuel = Pizzas.objects.all()
    contexto= {'pizzas':pizzeriamanuel}

    return render(request,"PizzeriaManuel/pizzas.html", contexto)


def crearPizza(request):

   if request.method == "POST":

        miFormulario = PizzaFormulario(request.POST)

        print(miFormulario)

        if PizzaFormulario.is_valid:

           informacion = miFormulario.cleaned_data

           pizza = Pizzas (nombre=informacion['nombre'],foto=informacion['foto'], tamanio=informacion['tamanio'], ingredientes=informacion['ingredientes'], precio=informacion['precio'])

           pizza.save()

           return render(request, "PizzeriaManuel/inicio.html")    

   else:

      miFormulario= PizzaFormulario()

   return render(request,'PizzeriaManuel/formulario.html',{"miFormulario":miFormulario})    

def buscarPizza(request):

    return render(request, "PizzeriaManuel/buscarPizza.html")

def buscar(request):

    if request.GET['nombre']:
       nombre = request.GET['nombre']
       pizzas = Pizzas.objects.filter(nombre__icontains=nombre)

       return render(request,"PizzeriaManuel/resultadosBusqueda.html",{"pizzas": pizzas,"nombre":nombre})

    else:
      
      respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

#iniciamos el login
def login_request(request):
      #capturamos el post
      if request.method == "POST":
            #inicio esl uso del formulario de autenticación que me da Django
            #me toma dos parámetros el request y los datos que toma del request
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
               
                  user = authenticate(username = usuario , password = contra)
                 
                  if user is not None:
                        login(request, user)

                        return render (request, "PizzeriaManuel/inicio.html", {"mensaje": f" {usuario}"})
                  else:
                       
                        return render (request, "PizzeriaManuel/inicio.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "PizzeriaManuel/inicio.html", {"mensaje":"Usuario o contraseña Incorrecto"})
      
      #al final recuperamos el form
      form = AuthenticationForm()
    
      return render(request, "PizzeriaManuel/login.html", {'form': form})



def register(request):
      
      if request.method == "POST":

            form = UserCreationForm(request.POST)
            
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()

                  return render(request, "PizzeriaManuel/inicio.html", {"mensaje": "usuario creado"})

      else: 
            form = UserRegisterForm()

      return render(request, "PizzeriaManuel/registro.html", {"form": form})