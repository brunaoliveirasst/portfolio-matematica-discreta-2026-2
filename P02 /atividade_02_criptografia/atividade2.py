# ==============================================================================
# ARQUIVO: atividade2.py
# DISCIPLINA: Estruturas Matemáticas para Computação - Matemática Discreta
# ATIVIDADE 2: Criptografia RSA e Teoremas de Euler e Fermat
# NOME: Bruna de Oliveira dos Santos
# RA: 2622130008
# ==============================================================================

def mdc(a, b):
    # Algoritmo de Euclides para calcular o Máximo Divisor Comum (MDC)
    # Troca iterativamente (a, b) por (b, a % b) até b se tornar 0
    while b != 0:
        a, b = b, a % b  # Atualiza a com b, e b com o resto da divisão de a por b
    return abs(a)  # Retorna o valor positivo do MDC


def eh_primo(n):
    # Teste de primalidade por divisão trial (procedimento próprio sem bibliotecas)
    if n <= 1:
        return False  # Números menores ou iguais a 1 não são primos
    if n <= 3:
        return True   # 2 e 3 são números primos fundamentais
    if n % 2 == 0 or n % 3 == 0:
        return False  # Elimina rapidamente pares e múltiplos de 3
    
    i = 5
    # Testa divisores ímpares na forma (6k ± 1) até a raiz quadrada de n (i * i <= n)
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False  # Encontrou divisor: n não é primo
        i += 6  # Salta múltiplos de 2 e 3 para otimizar os testes
    return True  # Não encontrou divisores: n é primo


def inverso_modular_estendido(a, m):
    # Algoritmo Estendido de Euclides para encontrar o inverso modular d
    # Resolve a equação e * d ≡ 1 (mod φ(n)) encontrando o coeficiente de Bézout
    m0, y, x = m, 0, 1  # Armazena o módulo original m0 e inicia os coeficientes
    
    if m == 1:
        return 0  # Em módulo 1, o inverso é trivialmente 0
    
    while a > 1:
        q = a // m  # Quociente inteiro da divisão de a por m
        t = m
        m = a % m   # O resto da divisão vira o novo divisor
        a = t       # O divisor anterior vira o novo dividendo
        t = y
        y = x - q * y  # Atualiza o coeficiente y usando o quociente q
        x = t       # Avança a substituição regressiva de Bézout
        
    if x < 0:
        x = x + m0  # Se o inverso for negativo, ajusta para o equivalente positivo no módulo
    return x  # Retorna o inverso multiplicativo d


def exponenciacao_modular_passo_a_passo(base, expoente, modulo):
    # Algoritmo de exponenciação modular eficiente (Square-and-Multiply)
    # Calcula (base^expoente) % modulo aplicando o resto a cada multiplicação
    print(f"\n   [Exponenciação Modular] Calculando {base}^{expoente} mod {modulo}...")
    resultado = 1          # Inicia com o elemento neutro da multiplicação
    base = base % modulo   # Reduz a base inicial pelo módulo para simplificar
    
    exp_temp = expoente  # Variável auxiliar do expoente
    passo = 1            # Contador para exibições dos passos
    
    while exp_temp > 0:
        if exp_temp % 2 == 1:
            # Se o bit atual do expoente for 1 (ímpar), multiplica o resultado pela base
            resultado_ant = resultado
            resultado = (resultado * base) % modulo
            print(f"   Passo {passo}: Expoente ímpar ({exp_temp}) -> resultado = ({resultado_ant} * {base}) mod {modulo} = {resultado}")
        else:
            # Se o bit for 0 (par), apenas mantém o resultado atual
            print(f"   Passo {passo}: Expoente par ({exp_temp}) -> resultado mantido = {resultado}")
            
        exp_temp = exp_temp // 2  # Divide o expoente por 2 (deslocamento de bit à direita)
        if exp_temp > 0:
            # Eleva a base ao quadrado a cada passo e aplica a redução modular
            base_ant = base
            base = (base * base) % modulo
            print(f"           Elevando base ao quadrado -> nova base = ({base_ant}^2) mod {modulo} = {base}")
            
        passo += 1
        
    print(f"   [Resultado Final] {base}^{expoente} mod {modulo} = {resultado}")
    return resultado  # Retorna o valor final calculado


