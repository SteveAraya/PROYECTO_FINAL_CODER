# Proyecto final CoderHouse

## Estudiantes:
    Adrian Figueroa.
    Adelso Steve Araya Solórzano.

## Estructura del proyecto
### Modelo Vehiculos.
    Tipo (Sedan, SUV, Pickup, Van)
    Marca (Toyota, Suzuki, Nissan, etc)
    Modelo (Corrolla, Vitara, Rush, Hilux)
    Placa
    Annio
    TipoCaja (manual o automatico)
    Combustible (Diesel, gasolina, gas, electrico)
    CantidadPasajeros
    NumeroPuertas

### Modelo Oficina.
    Nombre (Uvita)
    Ubicacion (Contiguo al Centro Llantero, carretera principal, Bahia Ballena, Osa, Puntarenas)
    Telefono ((506) 2743-8528)
    Horario (Todos los días de 8am a 5pm.)

### Modelo Contacto.
    Asunto
    Comentario
    NombreCompleto
    CorreoElectronico

### Modelo Reservacion.
    Oficina (seria una llave foranea con el id de la oficina)
    Vehiculo (seria una llave foranea con el id de la oficina)
    FechaRetiroVehiculo
    HoraRetiroVehiculo
    FechaDevolucionVehiculo
    HoraDevolucionVehiculo
    NombreConductor
    IDConductor (Cedula o documento legal de identificación )
    Telefono
    EdadConductor

Cada reservación requiere agregar un vehiculo y una oficina en la cual el cliente
va a realizar la reserva del vehiculo. Cada modelo de Reservacion requiere un VehiculoID y
una OficinaID para poder crear la reserva.
