# ==============================================================================
# ARQUIVO: atividade1.py
# DISCIPLINA: Estruturas Matemáticas para Computação - Matemática Discreta
# NOME: Bruna de Oliveira dos Santos
# RA: 2622130008
# ==============================================================================

def mdc(a, b):
    # Aplica o Algoritmo de Euclides dividindo sucessivamente a por b até o resto ser 0.
    # Usado para testar se os módulos do TCR são coprimos dois a dois (MDC = 1).
    while b != 0:
        a, b = b, a % b  # Atualiza a com b, e b com o resto da divisão (a % b)
    return abs(a)  # Retorna o valor absoluto do MDC (sempre positivo)


def inverso_modular_estendido(a, m):
    # Calcula o inverso multiplicativo y tal que (a * y) ≡ 1 (mod m).
    # Utiliza o Algoritmo Estendido de Euclides para resolver a combinação linear.
    m0, y, x = m, 0, 1  # Guarda o módulo original m0 e inicia os coeficientes x e y
    
    if m == 1:
        return 0  # Em módulo 1, o inverso é sempre 0 por definição
    
    a_original = a  # Salva a base original apenas para exibir nos logs da tela
    print(f"   [Passo Intermediário] Buscando y tal que: {a} * y ≡ 1 (mod {m})")
    
    # Processa as divisões euclidianas regressivas para isolar o inverso
    while a > 1:
        q = a // m  # Quociente inteiro da divisão de a por m
        t = m
        m = a % m   # Resto da divisão que se torna o novo divisor
        a = t       # O divisor antigo vira o novo dividendo
        t = y
        y = x - q * y  # Atualiza o coeficiente y usando o quociente q
        x = t       # Avança na sequência de substituição
        
    # Garante que o inverso retornado seja positivo no intervalo [0, m0 - 1]
    if x < 0:
        x = x + m0  # Soma o módulo m0 caso o coeficiente obtido seja negativo
        
    print(f"   [Inverso Encontrado] Inverso de {a_original} mod {m0} é: {x}")
    return x  # Retorna o valor de y_i necessário para a fórmula do TCR


def parte_a_congruencia():
    # Solicita a, b, n e verifica a congruência modular: a ≡ b (mod n)
    print("\n" + "="*60)
    print("PARTE A - VERIFICAÇÃO DE CONGRUÊNCIA MODULAR: a ≡ b (mod n)")
    print("="*60)
    
    # Coleta os números fornecidos pelo usuário
    a = int(input("Digite o número inteiro a: "))
    b = int(input("Digite o número inteiro b: "))
    
    # Garante que o módulo n seja estritamente positivo (n > 0)
    while True:
        n = int(input("Digite o módulo n (deve ser > 0): "))
        if n > 0:
            break
        print("Erro: O módulo n precisa ser maior que zero!")
        
    print("\n--- PASSO A PASSO DA RESOLUÇÃO ---")
    diferenca = a - b     # Passo 1: Calcula a diferença (a - b)
    resto = diferenca % n # Passo 2: Calcula o resto da divisão de (a - b) por n
    
    # Exibe todos os passos dos cálculos na tela
    print(f"1. Valor de a = {a}, b = {b}, módulo n = {n}")
    print(f"2. Calculando a diferença: (a - b) = {a} - ({b}) = {diferenca}")
    print(f"3. Verificando a divisibilidade: {diferenca} mod {n} = {resto}")
    
    # Conclusão fundamentada na definição teórica de congruência
    if resto == 0:
        print(f"\nCONCLUSÃO: Como o resto da divisão de ({diferenca}) por {n} é ZERO:")
        print(f"-> {a} ≡ {b} (mod {n}) [VERDADEIRO: {a} e {b} são congruentes modulo {n}]")
    else:
        print(f"\nCONCLUSÃO: Como o resto da divisão de ({diferenca}) por {n} é {resto} (≠ 0):")
        print(f"-> {a} ≢ {b} (mod {n}) [FALSO: {a} e {b} NÃO são congruentes modulo {n}]")


