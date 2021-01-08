import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def carrega_dados(caminho):
    dados = pd.read_csv(caminho)
    return dados


def grafico_comparativo(dados_2019, dados_2020, causa='Todas as doenças', estado='Brasil'):
    if estado != 'Brasil':
        seletor_estado_2019 = dados_2019.uf == estado
        seletor_estado_2020 = dados_2020.uf == estado
        total_2019 = dados_2019[seletor_estado_2019].groupby('tipo_doenca').sum()
        total_2020 = dados_2020[seletor_estado_2020].groupby('tipo_doenca').sum()
    else:
        total_2019 = dados_2019.groupby('tipo_doenca').sum()
        total_2020 = dados_2020.groupby('tipo_doenca').sum()

    if causa == 'Todas as doenças':
        dados = pd.concat([total_2019, total_2020], keys=['2019', '2020']).reset_index()

        fig, ax = plt.subplots(figsize=(12,8))
        ax = sns.barplot(x='tipo_doenca', y='total', hue='level_0', data=dados)
        ax.set_title(f'Óbitos por {causa}: {estado}')
        ax.legend(title='Ano')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=13)
        return fig

    else:
        # Dados
        lista = [int(total_2019.loc[causa]), int(total_2020.loc[causa])]
        dados = pd.DataFrame({'Total': lista,
                              'Ano': [2019, 2020]})

        # Grafico
        fig, ax = plt.subplots()
        ax = sns.barplot(x='Ano', y='Total', data=dados)
        ax.set_title(f'Óbitos por {causa}: {estado}')
        return fig


def main():
    obitos_2019 = carrega_dados('dados/obitos-2019.csv')
    obitos_2020 = carrega_dados('dados/obitos-2020.csv')
    tipo_doenca = np.append(obitos_2019.tipo_doenca.unique(), 'Todas as doenças')
    tipo_estado = np.append(obitos_2019.uf.unique(), 'Brasil')

    st.title('Minha aplicação')
    st.markdown('Este trabalho tem o intuito de analisar obitos comparando **2019 e 2020**')

    opcao_doenca = st.sidebar.selectbox('Selecione o tipo de doença', tipo_doenca)
    opcao_estado = st.sidebar.selectbox('Selecione o tipo de doença', tipo_estado)
    figura = grafico_comparativo(obitos_2019, obitos_2020, opcao_doenca, opcao_estado)
    st.pyplot(figura)

if __name__ == '__main__':
    main()
