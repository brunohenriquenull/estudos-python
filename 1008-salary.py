numero_funcionario = int(input())
qtde_horas_trabalhadas = int(input())
valor_hora = float(input())

salario = qtde_horas_trabalhadas * valor_hora

print(f'NUMBER = {numero_funcionario}')
print(f'SALARY = U$ {salario:.2f}')