def parte_b_teorema_chines_resto():
    # Resolve sistemas de 3 ou 4 congruências utilizando o Teorema Chinês do Resto (TCR)
    print("\n" + "="*60)
    print("PARTE B - TEOREMA CHINÊS DO RESTO (TCR)")
    print("="*60)
    
    # Valida a quantidade de equações escolhida pelo usuário (apenas 3 ou 4)
    while True:
        try:
            k = int(input("Deseja resolver um sistema com 3 ou 4 congruências? (Digite 3 ou 4): "))
            if k in [3, 4]:
                break
            print("Entrada inválida. Escolha apenas 3 ou 4.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            
    a_list = []  # Lista para armazenar os restos (a_i)
    n_list = []  # Lista para armazenar os módulos (n_i)
    
    # Coleta os pares a_i e n_i de cada congruência do sistema
    print(f"\nInforme os valores das {k} equações na forma x ≡ a_i (mod n_i):")
    for i in range(k):
        print(f"\n--- Equação {i+1} ---")
        ai = int(input(f" Digite o resto a_{i+1}: "))
        ni = int(input(f" Digite o módulo n_{i+1} (deve ser positivo): "))
        a_list.append(ai)
        n_list.append(ni)
        
    print("\n--- VERIFICAÇÃO DAS CONDIÇÕES MATEMÁTICAS ---")
    
    # 1. Checa se todos os módulos informados são positivos (n_i > 0)
    for i in range(k):
        if n_list[i] <= 0:
            print(f"ERRO: O módulo n_{i+1} = {n_list[i]} não é positivo.")
            print("O sistema está fora das condições previstas para o Teorema Chinês do Resto.")
            return
            
    # 2. Checa se todos os módulos são coprimos dois a dois (MDC(n_i, n_j) == 1)
    coprimos = True
    for i in range(k):
        for j in range(i + 1, k):
            g = mdc(n_list[i], n_list[j])
            print(f"MDC(n_{i+1}, n_{j+1}) = MDC({n_list[i]}, {n_list[j]}) = {g}")
            if g != 1:
                coprimos = False
                
    if not coprimos:
        print("\nERRO: Os módulos informados NÃO são coprimos dois a dois.")
        print("O sistema está fora das condições previstas para o Teorema Chinês do Resto.")
        return
        
    print("-> SUCESSO: Todos os módulos são positivos e coprimos dois a dois!")
    
    # PASSO 3: Calcula o produto total de todos os módulos N = n1 * n2 * ... * nk
    N = 1
    for ni in n_list:
        N *= ni
    print(f"\n--- PASSO 3: MÓDULO TOTAL (N) ---")
    print(f"N = {' * '.join(map(str, n_list))} = {N}")
    
    N_list = []  # Lista dos N_i (N / n_i)
    y_list = []  # Lista dos inversos multiplicativos y_i
    
    # PASSO 4 e 5: Calcula N_i e seu respectivo inverso modular y_i
    print("\n--- PASSOS 4 & 5: CÁLCULO DOS N_i E DOS INVERSOS MODULARES (y_i) ---")
    for i in range(k):
        Ni = N // n_list[i]  # N_i = N dividido pelo módulo n_i da própria equação
        N_list.append(Ni)
        print(f"\nPara a equação {i+1}:")
        print(f" N_{i+1} = N / n_{i+1} = {N} / {n_list[i]} = {Ni}")
        
        # Calcula o inverso de N_i módulo n_i (N_i * y_i ≡ 1 mod n_i)
        yi = inverso_modular_estendido(Ni, n_list[i])
        y_list.append(yi)
        
    # PASSO 6: Calcula a solução particular x0 reduzida módulo N
    print("\n--- PASSO 6: MONTAGEM DA SOLUÇÃO PARTICULAR (x0) ---")
    x0_bruto = 0
    soma_termos = []
    
    for i in range(k):
        termo = a_list[i] * N_list[i] * y_list[i]
        x0_bruto += termo
        soma_termos.append(f"({a_list[i]} * {N_list[i]} * {y_list[i]})")
        print(f"Parcela {i+1}: a_{i+1} * N_{i+1} * y_{i+1} = {a_list[i]} * {N_list[i]} * {y_list[i]} = {termo}")
        
    print(f"\nSomatório das parcelas (x0 bruto) = {' + '.join(soma_termos)} = {x0_bruto}")
    x0 = x0_bruto % N  # Reduz a menor solução positiva módulo N
    print(f"Solução mínima reduzida: x0 = {x0_bruto} mod {N} = {x0}")
    
    # PASSO 7: Apresenta a Solução Geral e realiza a validação do resultado
    print("\n--- PASSO 7: SOLUÇÃO GERAL E CONFIRMAÇÃO ---")
    print(f"Solução Geral: x = {x0} + t * {N}, para todo t ∈ ℤ")
    
    print(f"\nTestando se a solução x0 = {x0} satisfaz cada congruência inicial:")
    todas_corretas = True
    for i in range(k):
        resto_obtido = x0 % n_list[i]
        status = "CORRETO" if resto_obtido == a_list[i] else "ERRO"
        print(f" Equação {i+1}: {x0} mod {n_list[i]} = {resto_obtido} (Resto esperado: {a_list[i]}) -> [{status}]")
        if resto_obtido != a_list[i]:
            todas_corretas = False
            
    if todas_corretas:
        print(f"\n>>> CONCLUSÃO: O valor x0 = {x0} satisfaz com sucesso todo o sistema! <<<")
    else:
        print("\n>>> CONCLUSÃO: Houve uma falha na validação do sistema. <<<")


def main():
    # Menu interativo do programa
    while True:
        print("\n" + "#"*60)
        print("    PORTFÓLIO PARTE 2 - ATIVIDADE 1: CONGRUÊNCIA E TCR")
        print("#"*60)
        print("1. Parte A - Verificação de Congruência Modular (a ≡ b mod n)")
        print("2. Parte B - Teorema Chinês do Resto (TCR)")
        print("3. Sair")
        
        opcao = input("Escolha uma opção (1, 2 ou 3): ")
        if opcao == "1":
            parte_a_congruencia()
        elif opcao == "2":
            parte_b_teorema_chines_resto()
        elif opcao == "3":
            print("Encerrando o programa. Bons estudos!")
            break
        else:
            print("Opção inválida. Digite 1, 2 ou 3.")

if __name__ == "__main__":
    main()
