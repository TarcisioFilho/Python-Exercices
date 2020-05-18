from math import sin, cos, tan, radians
angulo = float(input("Digite um ângulo: "))
S = sin(radians(angulo))
C = cos(radians(angulo))
T = tan(radians(angulo))
print(" O seu seno {:.2f}\n O seu cosseno {:.2f}\n A sua tangente {:.2f}".format(S, C, T))



