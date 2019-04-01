
operacion_a_realizar = input("Bienvenido a la calculadora de Python, que operacion quieres realizar (multiplicar / dividir / sumar / restar)? :")

while operacion_a_realizar != "multiplicar" and operacion_a_realizar != "dividir" and operacion_a_realizar != "sumar" and operacion_a_realizar != "restar":
    print("La operacion elegida no existe en esta calculadora")
    operacion_a_realizar = input("Por favor, elije una de las siguientes operaciones (multiplicar / dividir / sumar / restar):")

primer_numero = float(input("Cual es el primer numero con el que quieres operar?: "))

segundo_numero = float(input("Cual es el segundo numero con el que quieres operar?: "))

if operacion_a_realizar == "multiplicar":
    print("El resultado de tu operacion es:")
    print(primer_numero * segundo_numero)
elif operacion_a_realizar == "dividir":
    print("El resultado de tu operacion es:")
    print(primer_numero / segundo_numero)
elif operacion_a_realizar == "sumar":
    print("El resultado de tu operacion es:")
    print(primer_numero + segundo_numero)
elif operacion_a_realizar == "restar":
    print("El resultado de tu operacion es:")
    print(primer_numero - segundo_numero)