def parte_a_e_b_rsa():
    # PARTE A & B: Coleta dos primos p e q, cálculo de n, φ(n), validação de e e geração de d
    print("\n" + "="*60)
    print("ATIVIDADE 2 - PARTE A & B: GERAÇÃO DE PARÂMETROS E CHAVES RSA")
    print("="*60)
    
    # Coleta e validação dos números primos p e q
    while True:
        try:
            p = int(input("Digite o primeiro número primo (p > 1): "))
            q = int(input("Digite o segundo número primo (q > 1 e q != p): "))
            
            if p <= 1 or q <= 1:
                print("Erro: Os números p e q devem ser maiores que 1!")
                continue
            if p == q:
                print("Erro: Os números p e q devem ser distintos!")
                continue
                
            print("\n--- TESTANDO PRIMALIDADE (Procedimento Próprio) ---")
            primo_p = eh_primo(p)
            primo_q = eh_primo(q)
            
            print(f" O número p = {p} é primo? {primo_p}")
            print(f" O número q = {q} é primo? {primo_q}")
            
            if primo_p and primo_q:
                print("-> Sucesso: p e q são primos válidos!")
                break
            else:
                print("Erro: p e q devem ser números primos. Tente novamente.\n")
        except ValueError:
            print("Entrada inválida. Digite números inteiros.")
            
    # Cálculo do Módulo RSA (n) e da Função Totiente de Euler φ(n)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    print(f"\n--- PARÂMETROS CALCULADOS ---")
    print(f"1. Módulo RSA (n = p * q): {p} * {q} = {n}")
    print(f"2. Totiente de Euler φ(n) = (p - 1)*(q - 1): ({p} - 1)*({q} - 1) = {phi}")
    
    # Validação do Expoente Público (e)
    while True:
        try:
            e = int(input(f"\nDigite o expoente público e (1 < e < {phi} e MDC(e, φ(n)) = 1): "))
            if not (1 < e < phi):
                print(f"Erro: O valor de e deve estar estritamente entre 1 e {phi}.")
                continue
                
            g = mdc(e, phi)
            print(f" Teste de Coprimalidade: MDC(e, φ(n)) = MDC({e}, {phi}) = {g}")
            if g == 1:
                print("-> Sucesso: Expoente público 'e' válido!")
                break
            else:
                print(f"Erro: MDC({e}, {phi}) = {g} ≠ 1. O expoente 'e' deve ser coprimo com φ(n).")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            
    # Cálculo da Chave Privada (d) via Algoritmo Estendido
    print("\n--- CONSTRUÇÃO DAS CHAVES (PARTE B) ---")
    d = inverso_modular_estendido(e, phi)
    
    # Validação do expoente privado: (e * d) mod φ(n) deve ser igual a 1
    verificacao_d = (e * d) % phi
    print(f"Verificação da chave privada: ({e} * {d}) mod {phi} = {verificacao_d}")
    if verificacao_d == 1:
        print("-> Validação da chave privada: (e * d) ≡ 1 (mod φ(n)) [CORRETO!]")
    else:
        print("-> Validação da chave privada: FALHOU!")
        
    print(f"\n>>> CHAVE PÚBLICA (e, n) : ({e}, {n}) <<<")
    print(f">>> CHAVE PRIVADA (d, n) : ({d}, {n}) <<<")
    
    return p, q, n, phi, e, d


