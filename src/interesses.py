import pandas as pd
import plotly.express as px
import streamlit as st

def render_interesses(df):

    col1, col2 = st.columns(2)

    with col1:
        # Gráfico Pizza: Você dedica parte do seu tempo para atividades voluntárias?
        st.subheader("Você dedica parte do seu tempo para atividades voluntárias?")
        voluntario_counts = df['Você dedica parte do seu tempo para atividades voluntárias?'].value_counts()
        fig_voluntario = px.pie(voluntario_counts, values=voluntario_counts.values, names=voluntario_counts.index, 
                                title='Atividades Voluntárias', color_discrete_sequence=px.colors.qualitative.Prism)
        st.plotly_chart(fig_voluntario, use_container_width=True, responsive=True)

        # Gráfico Barra: Qual religião você professa?
        st.subheader("Qual religião você professa?")
        religiao_counts = df['Qual religião você professa?'].value_counts()
        fig_religiao = px.bar(religiao_counts, x=religiao_counts.index, y=religiao_counts.values, title='Religião', labels={'x': 'Religião', 'y': 'Contagem'},
                              color=religiao_counts.index)
        st.plotly_chart(fig_religiao, use_container_width=True, responsive=True)

        # Gráfico Pizza: Cinema
        st.subheader("Cinema")
        cinema_counts = df['Cinema'].value_counts()
        fig_cinema = px.pie(cinema_counts, values=cinema_counts.values, names=cinema_counts.index, title='Cinema', color=cinema_counts.values)
        st.plotly_chart(fig_cinema, use_container_width=True, responsive=True)

        # Gráfico Pizza: Exposição de Arte
        st.subheader("Exposição de Arte")
        arte_counts = df['Exposição de Arte'].value_counts()
        fig_arte = px.pie(arte_counts, values=arte_counts.values, names=arte_counts.index, title='Exposição de Arte', color_discrete_sequence=px.colors.qualitative.Prism)
        st.plotly_chart(fig_arte, use_container_width=True, responsive=True)

        # Gráfico Barra: Filmes na Internet
        st.subheader("Filmes na Internet")
        filmes_internet_counts = df['Filmes na Internet'].value_counts()
        fig_filmes_internet = px.bar(filmes_internet_counts, x=filmes_internet_counts.index, y=filmes_internet_counts.values, 
                                     title='Filmes na Internet', labels={'x': 'Opções', 'y': 'Contagem'}, color=filmes_internet_counts.index)
        st.plotly_chart(fig_filmes_internet, use_container_width=True, responsive=True)

        # Gráfico Pizza: Literatura
        st.subheader("Literatura")
        literatura_counts = df['Literatura'].value_counts()
        fig_literatura = px.pie(literatura_counts, values=literatura_counts.values, names=literatura_counts.index, title='Literatura',
                                color_discrete_sequence=px.colors.qualitative.Prism)
        st.plotly_chart(fig_literatura, use_container_width=True, responsive=True)

    with col2:
        # Gráfico Pizza: Museus
        st.subheader("Museus")
        museus_counts = df['Museus'].value_counts()
        fig_museus = px.pie(museus_counts, values=museus_counts.values, names=museus_counts.index, title='Museus')
        st.plotly_chart(fig_museus, use_container_width=True, responsive=True)

        # Gráfico Pizza: Música
        st.subheader("Música")
        musica_counts = df['Música'].value_counts()
        fig_musica = px.pie(musica_counts, values=musica_counts.values, names=musica_counts.index, title='Música', color_discrete_sequence=px.colors.qualitative.Prism)
        st.plotly_chart(fig_musica, use_container_width=True, responsive=True)

        # Gráfico Pizza: Teatro
        st.subheader("Teatro")
        teatro_counts = df['Teatro'].value_counts()
        fig_teatro = px.pie(teatro_counts, values=teatro_counts.values, names=teatro_counts.index, title='Teatro')
        st.plotly_chart(fig_teatro, use_container_width=True, responsive=True)

        # Gráfico Pizza: TV2
        st.subheader("TV2")
        tv_counts = df['TV2'].value_counts()
        fig_tv = px.pie(tv_counts, values=tv_counts.values, names=tv_counts.index, title='TV2', color_discrete_sequence=px.colors.qualitative.Prism)
        st.plotly_chart(fig_tv, use_container_width=True, responsive=True)

        # Gráfico Pizza: Viagens
        st.subheader("Viagens")
        viagens_counts = df['Viagens'].value_counts()
        fig_viagens = px.pie(viagens_counts, values=viagens_counts.values, names=viagens_counts.index, title='Viagens')
        st.plotly_chart(fig_viagens, use_container_width=True, responsive=True)

        # Gráfico Pizza: Nenhuma
        st.subheader("Nenhuma")
        nenhuma_counts = df['Nenhuma'].value_counts()
        fig_nenhuma = px.pie(nenhuma_counts, values=nenhuma_counts.values, names=nenhuma_counts.index, title='Nenhuma', color_discrete_sequence=px.colors.qualitative.Prism)
        st.plotly_chart(fig_nenhuma, use_container_width=True, responsive=True)
