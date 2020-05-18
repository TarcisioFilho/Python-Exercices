import random
print("Gerador de arsenal")
print("Escolha entre 4 armas primarias")
armap1 = str(input("Digite o nome de uma arma primaria: "))
armap2 = str(input("Digite uma segunda arma primaria: "))
armap3 = str(input("Digite uma terceira arma primaria: "))
armap4 = str(input("Digite uma quarta arma primaria: "))
lista1 = [armap1, armap2, armap3, armap4]
armap1esc = random.choice(lista1)
print("Sua arma primária será {}".format(armap1esc))
















