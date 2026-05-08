nome_funcionario = input()
salario_funcionario = float(input())
valor_produtos_vendidos = float(input())

salario_com_bonus = salario_funcionario + (valor_produtos_vendidos*0.15)

print(f'TOTAL = R$ {salario_com_bonus:.2f}')