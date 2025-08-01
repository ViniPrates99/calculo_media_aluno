# Programa para calcular a média de notas de um aluno

# Entrada das notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Exibir o resultado
print(f"Sua média é: {media:.2f}")

# Verificação de aprovação
if media >= 7:
    print("Parabéns! Você está APROVADO.")
elif 5 <= media < 7:
    print("Você está de RECUPERAÇÃO.")
else:
    print("Infelizmente você está REPROVADO.")
