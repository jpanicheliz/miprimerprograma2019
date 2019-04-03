numero_a_adivinar = input("Elige un numero a adivinar entre 0 y 20 (que tu companero no lo vea):")

numero_adivinado = input("Adivina el numero:")

while numero_a_adivinar != numero_adivinado:
    numero_adivinado = input("Adivina el numero")

if numero_adivinado == numero_a_adivinar:
    print("Lo has adivinado")

