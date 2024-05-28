import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Análise exploratória",
     page_icon="📈",
     layout="wide",
     initial_sidebar_state="expanded",
)


renda = pd.read_csv('./input/previsao_de_renda.csv')
# transformando variavel data_ref para datetime
renda['data_ref'] = pd.to_datetime(renda['data_ref'])
# removendo variaveis que não serão analisadas
renda.drop(columns=['Unnamed: 0', 'id_cliente'], inplace=True)

st.write('# Análise exploratória da previsão de renda')

st.write('## Distribuição das variáveis')
c1, c2 = st.columns(2)

sns.set_theme('talk')
figsize = (10,8)
with c1:
    ##  Distribuição da variavel ["sexo"]
    fig, ax = plt.subplots(figsize=figsize)
    sns.histplot(renda,
             x="sexo",
             ax=ax
            ).set_xticklabels(['Feminino', 'Masculino']
            )
    plt.xlabel('Sexo')
    plt.ylabel('')
    plt.title('Distribuição da variavel ["sexo"]')
    st.pyplot(fig)
    ##


    ## Distribuição da variavel ["tipo_residencia"]
    fig, ax = plt.subplots(figsize=figsize)
    sns.countplot(renda,
              x="tipo_residencia")
    plt.xlabel('Tipo de residência')
    plt.ylabel('')
    plt.title('Distribuição da variavel ["tipo_residencia"]')
    plt.xticks(rotation=13)
    st.pyplot(fig)
    ##
    

    ##  Distribuição da variavel ["estado_civil"]
    fig, ax = plt.subplots(figsize=figsize)
    sns.countplot(renda,
              x="estado_civil")
    plt.xlabel('Estado civil')
    plt.ylabel('')
    plt.title('Distribuição da variavel ["estado_civil"]')
    st.pyplot(fig)
    ##


    ##  Distribuição da variavel ["educacao"]
    fig, ax = plt.subplots(figsize=(10,7.5))
    sns.countplot(renda,
              x="educacao",
              order=['Primário',
                     'Secundário',
                     'Superior incompleto',
                     'Superior completo',
                     'Pós graduação'])
    plt.xticks(rotation=12)
    plt.xlabel('Educação')
    plt.ylabel('')
    plt.title('Distribuição da variavel ["educacao"]')
    st.pyplot(fig)
    ##
    

    ##  Distribuição da variavel ["idade"]
    fig, ax = plt.subplots(figsize=figsize)
    sns.kdeplot(renda,
            x="idade",
            fill=True
           )
    plt.xlabel('Idade')
    plt.ylabel('')
    plt.title('Distribuição da variavel ["idade"]')
    st.pyplot(fig)
    ##
    
with c2:
    ##  Distribuição da variavel ["qtd_filhos"]
    fig, ax = plt.subplots(figsize=figsize)
    sns.histplot(renda,
             x='qtd_filhos',
             binrange=(min(renda.qtd_filhos)-0.5,
                       max(renda.qtd_filhos)+0.5),
             binwidth=1)
    plt.xticks(ticks=[x for x in range(0,15)])
    plt.xlabel('Quantidade de filhos')
    plt.ylabel('')
    plt.title('Distribuição da variavel ["qtd_filhos"]')
    st.pyplot(fig)
    ##
    

    ##  Distribuição da variavel ["tipo_renda"]
    fig, ax = plt.subplots(figsize=figsize)
    sns.countplot(renda,
              x="tipo_renda")
    plt.xlabel('Tipo de renda')
    plt.ylabel('')
    plt.title('Distribuição da variavel ["tipo_renda"]')
    plt.xticks(rotation=10)
    st.pyplot(fig)
    ##

    ##  Distribuição da variavel ["posse_de_veiculo"]
    fig, ax = plt.subplots(figsize=figsize)
    sns.histplot(renda,
                x="posse_de_veiculo",
                bins=[-0.5, 0.5, 1.5],
                ax=ax,
                ).set_xticklabels(['Não', 'Sim'])
    plt.xticks(ticks=(0,1))
    plt.xlabel('Posse de Veículo')
    plt.ylabel('')
    plt.title('Distribuição da variavel ["posse_de_veiculo"]')
    st.pyplot(fig)
    ##


    ##  Distribuição da variavel ["posse_de_imovel"]
    fig, ax = plt.subplots(figsize=figsize)
    sns.histplot(renda,
                x="posse_de_imovel",
                bins=[-0.5, 0.5, 1.5],
                ax=ax,
            ).set_xticklabels(['Não', 'Sim']
            )
    plt.xticks(ticks=(0,1))
    plt.xlabel('Posse de Imóvel')
    plt.ylabel('')
    plt.title('Distribuição da variavel ["posse_de_imovel"]')
    st.pyplot(fig)
    ##

    ##  Distribuição da variavel ["tempo_emprego"]
    fig, ax = plt.subplots(figsize=figsize)
    sns.histplot(renda,
             x="tempo_emprego",
             bins=50
            )
    plt.xlabel('Tempo de emprego (em anos)')
    plt.ylabel('')
    plt.title('Distribuição da variavel ["tempo_emprego"]')
    st.pyplot(fig)
    ##

