
pokemon_elegido = input("Contra que pokemon quieres combatir? (Squirtle / Charmander / Bulbasaur): ")

vida_pikachu = 100
vida_enemigo = 0


if pokemon_elegido == "Squirtle":
    vida_enemigo = 90

elif pokemon_elegido == "Charmander":
    vida_enemigo = 80

elif pokemon_elegido == "Bulbasaur":
    vida_enemigo = 100


while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("Que ataque vas a utilizar? (Chispazo / Bola voltio):")

    if ataque_elegido == "Chispazo":
        vida_enemigo -= 10
    if ataque_elegido == "Bola voltio":
        vida_enemigo -= 12

    print("La vida del enemigo es de {}".format(vida_enemigo))

    if pokemon_elegido == "Squirtle":
        print("Squirtle te hace un ataque de 8 de dano")
        vida_pikachu -= 8

    if pokemon_elegido == "Charmander":
        print("Charmander te hace un ataque de 7 de dano")
        vida_pikachu -= 7

    if pokemon_elegido == "Bulbasaur":
        print("Bulbasaur te hace un ataque de 10 de dano")
        vida_pikachu -= 10

    print("La vida de Pikachu es de {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("!Has ganado!")
if vida_pikachu <= 0:
    print("Has perdido!")

print("El combate ha terminado")



