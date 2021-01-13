import streamlit as st
import pandas as pd
from modulos.graficos import grafico_comparativo
import numpy as np


@st.cache
def carrega_dados(caminho):
    dados = pd.read_csv(caminho)
    return dados


def main():
    obitos_2019 = carrega_dados('dados/obitos-2019.csv')
    obitos_2020 = carrega_dados('dados/obitos-2020.csv')
    tipo_doenca = np.append(obitos_2019.tipo_doenca.unique(), 'Todas as doenças')
    tipo_estado = np.append(obitos_2019.uf.unique(), 'Brasil')

    st.title('Minha aplicação')
    st.markdown('Este trabalho tem o intuito de analisar obitos comparando **2019 e 2020**')

    # Side bar
    st.sidebar.title('Opções')
    opcao_doenca = st.sidebar.selectbox('Selecione o tipo de doença', tipo_doenca, 7)
    opcao_estado = st.sidebar.selectbox('Selecione o tipo de doença', tipo_estado, 27)

    # Main
    figura = grafico_comparativo(obitos_2019, obitos_2020, opcao_doenca, opcao_estado)
    st.pyplot(figura)

    if st.checkbox('Exibir DataFrame 2019'):
        st.dataframe(obitos_2019)
    if st.checkbox('Exibir DataFrame 2020'):
        st.dataframe(obitos_2020)


if __name__ == '__main__':
    main()
