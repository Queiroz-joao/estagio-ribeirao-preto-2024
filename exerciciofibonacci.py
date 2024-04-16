# Solicita um número ao usuário
num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if ((5 * num * num + 4) ** 0.5).is_integer() or ((5 * num * num - 4) ** 0.5).is_integer():
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
