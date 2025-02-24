import pandas as pd
import matplotlib.pyplot as plt

# Carregar a base de dados
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')

# Exibir as primeiras linhas da base de dados
print(dados.head())

# Agrupar por tipo de imóvel e calcular a média de valores
df_valor_por_imovel = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

# Criar um gráfico de barras para visualizar os valores médios por tipo de imóvel
df_valor_por_imovel.plot(kind='barh', figsize=(14, 7), color='blue')
plt.title('Valor Médio por Tipo de Imóvel')
plt.xlabel('Valor Médio (R$)')
plt.ylabel('Tipo de Imóvel')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Lista de imóveis comerciais a serem removidos
list_imoveis_comerciais = [
    'Conjunto Comercial/Sala', 'Prédio Inteiro', 'Loja/Salão',
    'Galpão/Depósito/Armazém', 'Casa Comercial', 'Terreno Padrão',
    'Loja Shopping/ Ct Comercial', 'Box/Garagem', 'Chácara',
    'Loteamento/Condomínio', 'Sítio', 'Pousada/Chalé',
    'Hotel', 'Indústria'
]

# Filtrar apenas imóveis residenciais
df = dados[~dados['Tipo'].isin(list_imoveis_comerciais)]

# Criar um DataFrame com percentual de cada tipo de imóvel
percentual_por_tipo = df['Tipo'].value_counts(normalize=True).to_frame().sort_values('Tipo')

# Criar gráfico de distribuição percentual por tipo de imóvel
percentual_por_tipo.plot(kind='bar', figsize=(14, 5), color='green')
plt.title('Distribuição dos Tipos de Imóvel')
plt.xlabel('Tipo')
plt.ylabel('Percentual')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Filtrando apenas apartamentos
df_apartamento = df.query('Tipo == "Apartamento"')

# Média de quartos por apartamento
m_quarto_apartamento = df.groupby('Tipo')[['Quartos']].mean()
print(m_quarto_apartamento)

# Quantidade de bairros na base
total_bairros = len(df['Bairro'].unique())
print(f'Total de bairros na base: {total_bairros}')

# Top 10 bairros mais caros
bairros_precos = df.groupby('Bairro')[['Valor']].mean().sort_values('Valor', ascending=False).head(10)
print(bairros_precos)

# Criando gráfico de bairros mais caros
bairros_precos.sort_values(by='Valor', ascending=True).plot(kind='barh', figsize=(15,6), color='blue')
plt.title('Top 10 Bairros com Maior Valor Médio de Aluguel')
plt.xlabel('Valor Médio (R$)')
plt.ylabel('Bairro')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Identificar e tratar valores nulos
df_apartamento.fillna(0, inplace=True)

# Removendo registros com valores zerados
df_apartamento = df_apartamento[(df_apartamento['Valor'] > 0) & (df_apartamento['Condominio'] > 0)]

# Remover a coluna 'Tipo' pois já filtramos apenas apartamentos
df_apartamento.drop(columns=['Tipo'], inplace=True)

# Criar filtros específicos
filtro1 = df_apartamento.query('Quartos == 1 & Valor < 1200.0')
filtro2 = df_apartamento.query('Quartos >= 2 & Valor <= 3000 & Area > 70')

# Salvar arquivos tratados
df_apartamento.to_csv('dados_apartamentos.csv', index=False, sep=';')
filtro1.to_csv('Apto_1_quarto_1200.csv', sep=';', index=False)
filtro2.to_csv('Apto_2_quartos_3000_70m2.csv', sep=';', index=False)

print('Processamento concluído! Arquivos salvos.')
