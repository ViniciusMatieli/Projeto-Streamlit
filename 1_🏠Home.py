import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

#lendo os dados para df
st.set_page_config(page_title='FIFA 23',page_icon='⚽')

file_url  = 'https://drive.google.com/file/d/16v09jfNGHXkKs7o4MItkQ5e_jhzCjvuU/view?usp=sharing'

@st.cache
def load_data():
    return pd.read_csv(file_url,delimiter=',', index_col=0)

if 'data' not in st.session_state:
    df = load_data()
    df = df.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df

st.title('Analise do FIFA 23 ⚽🎮')

st.write('Base de dados do Kaggle')
#assinatura do desenvolvidor 
st.sidebar.markdown('Desenvolvido por [Vinicius Mattielli](https://facebook.com/viniciusmatieli)')

btn = st.button('Acessar a base de dados')
if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database')

st.markdown(
    """

O FIFA 23, desenvolvido pela EA Sports, marca um marco significativo na série de jogos de futebol, sendo o último título da franquia antes da mudança para o novo nome, EA Sports FC. Lançado em setembro de 2022, o jogo oferece uma série de melhorias e inovações, tanto no campo gráfico quanto na jogabilidade. A introdução do HyperMotion2, uma evolução do sistema HyperMotion presente em FIFA 22, proporciona uma experiência de jogo mais realista, com movimentos de jogadores e dinâmicas de jogo mais autênticos. Além disso, o FIFA 23 destaca-se por seu aprimorado modo Career, que inclui novas opções de personalização e maior profundidade tática.

O modo Ultimate Team, um dos mais populares da série, também recebeu atualizações significativas, com novos eventos e um sistema de química reformulado que visa oferecer mais flexibilidade na construção de equipes. A inclusão das ligas femininas pela primeira vez, com a possibilidade de jogar com times de futebol feminino, representa uma grande inovação e um passo importante para a inclusão e diversidade no jogo.

Além dessas melhorias, o FIFA 23 mantém sua tradicional base de dados atualizada, oferecendo uma ampla gama de equipes e jogadores licenciados. No entanto, como em qualquer título anual, o jogo também enfrenta críticas relacionadas à sua abordagem incremental em comparação com edições anteriores. No geral, o FIFA 23 oferece uma experiência de futebol enriquecida e detalhada, mantendo o padrão de qualidade da série e preparando o terreno para a transição para o novo título da EA Sports.

"""
)
