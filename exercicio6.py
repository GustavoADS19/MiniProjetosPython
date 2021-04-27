'''-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara 
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Gustavo Araujo da Silva  RA: N6648G7 – SEMESTRE: 2º Semestre
ALUNO: Veronica Thais Gomes de Oliveira RA: N664860 – SEMESTRE: 2º Semestre
ENUNCIADO: 6 - Fazer um algoritmo que calcule e escreva a soma dos 50 primeiros termos das seguintes séries:. 
   -----------------------------------------------------------------------------
'''
print("Calculo dos 50 primeiros termos da série 1000/1 + 997/2...")

dividendo = 1000
divisor = 1
resultado = 0
lista = [1000, ]
contador = 0

while(contador<49):
    resultado = 0
    dividendo = dividendo-3
    divisor = divisor+1
    resultado = dividendo/divisor
    lista.append(resultado)
    contador = contador+1

soma = 0
for numero in lista:
    soma += numero
print(soma)


sair = 0

while (sair != 1):
    sair = int(input("Digite 1 para sair: "))
    
    
