# Dicionário contendo o faturamento de cada estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcula o faturamento total
faturamento_total = sum(faturamento_estados.values())

# Função para calcular o percentual de cada estado
def calcular_percentual(faturamento, total):
    return (faturamento / total) * 100

# Exibe os percentuais de cada estado
print("Percentual de representação por estado:")
for estado, faturamento in faturamento_estados.items():
    percentual = calcular_percentual(faturamento, faturamento_total)
    print(f"{estado}: {percentual:.2f}%")

# Exibe o faturamento total
print(f"\nFaturamento total: R${faturamento_total:.2f}")
