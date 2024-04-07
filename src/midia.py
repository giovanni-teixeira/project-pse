import streamlit as st
import plotly.express as px


def render_midia(df):

    # Tópicos para os gráficos
    topics = [
              "TV", "Internet2", "Revistas", 
               "Jornais", "Rádio2", "Redes sociais", "Conversas com Amigos", "Se você lê jornal, qual a frequência?", 
               "Quando você lê jornal quais os assuntos que mais lê?", "Não considerando os livros escolares, quantos livros você lê por ano (em média)?", 
               "Se você lê livros literários, qual o gênero preferido?"
            ]

    # Organização dos gráficos em coluna
    cols = [st.columns(2) for _ in range(len(topics) // 2 + 1)]

    # Criar e exibir gráficos de barras para cada par de tópicos
    for i in range(len(topics) // 2 + 1):
        with cols[i][0]:
            if 2*i < len(topics):
                st.subheader(topics[2*i])
                topic_counts = df[topics[2*i]].value_counts()
                fig = px.bar(x=topic_counts.index, y=topic_counts.values, labels={'x': topics[2*i], 'y': 'Contagem'}, title=topics[2*i], color=topic_counts.index)
                st.plotly_chart(fig, use_container_width=True, responsive=True)
            with cols[i][1]:
                if 2*i+1 < len(topics):
                    st.subheader(topics[2*i+1])
                    topic_counts = df[topics[2*i+1]].value_counts()
                    fig = px.bar(x=topic_counts.index, y=topic_counts.values, labels={'x': topics[2*i+1], 'y': 'Contagem'}, title=topics[2*i+1], color=topic_counts.index)
                    st.plotly_chart(fig, use_container_width=True, responsive=True)