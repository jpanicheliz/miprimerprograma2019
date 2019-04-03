
mi_lista = []

cosas_a_comprar = input("Que necesitas comprar? (escribe FIN al introducido todo lo que necesitas comprar:")

while cosas_a_comprar != "FIN":
    mi_lista.append(cosas_a_comprar)
    cosas_a_comprar = input("Que necesitas comprar? (escribe FIN al introducir todo lo que necesitas comprar:")

largo_lista = len(mi_lista)
indice_actual = 0

for alimento_a_comprar in mi_lista:
    print("Tengo que comprar {}".format(alimento_a_comprar))

print("Esta es la lista de la compra")



