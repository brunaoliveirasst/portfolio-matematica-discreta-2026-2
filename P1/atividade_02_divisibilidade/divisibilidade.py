# ==================================================
# PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA
# Disciplina: Estruturas Matemáticas para Computação
# Atividade 2 - Divisibilidade, MDC e MMC
# Nome: Bruna de Oliveira dos Santos
# Matricula: 2622130008
# Turno: Maturino
# ==================================================

# 1. ENTRADA DE DADOS
# O comando int() garante que o valor inserido seja tratado como número inteiro
numero1 = int(input("Digite o primeiro número inteiro positivo: "))
numero2 = int(input("Digite o segundo número inteiro positivo: "))

print("\n----------------------------------------------")
print("NÚMEROS INFORMADOS")
print("----------------------------------------------")
print("Primeiro número:", numero1)
print("Segundo número:", numero2)

# 2. DIVISÃO INTEIRA (DIV) E RESTO DA DIVISÃO (MOD)
# Operador // calcula a divisão inteira (DIV)
# Operador % calcula o resto da divisão (MOD)
divisao_inteira = numero1 // numero2
resto = numero1 % numero2

print("\n----------------------------------------------")
print("1 E 2. DIVISÃO INTEIRA (DIV) E RESTO (MOD)")
print("----------------------------------------------")
print("DIV (", numero1, "//", numero2, "):", divisao_inteira)
print("MOD (", numero1, "%", numero2, "):", resto)

# 3 E 4. ALGORITMO DE EUCLIDES (PASSO A PASSO) E MDC
print("\n----------------------------------------------")
print("3 E 4. PASSO A PASSO DO ALGORITMO DE EUCLIDES (MDC)")
print("----------------------------------------------")

# Criamos variáveis temporárias para não alterar os números originais
a = numero1
b = numero2

# Para o algoritmo de Euclides, colocamos o maior número em 'a'
if a < b:
    temp = a
    a = b
    b = temp

# Enquanto o resto não for zero, continuamos a divisão
while b != 0:
    quociente = a // b
    resto_euclides = a % b
    
    # Exibe a equação: a = b * quociente + resto
    print(a, "=", b, "*", quociente, "+", resto_euclides)
    
    # Atualiza 'a' e 'b' para o próximo passo
    a = b
    b = resto_euclides

# Quando 'b' se torna 0, o último valor de 'a' é o MDC
mdc = a

print("\nMDC (Maior Divisor Comum) =", mdc)

# 5. CÁLCULO DO MMC (MÍNIMO MÚLTIPLO COMUM)

print("\n----------------------------------------------")
print("5. CÁLCULO DO MMC")
print("----------------------------------------------")

# Relação matemática entre MDC e MMC: MMC(a, b) = (a * b) // MDC(a, b)
mmc = (numero1 * numero2) // mdc

print("MMC (Mínimo Múltiplo Comum) =", mmc)
print("==============================================")
