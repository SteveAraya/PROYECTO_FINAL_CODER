from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import CarForm
from .models import Car
from django.contrib import messages

from django.views.generic import DeleteView, UpdateView

#NUEVA VERSION
# Create your views here.

#Vista para la creación de vehículos (solo administradores)
def CarCreate(request):
    if(request.method=="POST"):
        carformulario=CarForm(request.POST, request.FILES)
        if(carformulario.is_valid()):
            data=carformulario.cleaned_data
            car=Car(categoria=data["categoria"],tipo=data["tipo"],marca=data["marca"],modelo=data["modelo"],placa=data["placa"],annio=data["annio"],
                    tipo_caja=data["tipo_caja"],combustible=data["combustible"],cantidad_pasajeros=data["cantidad_pasajeros"],
                    numero_puertas=data["numero_puertas"],imagen=data["imagen"],control_crucero=data["control_crucero"],radio=data["radio"],aacond=data["aacond"],bluetooth=data["bluetooth"],cierrepuertas=data["cierrepuertas"])
            car.save()
            messages.success(request, 'El vehículo fue creado con éxito!')
            return render(request, "CarCreate.html")
    else:
        carformulario=CarForm()
    return render(request, "CarCreate.html", {"carformulario":carformulario})

#Vista para ver una tabla con todos los vehículos de la base de datos (solo administradores)
def CarTable(request):
    cars=Car.objects.all()
    contexto={"cars": cars}
    return render(request, "CarTable.html", contexto )

class CarDelete(DeleteView):
    model=Car
    template_name="CarDelete.html"
    success_url="/car/table"

class CarUpdate(UpdateView):
    model=Car
    template_name="CarEdit.html"
    fields="__all__"
    success_url="/car/table"

# def CarEdit(request, id):
#     car=Car.objects.get(id=id)
#     if(request.method=="POST"):
#         carformulario=CarForm(request.POST, request.FILES)
#         if(carformulario.is_valid()):
#             data=carformulario.cleaned_data
#             car.categoria=data["categoria"]
#             car.tipo=data["tipo"]
#             car.marca=data["marca"]
#             car.modelo=data["modelo"]
#             car.placa=data["placa"]
#             car.annio=data["annio"]
#             car.tipo_caja=data["tipo_caja"]
#             car.combustible=data["combustible"]
#             car.cantidad_pasajeros=data["cantidad_pasajeros"]
#             car.numero_puertas=data["numero_puertas"]
#             car.imagen=data["imagen"]
#             car.radio=data["radio"]
#             car.aacond=data["aacond"]
#             car.bluetooth=data["bluetooth"]
#             car.cierrepuertas=data["cierrepuertas"]
#             car.save()
#     else:
#         carformulario=CarForm(initial={
#             "categoria":car.categoria,
#             "tipo":car.tipo,
#             "marca":car.marca,
#             "modelo":car.modelo,
#             "placa":car.placa,
#             "annio":car.annio,
#             "tipo_caja":car.tipo_caja,
#             "combustible":car.combustible,
#             "cantidad_pasajeros":car.cantidad_pasajeros,
#             "numero_puertas":car.numero_puertas,
#             "imagen":car.imagen,
#             "radio":car.radio,
#             "aacond":car.aacond,
#             "bluetooth":car.bluetooth,
#             "cierrepuertas":car.cierrepuertas,
#         })
#     print(carformulario)
#     return render(request, "CarEdit.html", {"carformulario":carformulario, "id":car.id})


def CarList(request):
    listado_cars=Car.objects.all()
    paginator=Paginator(listado_cars,3)
    pagina=request.GET.get("page") or 1
    cars=paginator.get_page(pagina)
    pagina_actual=int(pagina)
    paginas=range(1, cars.paginator.num_pages + 1)
    contexto={"cars": cars, "paginas":paginas, "pagina_actual":pagina_actual}
    busqueda=request.GET.get("buscar")
    if(busqueda):
        listado_cars=Car.objects.filter(
            Q(marca__icontains=busqueda) |
            Q(modelo__icontains=busqueda) 
        ).distinct()
        paginator=Paginator(listado_cars,2)
        pagina=request.GET.get("page") or 1
        cars=paginator.get_page(pagina)
        if(len(cars)==0):
            return render(request, "CarNotFound.html")
        pagina_actual=int(pagina)
        paginas=range(1, cars.paginator.num_pages + 1)
        contexto={"cars": cars, "paginas":paginas, "pagina_actual":pagina_actual,"busqueda":busqueda}
        return render(request, "CarList.html", contexto )
    return render(request, "CarList.html", contexto )
    
def CarDetail(request, id):
    cars=Car.objects.filter(id=id)
    contexto={"cars": cars}
    return render(request, "CarDetail.html", contexto)