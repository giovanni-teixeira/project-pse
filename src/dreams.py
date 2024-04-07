import pandas as pd
import streamlit as st
import plotly.express as px

def render_dreams(df):

    # Criar uma lista para armazenar os subgrupos
    subgroups = {}

    # Lista de palavras-chave para cada subgrupo
    keywords = {
        "Estabilidade Financeira": ["estabilidade financeira", "financeiro", "salário", "renda"],
        "Aprendizado e Desenvolvimento": ["aprender", "conhecimento", "desenvolver", "crescer", "estudar"],
        "Família": ["família", "filhos", "casado", "esposa", "marido"],
        "Viagens": ["viajar", "mundo", "países", "explorar", "cultura"],
        "Empreendedorismo": ["empreender", "empresário", "negócio", "empresa"],
        "Carreira Profissional": ["profissão", "trabalho", "emprego", "cargo"],
        "Tecnologia e TI": ["tecnologia", "informática", "TI", "programação", "desenvolvedor"],
        "Realização Pessoal": ["realizar", "sonho", "objetivo", "vida", "futuro"]
    }

    # Iterar sobre cada opinião
    for index, row in df.iterrows():
        opinion = row["Escreva algumas linhas sobre sua história e seus sonhos de vida"].lower()  # Converter para minúsculas para tornar a busca de palavras-chave case-insensitive

        # Verificar palavras-chave em cada subgrupo
        for subgroup, keys in keywords.items():
            for key in keys:
                if key in opinion:
                    if subgroup not in subgroups:
                        subgroups[subgroup] = 0
                    subgroups[subgroup] += 1


    # Converter os subgrupos em DataFrame para plotar o gráfico
    df_subgroups = pd.DataFrame.from_dict(subgroups, orient="index", columns=["Quantidade"])
    df_subgroups.reset_index(inplace=True)
    df_subgroups.rename(columns={"index": "Subgrupo"}, inplace=True)

    
    fig_pie = px.pie(df_subgroups, values="Quantidade", names="Subgrupo", title="Distribuição de Sonhos e Objetivos", color_discrete_sequence=px.colors.qualitative.Prism)
    st.plotly_chart(fig_pie, use_container_width=True, responsive=True)
