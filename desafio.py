constante_bonus = 1000

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite o valor do seu salario: "))


# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o seu bonus "))


# 4) Calcule o valor do bônus final
valor_do_bonus = constante_bonus + salario_usuario * bonus_usuario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus
print(f"O usario {nome_usuario} possui bonus de {valor_do_bonus}")
