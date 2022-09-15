import math

def fat(i):
    fatint = 1
    while i: # "z!"
        fatint = fatint * i
        i = i - 1

    print("A fatoração do número, em fatorial inteiro padrão, é: " 
        + str(fatint))
    return fatint

print("Fatoração padrão de 4 em inteiro: " + str(fat(4)))
print("Fatoração de 4 em gamma: " + str(math.gamma(4 + 1)))
print("Fatoração padrão de 6 em inteiro: " + str(fat(6)))
print("Fatoração de 6 em gamma: " + str(math.gamma(6 + 1)))
print("Fatoração padrão de 8 em inteiro: " + str(fat(8)))
print("Fatoração de 8 em gamma: " + str(math.gamma(8 + 1)))
print("\nA fatoração da função gamma resulta nos mesmos números função fatorial simples de inteiro, a diferença é que também permite números não inteiros, como: ")
print("Fatoração de 3.2 em gamma: " + str(math.gamma(3.2 + 1)))
print("Fatoração de 5.7 em gamma: " + str(math.gamma(5.7 + 1)))

print("\nFaça um teste com qualquer número: ")
num = float(input()) # "z"

gamma = num + 1 # "(z + 1)"
fatgamma = math.gamma(gamma)
print ("A fatoração do número, por gama, é: " + str(fatgamma)) 

i = int(num)
fat(i)