def parte_c_cifragem_decifragem(n, e, d):
    # PARTE C: Cifragem C = M^e mod n e Decifragem M' = C^d mod n
    print("\n" + "="*60)
    print("ATIVIDADE 2 - PARTE C: CIFRAGEM E DECIFRAGEM DE MENSAGEM INTEIRA")
    print("="*60)
    
    # Coleta da mensagem inteira M
    while True:
        try:
            M = int(input(f"Digite uma mensagem numérica inteira M (0 <= M < {n}): "))
            if 0 <= M < n:
                break
            print(f"Erro: A mensagem M deve satisfazer a condição 0 <= M < {n}.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            
    # Etapa de Cifragem
    print(f"\n--- ETAPA 1: CIFRAGEM (C = M^e mod n) ---")
    print(f"Cifrando M = {M} com Chave Pública (e={e}, n={n})...")
    C = exponenciacao_modular_passo_a_passo(M, e, n)
    print(f"-> MENSAGEM CIFRADA OBTIDA (C): {C}")
    
    # Etapa de Decifragem
    print(f"\n--- ETAPA 2: DECIFRAGEM (M' = C^d mod n) ---")
    print(f"Decifrando C = {C} com Chave Privada (d={d}, n={n})...")
    M_linha = exponenciacao_modular_passo_a_passo(C, d, n)
    print(f"-> MENSAGEM DECIFRADA OBTIDA (M'): {M_linha}")
    
    print(f"\n--- RESUMO DA OPERAÇÃO ---")
    print(f"Mensagem Original (M) : {M}")
    print(f"Mensagem Cifrada  (C) : {C}")
    print(f"Mensagem Decifrada(M'): {M_linha}")
    
    if M_linha == M:
        print("\n>>> CONCLUSÃO: M' == M (SUCESSO: A mensagem original foi recuperada com perfeição!). <<<")
    else:
        print("\n>>> CONCLUSÃO: M' != M (FALHA na decifragem!). <<<")


def parte_d_teoremas_fermat_euler(n, phi, p, q):
    # PARTE D: Demonstração dos Teoremas de Euler e Fermat
    print("\n" + "="*60)
    print("ATIVIDADE 2 - PARTE D: TEOREMAS DE FERMAT E EULER NA EXPONENCIAÇÃO")
    print("="*60)
    
    # 1. Demonstração de Euler: M^φ(n) ≡ 1 (mod n)
    print("\n1. DEMONSTRAÇÃO DO TEOREMA DE EULER:")
    print(f" Para base M coprima com n (MDC(M, n) = 1): M^φ(n) ≡ 1 (mod n).")
    
    while True:
        try:
            base_euler = int(input(f"\nDigite uma base M para testar o Teorema de Euler mod {n}: "))
            g_euler = mdc(base_euler, n)
            print(f" Testando MDC({base_euler}, {n}) = {g_euler}")
            if g_euler == 1:
                print(" -> Base coprima com n! Condição de Euler satisfeita.")
                break
            else:
                print(f" -> MDC({base_euler}, {n}) = {g_euler} ≠ 1. A base DEVE ser coprima com n.")
        except ValueError:
            print("Digite um número inteiro válido.")
            
    res_euler = exponenciacao_modular_passo_a_passo(base_euler, phi, n)
    print(f" Resultado de Euler: {base_euler}^{phi} mod {n} = {res_euler}")
    if res_euler == 1:
        print(" -> TEORIA CONFIRMADA: M^φ(n) ≡ 1 (mod n) verificado na prática!")
        
    # 2. Demonstração de Fermat: a^(p-1) ≡ 1 (mod p)
    print("\n" + "-"*50)
    print("2. DEMONSTRAÇÃO DO PEQUENO TEOREMA DE FERMAT:")
    print(f" Para módulo primo p e base 'a' não divisível por p: a^(p-1) ≡ 1 (mod p).")
    
    while True:
        try:
            base_fermat = int(input(f"\nDigite uma base 'a' (não divisível pelo primo p={p}): "))
            if base_fermat % p != 0:
                print(f" -> {base_fermat} não é divisível por {p}. Condição de Fermat satisfeita.")
                break
            else:
                print(f" -> {base_fermat} é divisível por {p}. Escolha outra base!")
        except ValueError:
            print("Digite um número inteiro válido.")
            
    res_fermat = exponenciacao_modular_passo_a_passo(base_fermat, p - 1, p)
    print(f" Resultado de Fermat: {base_fermat}^{p-1} mod {p} = {res_fermat}")
    if res_fermat == 1:
        print(" -> TEORIA CONFIRMADA: a^(p-1) ≡ 1 (mod p) verificado na prática!")
        
    # 3. Nota Explicativa Teórica
    print("\n" + "-"*50)
    print("3. NOTA EXPLICATIVA SOBRE OS TEOREMAS NO RSA:")
    print("""
    IMPORTANTE:
    - O Pequeno Teorema de Fermat NÃO se aplica diretamente ao módulo n do RSA (n = p * q), 
      porque n é COMPOSTO, e Fermat exige estritamente um módulo PRIMO.
    - O Teorema de Euler exige que a base M seja COPRIMA com n (MDC(M, n) = 1).
    - Quando essas condições não são atendidas, a exponenciação modular por reduções 
      sucessivas (Square-and-Multiply) continua sendo o único procedimento universal e válido!
    """)


def main():
    # Função principal que executa a sequência inteira do RSA
    print("#"*60)
    print("    PORTFÓLIO PARTE 2 - ATIVIDADE 2: CRIPTOGRAFIA RSA")
    print("#"*60)
    
    p, q, n, phi, e, d = parte_a_e_b_rsa()
    parte_c_cifragem_decifragem(n, e, d)
    parte_d_teoremas_fermat_euler(n, phi, p, q)


if __name__ == "__main__":
    main()
