# ==================================================
# PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA
# Disciplina: Estruturas Matemáticas para Computação
# Atividade 1 - Teoria dos Conjuntos
# Nome: Bruna de Oliveira dos Santos
# Matrícula: 2622130008
# Turno: Matutino
# ==================================================

texto_a = input("Digite os elementos do conjunto A (separados por espaço): ")
texto_b = input("Digite os elementos do conjunto B (separados por espaço): ")

lista_a = texto_a.split()
lista_b = texto_b.split()

conjunto_A = []
for elemento in lista_a:
    if elemento not in conjunto_A:
        conjunto_A.append(elemento)

conjunto_B = []
for elemento in lista_b:
    if elemento not in conjunto_B:
        conjunto_B.append(elemento)

print("\n----------------------------------------------")
print("CONJUNTOS INFORMADOS")
print("----------------------------------------------")
print("A =", conjunto_A)
print("B =", conjunto_B)

# 2. UNIÃO (A ∪ B)
uniao = []
for elemento in conjunto_A:
    uniao.append(elemento)

for elemento in conjunto_B:
    if elemento not in uniao:
        uniao.append(elemento)

# 3. INTERSEÇÃO (A ∩ B)
intersecao = []
for elemento in conjunto_A:
    if elemento in conjunto_B:
        intersecao.append(elemento)

# 4. DIFERENÇAS (A - B) e (B - A)
diferenca_A_B = []
for elemento in conjunto_A:
    if elemento not in conjunto_B:
        diferenca_A_B.append(elemento)

diferenca_B_A = []
for elemento in conjunto_B:
    if elemento not in conjunto_A:
        diferenca_B_A.append(elemento)

# 5. CARDINALIDADES (Quantidade de elementos)
cardinalidade_A = len(conjunto_A)
cardinalidade_B = len(conjunto_B)
cardinalidade_uniao = len(uniao)
cardinalidade_intersecao = len(intersecao)

# 6. CONJUNTO DAS PARTES DE A (P(A))
# Começamos com o conjunto vazio []
partes_A = [[]]
for elemento in conjunto_A:
    novos_subconjuntos = []
    for subconjunto in partes_A:
        # Cria um novo subconjunto adicionando o elemento atual
        novos_subconjuntos.append(subconjunto + [elemento])
    # Junta os novos subconjuntos na lista principal
    for novo in novos_subconjuntos:
        partes_A.append(novo)

# 7. CONJUNTO DAS PARTES DE B (P(B))
partes_B = [[]]
for elemento in conjunto_B:
    novos_subconjuntos = []
    for subconjunto in partes_B:
        novos_subconjuntos.append(subconjunto + [elemento])
    for novo in novos_subconjuntos:
        partes_B.append(novo)

cardinalidade_partes_A = len(partes_A)
cardinalidade_partes_B = len(partes_B)

# 8. EXEMPLO DE PARTIÇÃO DE A
# Colocar cada elemento do conjunto A em seu próprio subconjunto
particao_A = []
for elemento in conjunto_A:
    particao_A.append([elemento])

# 9. PRODUTO CARTESIANO (A x B)
produto_cartesiano = []
for item_a in conjunto_A:
    for item_b in conjunto_B:
        produto_cartesiano.append((item_a, item_b))

# 10. VERIFICAÇÃO DE INCLUSÃO (A ⊆ B e B ⊆ A)
A_contido_em_B = True
for elemento in conjunto_A:
    if elemento not in conjunto_B:
        A_contido_em_B = False

B_contido_em_A = True
for elemento in conjunto_B:
    if elemento not in conjunto_A:
        B_contido_em_A = False

print("\n----------------------------------------------")
print("RESULTADOS DAS OPERAÇÕES")
print("----------------------------------------------")
print("1. União (A ∪ B):", uniao)
print("2. Interseção (A ∩ B):", intersecao)
print("3. Diferença (A - B):", diferenca_A_B)
print("   Diferença (B - A):", diferenca_B_A)
print("4. Cardinalidade |A|:", cardinalidade_A)
print("   Cardinalidade |B|:", cardinalidade_B)
print("   Cardinalidade |A ∪ B|:", cardinalidade_uniao)
print("   Cardinalidade |A ∩ B|:", cardinalidade_intersecao)
print("5. Conjunto das partes P(A):", partes_A)
print("   Conjunto das partes P(B):", partes_B)
print("6. Cardinalidade de P(A):", cardinalidade_partes_A)
print("   Cardinalidade de P(B):", cardinalidade_partes_B)
print("7. Exemplo de partição de A:", particao_A)
print("8. Produto Cartesiano (A x B):", produto_cartesiano)

if A_contido_em_B:
    print("9. A ⊆ B? Sim")
else:
    print("9. A ⊆ B? Não")

if B_contido_em_A:
    print("   B ⊆ A? Sim")
else:
    print("   B ⊆ A? Não")

print("==============================================")
