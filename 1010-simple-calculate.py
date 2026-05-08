# ==========================================
# OPÇÃO 1: Solução Linear 
# ==========================================

cod1, qtd1, preco1 = input().split()
cod2, qtd2, preco2 = input().split()

total_produto1 = int(qtd1) * float(preco1)
total_produto2 = int(qtd2) * float(preco2)
valor_a_pagar = total_produto1 + total_produto2

print(f'VALOR A PAGAR: R$ {valor_a_pagar:.2f}')


# ==========================================
# OPÇÃO 2: Solução com Laço de repetição
# ==========================================
'''
valor_a_pagar = 0

for _ in range(2):
    cod, qtd, preco = input().split()
    valor_a_pagar += int(qtd) * float(preco)

print(f'VALOR A PAGAR: R$ {valor_a_pagar:.2f}')
'''