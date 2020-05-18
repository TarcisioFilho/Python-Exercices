#Faça um conversor de temperatura de C para K e F
# Exercicio 10 -- 014

C = float(input("Digite a temperatura em C: "))
K = C+273
F = C*1.8 + 32
print(" {} Graus equivale a {:.1f} Fahrenheit e {} Kelvins ".format(C, F, K))


