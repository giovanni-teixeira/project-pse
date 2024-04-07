import streamlit as st
import plotly.express as px


def render_equipamentos(df):

    # Tópicos para os gráficos
    topics = [
              "Televisor", "Video cassete e(ou) DVD", "Microcomputador de mesa", 
               "Notebook", "Rádio", "Telefone fixo", "Smartphone", "Celular comum", 
               "TV por assinatura", "Internet", "Automóvel", "Motocicleta", 
               "Geladeira", "Máquina de lavar roupa e(ou) Tanquinho", "Empregada mensalista"
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
                st.plotly_chart(fig,  use_container_width=True, responsive=True)
            with cols[i][1]:
                if 2*i+1 < len(topics):
                    st.subheader(topics[2*i+1])
                    topic_counts = df[topics[2*i+1]].value_counts()
                    fig = px.bar(x=topic_counts.index, y=topic_counts.values, labels={'x': topics[2*i+1], 'y': 'Contagem'}, title=topics[2*i+1], color=topic_counts.index)
                    st.plotly_chart(fig,  use_container_width=True, responsive=True)