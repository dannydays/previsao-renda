import joblib
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
     page_title="Simulação",
     page_icon="💰",
     layout="wide",
     initial_sidebar_state="expanded",
)

renda = pd.read_csv('./input/previsao_de_renda.csv')

# removendo variaveis que não serão analisadas
renda.drop(columns=['Unnamed: 0', 'id_cliente'], inplace=True)

# removendo valores faltantes
renda.dropna(inplace=True)

# removendo valores duplicados
renda.drop_duplicates(inplace=True)

X = (pd.get_dummies(data=renda)
    .astype('float')
).tail(1)

m_tree = joblib.load('./modelo_treinado.pkl')

with st.form("my_form"):
    st.write("Previsão de renda")
    idade = st.number_input("Idade", step=1, min_value=0)
    tempo_emprego = st.number_input("Tempo de emprego em anos", step=1, min_value=0)
    posse_de_imovel = st.checkbox("Posse de Imóvel")
    posse_de_veiculo = st.checkbox("Posse de Veiculo")
    sexo = st.selectbox("Sexo", ["Masculino","Feminino"])
    qtd_filhos = st.number_input("Quantidade de filhos", step=1, min_value=0)
    tipo_renda = st.selectbox("Tipo de renda", ["Empresário", "Assalariado", "Servidor público", "Bolsista", "Pensionista"])
    educacao = st.selectbox("Educação", ["Primário", "Secundário", "Superior incompleto", "Superior completo", "Pós graduação"])
    estado_civil = st.selectbox("Estado Civil", ["Solteiro", "Casado", "Viúvo", "União", "Separado"])
    tipo_residencia = st.selectbox("Tipo de residência", ["Casa", "Governamental", "Com os pais", "Aluguel", "Estúdio", "Comunitário"])
    qt_pessoas_residencia = st.number_input("Quantidade de pessoas na residência", step=1, min_value=0)
    # Every form must have a submit button.
    submitted = st.form_submit_button("Enviar")
    if submitted:
        entrada = (pd.get_dummies(pd.DataFrame([{
                                'idade':idade,
                                'tempo_emprego':tempo_emprego,
                                'posse_de_imovel':posse_de_imovel,
                                'posse_de_veiculo':posse_de_veiculo,
                                'sexo':sexo[0],
                                'qtd_filhos':qtd_filhos,
                                'tipo_renda':tipo_renda,
                                'educacao':educacao,
                                'estado_civil':estado_civil,
                                'tipo_residencia':tipo_residencia,
                                'qt_pessoas_residencia':qt_pessoas_residencia,}]),
                                columns=['sexo',
                                         'tipo_renda',
                                         'tipo_residencia',
                                         'estado_civil',
                                         'educacao']
                                ).astype('float'))
                    
        st.write(f" Renda aproximada: R${str(np.round(m_tree.predict(pd.concat([X, entrada]).fillna(0).tail(1)[['tempo_emprego',
                                                                                                             'sexo_F',
                                                                                                             'tipo_renda_Empresário',
                                                                                                             'idade',
                                                                                                             'sexo_M',
                                                                                                             'educacao_Superior completo',
                                                                                                             'estado_civil_Casado']])[0], 2)).replace('.', ',')}")