import streamlit as st
import pandas as pd
st.set_page_config(page_title='Players',page_icon='🥇',layout='wide')
df = st.session_state['data']

clubes = df['Club'].unique()
club = st.sidebar.selectbox('Clube', clubes)

df_players = df[df['Club'] == club]
players = df_players['Name'].unique()
player = st.sidebar.selectbox('Jogador', players)

player_stats = df[df['Name'] == player].iloc[0]

st.image(player_stats['Photo'])
st.title(f'{player_stats['Name']}')

st.markdown(f'**Clube:** {player_stats["Club"]}')
st.markdown(f'**Numeração:** {player_stats['Kit Number']}')
st.markdown(f'**Posição:** {player_stats["Position"][-3:]}')

col1,col2,col3,col4 = st.columns(4)
col1.markdown(f'**Idade:** {player_stats["Age"]}')
col2.markdown(f'**Altura:** {player_stats["Height"]}')
col3.markdown(f'**Peso:** {player_stats["Weight"]}')

st.divider()
st.subheader(f'Overall {player_stats["Overall"]}')
st.progress(int(player_stats['Overall']))

col1,col2,col3,col4 = st.columns(4)
col1.metric('Valor de Mercado', value=f'£{player_stats["Value (€)"]:,}')
col2.metric('Remuneração Semanal', value=f'£{player_stats["Wage (€)"]:,}')
col3.metric('Clausula de Rescisão', value=f'£{player_stats["Release Clause (€)"]:,}')