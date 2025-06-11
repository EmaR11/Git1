dividendo = float(input("Ingrese el número a dividir (dividendo): "))
divisor = float(input("Ingrese el número por el que se va a dividir (divisor): "))

# Verificamos que el divisor no sea cero
if divisor != 0:
    resultado = dividendo / divisor
    print("El resultado de la división es:", resultado)
else:
    print("Error: No se puede dividir por cero.")