from django.shortcuts      import render, redirect
from django.db.models      import Q
from django.core.paginator import Paginator
from .forms                import CarForm
from .models               import Car
from django.contrib        import messages
from App_Register.models   import Avatar
from django.views.generic  import DeleteView, UpdateView

from django.utils.decorators        import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

#Vista para la creación de vehículos (solo administradores)
# @method_decorator(login_required, name='dispatch')
def CarCreate(request):

    if(request.method=="POST"):
        carformulario = CarForm(request.POST, request.FILES)
        if(carformulario.is_valid()):
            data=carformulario.cleaned_data
            car = Car(
                categoria=data["categoria"],
                tipo=data["tipo"],
                marca=data["marca"],
                modelo=data["modelo"],
                placa=data["placa"],
                annio=data["annio"],
                tipo_caja=data["tipo_caja"],
                combustible=data["combustible"],
                cantidad_pasajeros=data["cantidad_pasajeros"],
                numero_puertas=data["numero_puertas"],
                imagen=data["imagen"],
                control_crucero=data["control_crucero"],
                radio=data["radio"],
                aacond=data["aacond"],
                bluetooth=data["bluetooth"],
                cierrepuertas=data["cierrepuertas"]
            )
            car.save()
            messages.success(request, 'El vehículo fue creado con éxito!')
            
            return render(request, "CarCreate.html")
    else:
        carformulario=CarForm()

    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, "CarCreate.html", {"carformulario":carformulario, "url":avatar.avatar.url})
    except:
        return render(request, "CarCreate.html", {"carformulario":carformulario})

#Vista para ver una tabla con todos los vehículos de la base de datos (solo administradores)
# @method_decorator(login_required, name='dispatch')
def CarTable(request):
    cars     = Car.objects.all()
    contexto = {"cars": cars}

    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, "CarTable.html", {"cars": cars, "url":avatar.avatar.url})
    except:
        return render(request, "CarTable.html", contexto)

@method_decorator(login_required, name='dispatch')
class CarDelete(DeleteView):
    model         = Car
    template_name = "CarDelete.html"
    success_url   = "/car/table"

@method_decorator(login_required, name='dispatch')
class CarUpdate(UpdateView):
    model         = Car
    template_name = "CarEdit.html"
    fields        = "__all__"
    success_url   = "/car/table"

def CarList(request):

    listado_cars  = Car.objects.all()
    paginator     = Paginator(listado_cars,3)
    pagina        = request.GET.get("page") or 1
    cars          = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas       = range(1, cars.paginator.num_pages + 1)
    contexto      = {"cars": cars, "paginas":paginas, "pagina_actual":pagina_actual}
    busqueda      = request.GET.get("buscar")

    if(busqueda):

        listado_cars = Car.objects.filter(
            Q(marca__icontains=busqueda) |
            Q(modelo__icontains=busqueda) 
        ).distinct()

        paginator = Paginator(listado_cars,3)
        pagina    = request.GET.get("page") or 1
        cars      = paginator.get_page(pagina)

        if(len(cars)==0):
            return render(request, "CarNotFound.html")

        pagina_actual = int(pagina)
        paginas       = range(1, cars.paginator.num_pages + 1)
        contexto      = {"cars": cars, "paginas":paginas, "pagina_actual":pagina_actual,"busqueda":busqueda}

        return render(request, "CarList.html", contexto )

    return render(request, "CarList.html", contexto )
    
def CarDetail(request, id):
    cars     = Car.objects.filter(id=id)
    contexto = {"cars": cars}
    return render(request, "CarDetail.html", contexto)