#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input("Quantos KM rodados : "))
dias = int(input("Quantos dias o carro foi alugado: "))
pago = (km * 0.15) + (dias * 60)
print(" O total a pagar será R$ {}".format(pago))

#Dificil interpretação...
