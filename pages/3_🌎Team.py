import streamlit as st
import pandas as pd

st.set_page_config('Clube',page_icon='⚽',layout='wide')

df = st.session_state['data']

clubes = df['Club'].unique()
club = st.sidebar.selectbox('Clube',clubes)


df_filtred = df[df['Club'] == club].set_index('Name')

st.image(df_filtred.iloc[0]['Club Logo'])
st.markdown(f"## {club}")

columns = ['Age', 'Photo', 'Nationality', 'Flag', 'Overall', 'Potential',
       'Club', 'Value (€)', 'Wage (€)',
       'Preferred Foot', 'International Reputation','Position',
       'Joined', 'Contract Valid Until', 'Height', 'Weight',
       'Release Clause (€)', 'Kit Number']

st.dataframe(df_filtred[columns],column_config={
    'Overall' : st.column_config.ProgressColumn('Overall', format="%d",min_value=0,max_value=100),
    'Photo' : st.column_config.ImageColumn(),
    'Value (€)' : st.column_config.NumberColumn(),
    'Wage (€)' : st.column_config.ProgressColumn('Wage (€)', format="%d",min_value=0,max_value=df_filtred['Wage (€)'].max()),
    'Flag' : st.column_config.ImageColumn('Country')
})