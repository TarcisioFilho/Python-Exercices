# Leia largura e altura de uma parede em metros, calcule a área e a quantidade de tinta pra pintar.
# Cada litro de tinta pinta uma area de 2m²
L = float(input("Digite a largura da parede em metros: "))
A = float(input("Digite a altura da parede em metros: "))
AR = (L*A)
print(" Largura da parede : {} \n Altura da parede : {} \n Area : {} \n".format(L, A, AR))
litros = AR/2
print("A quantidade necessária de litros de tinta para pintar uma parede de {} m² é de {} litros.".format(AR, litros))




