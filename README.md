# 📊 Análise de Dados de Imóveis

## 📌 Sobre o Projeto
Este projeto realiza uma análise exploratória de um conjunto de dados de imóveis. O objetivo é entender a distribuição dos preços, identificar padrões entre diferentes tipos de imóveis e realizar uma limpeza e filtragem eficiente dos dados.

### ✅ O que foi feito?
- Importação e exploração dos dados.
- Tratamento de valores nulos e inconsistentes.
- Aplicação de filtros para imóveis residenciais.
- Criação de gráficos para melhor visualização dos dados.
- Exportação dos dados limpos.

## 📂 Estrutura do Repositório
```
📦 analise-imoveis
 ├── 📂 data                # Dados brutos e processados
 │   ├── aluguel.csv       # Base original
 │   ├── dados_apartamentos.csv  # Dados tratados
 │   ├── Apto_1_quarto_1200.csv  # Filtros aplicados
 │   ├── Apto_2_quartos_3000_70m2.csv  
 │
 ├── 📂 notebooks           # Notebooks para análise
 │   ├── Imoveis_Portfolio_Documentado.ipynb  # Notebook final e organizado
 │
 ├── 📂 images              # Gráficos gerados na análise
 │
 ├── 📂 scripts             # Código Python para automação
 │   ├── analise_imoveis.py  # Versão do código estruturado para rodar como script
 │
 ├── README.md              # Documentação do projeto
 ├── requirements.txt       # Lista de pacotes necessários
```

## 📊 Análises Realizadas
### 🔍 Exploração dos Dados
- Estatísticas descritivas dos imóveis.
- Comparação entre valores médios de aluguel por tipo de imóvel.
- Identificação e remoção de valores nulos e inconsistentes.

### 📈 Visualizações
- Gráfico de barras com a distribuição de valores por tipo de imóvel.
- Percentual de cada tipo de imóvel disponível.
- Análise dos bairros mais caros.

## 🚀 Como Executar o Projeto
### 1️⃣ Rodar no Google Colab
Se você deseja rodar diretamente no Google Colab, basta acessar este link:
[Abrir no Google Colab](https://colab.research.google.com/github/seu-usuario/analise-imoveis/blob/main/notebooks/Imoveis_Portfolio_Documentado.ipynb)

### 2️⃣ Rodar localmente
Se quiser rodar o projeto em sua máquina, siga os passos:
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/analise-imoveis.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
4. Abra o arquivo `Imoveis_Portfolio_Documentado.ipynb` e execute as células.

## 🔧 Tecnologias Utilizadas
- **Python** (Pandas, Matplotlib)
- **Google Colab** para execução online
- **Jupyter Notebook** para execução local

## 🎯 Como este projeto pode ser útil?
🔹 Ajuda a entender a precificação de imóveis em diferentes bairros.  
🔹 Facilita a visualização dos dados para análise exploratória.  
🔹 Serve como base para futuros projetos de ciência de dados ou Machine Learning.  

## 📢 Conecte-se Comigo!
Se você gostou do projeto, me adicione no [LinkedIn](https://www.linkedin.com/in/hencheo) e confira meu portfólio no GitHub! 😃