_, c, _ = st.columns([2,6,2])
with c:
    ##  Distribuição da variavel ["qt_pessoas_residencia"]
    fig, ax = plt.subplots(figsize=figsize)
    sns.histplot(renda,
             x="qt_pessoas_residencia",
             bins=7)
    plt.xlabel("Quantidade de pessoas na residência")
    plt.ylabel('')
    plt.title('Distribuição da variavel ["qt_pessoas_residencia"]')
    st.pyplot(fig)
    ##

st.write('## Gráficos ao longo do tempo')

c1, c2 = st.columns(2)

with c1:


    ##  Média da renda por tipo de renda
    fig, ax = plt.subplots(figsize=figsize)
    sns.lineplot(data=renda,
             x='data_ref',
             y='renda',
             hue='tipo_renda'
            )
    plt.title('Média da renda por tipo de renda')
    plt.xticks(rotation=10)
    plt.xlabel('Tipo de renda')
    st.pyplot(fig)
    ##


    ##  Média da renda por sexo
    fig, ax = plt.subplots(figsize=figsize)
    sns.lineplot(data=renda,
             x='data_ref',
             y='renda',
             hue='sexo',
            )
    plt.title('Média da renda por sexo')
    plt.xlabel('Sexo')
    st.pyplot(fig)
    ##


with c2:


    ##  Média da renda por estado civil
    fig, ax = plt.subplots(figsize=figsize)
    sns.lineplot(data=renda,
             x='data_ref',
             y='renda',
             hue='estado_civil',
            )
    plt.xticks(rotation=12)
    plt.title('Média da renda por estado civil')
    plt.xlabel('Estado Civil')
    st.pyplot(fig)
    ##


    ##  Média da renda por educação
    fig, ax = plt.subplots(figsize=figsize)
    sns.lineplot(data=renda,
             x='data_ref',
             y='renda',
             hue='educacao',
            )
    plt.title('Média da renda por educação')
    plt.xlabel('Educação')
    st.pyplot(fig)
    ##

_, c, _ = st.columns([1,8,1])
with c:
    ##  Média da renda por tipo de residência
    fig, ax = plt.subplots(figsize=(15,8))
    sns.lineplot(data=renda,
             x='data_ref',
             y='renda',
             hue='tipo_residencia'
            )
    plt.xticks(rotation=12)
    plt.title('Média da renda por tipo de residência')
    plt.xlabel('Tipo residência')
    st.pyplot(fig)
    ##

st.write('## Matriz de correlação para variáveis numéricas')
_, c, _ = st.columns([.5,9,.5])
with c:
    fig, ax = plt.subplots(figsize=(16,12))
    correlation_matrix = renda.drop(['sexo',
                                    'tipo_renda',
                                    'educacao',
                                    'estado_civil',
                                    'tipo_residencia',
                                    'data_ref'],
                                    axis=1).corr()
    sns.heatmap(correlation_matrix,
                annot=True,
                fmt=".2f",
                cmap='coolwarm',
                center=0,
                ax=ax,
                )
    plt.xticks(rotation=25)
    plt.title('Matriz de Correlação')
    st.pyplot(fig)
    sns.despine()






