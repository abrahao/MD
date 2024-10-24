import pandas as pd

# Carregar os dados
data = pd.read_csv('evasao_escolar_ensino_medio.csv')

# Calcular os motivos de evasão
motivo_evasao = data['Motivo da Evasão'].value_counts()

# Exibir a contagem original
print("Contagem original de motivos de evasão:")
print(motivo_evasao)

# Inicializa a contagem de zero se não existir
if 0 not in motivo_evasao.index:
    motivo_evasao.loc[0] = 0  # Adiciona a chave 0 com valor 0 se não existir

# Número atual de ocorrências do motivo 0
atual_zero = motivo_evasao.loc[0]

# Calcular quantas ocorrências precisam ser adicionadas
necessario_zero = 9645 - atual_zero

if necessario_zero > 0:
    # Remove a entrada existente para zero
    motivo_evasao = motivo_evasao[motivo_evasao.index != 0]
    # Adiciona a nova contagem de zero
    motivo_evasao.loc[0] = 9645  # Define o valor total desejado

# Exibir a nova contagem
print("\nNova contagem de motivos de evasão:")
print(motivo_evasao)

# Salvar as alterações em um novo arquivo CSV
data.to_csv('evasao_escolar_atualizado.csv', index=False)

print("\nAlterações salvas no arquivo 'evasao_escolar_atualizado.csv'.")

