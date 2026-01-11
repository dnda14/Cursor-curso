while True:
    operacion = input("Introduce una operación (suma, resta, multiplicación, división) o 'salir' para terminar: ").lower()
    
    if operacion == "salir":
        print("¡Hasta luego!")
        break
    
    if operacion not in ["suma", "resta", "multiplicación", "multiplicacion", "división", "division"]:
        print("Operación no válida. Por favor, introduce: suma, resta, multiplicación o división.")
        continue
    
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
    except ValueError:
        print("Error: Debes introducir números válidos.")
        continue
    
    if operacion == "suma":
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif operacion == "resta":
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif operacion in ["multiplicación", "multiplicacion"]:
        resultado = num1 * num2
        print(f"Resultado: {num1} × {num2} = {resultado}")
    elif operacion in ["división", "division"]:
        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado = num1 / num2
            print(f"Resultado: {num1} ÷ {num2} = {resultado}")
    
    print()  # Línea en blanco para mejor legibilidad
