import pandas as pd
from matplotlib.pyplot import subplots
from seaborn import barplot


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

        fig, ax = subplots(figsize=(12, 8))
        ax = barplot(x='tipo_doenca', y='total', hue='level_0', data=dados)
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
        fig, ax = subplots()
        ax = barplot(x='Ano', y='Total', data=dados)
        ax.set_title(f'Óbitos por {causa}: {estado}')
        return fig
