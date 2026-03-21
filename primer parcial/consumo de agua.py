#pedir al usario que ingrese su nombre
nombre = input("Ingrese su nombre: ")
consumo = int(input("Ingrese su consumo mensual de agua en m³:"))
#pedir al usario que ingrese su consumo de agua en metros cubicos
if consumo <= 0:
    print("Error: el consumo debe ser un número positivo.")
else:
    if consumo <= 15:
        categoria = "Bajo"
        mensaje = "Su consumo es eficiente. ¡Buen trabajo!"
    elif consumo <= 30:
        categoria = "Medio"
        mensaje = "Su consumo es moderado. Puede mejorar."
    else:
        categoria = "Alto"
        mensaje = "Su consumo es alto. Considere ahorrar agua."
   
    print("Nombre:", nombre)
    print("Categoría:", categoria)
    print("Mensaje:", mensaje)
