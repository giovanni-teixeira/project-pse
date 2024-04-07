import streamlit as st
import pandas as pd
import plotly.express as px


def render_motivacoes(df):

    col1, col2 = st.columns(2)

    with col1:
        # Gráfico Pizza: Como conheceu a FATEC Franca?
        st.subheader("Como conheceu a FATEC Franca?")
        if 'Estamos quase acabando... Como conheceu a FATEC Franca?' in df.columns:
            # Contar o número de ocorrências de cada opção
            conheceu_counts = df['Estamos quase acabando... Como conheceu a FATEC Franca?'].value_counts().reset_index()
            conheceu_counts.columns = ['Meio', 'Contagem']
            # Criar o gráfico de pizza
            fig_conheceu = px.pie(conheceu_counts, values='Contagem', names='Meio', title='Estamos quase acabando... Como conheceu a FATEC Franca?')
            st.plotly_chart(fig_conheceu, use_container_width=True, responsive=True)
        else:
            st.write("A coluna 'Estamos quase acabando... Como conheceu a FATEC Franca?' não foi encontrada nos dados.")

        # Gráfico Barra: Porque você escolheu este curso?
        st.subheader("Por que você escolheu este curso?")
        if 'Porque você escolheu este curso?' in df.columns:
            # Contar o número de ocorrências de cada opção
            motivo_counts = df['Porque você escolheu este curso?'].value_counts().reset_index()
            motivo_counts.columns = ['Motivo', 'Contagem']
            # Criar o gráfico de barras
            fig_motivo = px.pie(motivo_counts, names='Motivo', values='Contagem', title='Por que você escolheu este curso?', color_discrete_sequence=px.colors.qualitative.Prism,
                                labels={'Motivo': 'Motivo', 'Contagem': 'Contagem'})
            st.plotly_chart(fig_motivo, use_container_width=True, responsive=True)
        else:
            st.write("A coluna 'Porque você escolheu este curso?' não foi encontrada nos dados.")

        # Gráfico Barra: Qual sua maior expectativa quanto ao curso?
        st.subheader("Qual sua maior expectativa quanto ao curso?")
        if 'Qual sua maior expectativa quanto ao curso?' in df.columns:
            # Contar o número de ocorrências de cada opção
            expectativa_counts = df['Qual sua maior expectativa quanto ao curso?'].value_counts().reset_index()
            expectativa_counts.columns = ['Expectativa', 'Contagem']
            # Criar o gráfico de barras
            fig_expectativa = px.bar(expectativa_counts, x='Expectativa', y='Contagem', title='Maior Expectativa quanto ao Curso',
                                    color='Expectativa', labels={'Expectativa': 'Expectativa', 'Contagem': 'Contagem'})
            st.plotly_chart(fig_expectativa, use_container_width=True, responsive=True)
        else:
            st.write("A coluna 'Qual sua maior expectativa quanto ao curso?' não foi encontrada nos dados.")

        # Gráfico Barra: Qual sua expectativa após se formar?
        st.subheader("Qual sua expectativa após se formar?")
        if 'Qual sua expectativa após se formar?' in df.columns:
            # Contar o número de ocorrências de cada opção
            expectativa_formar_counts = df['Qual sua expectativa após se formar?'].value_counts().reset_index()
            expectativa_formar_counts.columns = ['Expectativa após se formar', 'Contagem']
            # Criar o gráfico de barras
            fig_formar = px.bar(expectativa_formar_counts, x='Expectativa após se formar', y='Contagem', 
                                title='Expectativa após se formar', color='Expectativa após se formar',
                                labels={'Expectativa após se formar': 'Expectativa após se formar', 'Contagem': 'Contagem'})
            st.plotly_chart(fig_formar, use_container_width=True, responsive=True)
        else:
            st.write("A coluna 'Qual sua expectativa após se formar?' não foi encontrada nos dados.")

    with col2:

        # Gráfico Pizza: Você já estudou nesta escola?
        st.subheader("Você já estudou nesta escola?")
        if 'Você já estudou nesta escola?' in df.columns:
            # Contar o número de ocorrências de cada opção
            estudou_counts = df['Você já estudou nesta escola?'].value_counts().reset_index()
            estudou_counts.columns = ['Resposta', 'Contagem']
            # Criar o gráfico de pizza
            fig_estudou = px.pie(estudou_counts, values='Contagem', names='Resposta', title='Você já estudou nesta escola?')
            st.plotly_chart(fig_estudou, use_container_width=True, responsive=True)
        else:
            st.write("A coluna 'Você já estudou nesta escola?' não foi encontrada nos dados.")

        # Gráfico Pizza: Você fez algum curso técnico?
        st.subheader("Você fez algum curso técnico?")
        if 'Você fez algum curso técnico?' in df.columns:
            # Contar o número de ocorrências de cada opção
            curso_tecnico_counts = df['Você fez algum curso técnico?'].value_counts().reset_index()
            curso_tecnico_counts.columns = ['Resposta', 'Contagem']
            # Criar o gráfico de pizza
            fig_curso_tecnico = px.pie(curso_tecnico_counts, values='Contagem', names='Resposta', title='Você fez algum curso técnico?')
            st.plotly_chart(fig_curso_tecnico, use_container_width=True, responsive=True)
        else:
            st.write("A coluna 'Você fez algum curso técnico?' não foi encontrada nos dados.")

        # Gráfico Pizza: Qual o meio de transporte você usa para vir à escola?
        st.subheader("Qual o meio de transporte você usa para vir à escola?")
        if 'Qual o meio de transporte você usa para vir à escola?' in df.columns:
            # Contar o número de ocorrências de cada opção
            transporte_counts = df['Qual o meio de transporte você usa para vir à escola?'].value_counts().reset_index()
            transporte_counts.columns = ['Meio de transporte', 'Contagem']
            # Criar o gráfico de pizza
            fig_transporte = px.pie(transporte_counts, values='Contagem', names='Meio de transporte', 
                                    title='Meio de transporte usado para vir à escola', color_discrete_sequence=px.colors.qualitative.Prism)
            st.plotly_chart(fig_transporte, use_container_width=True, responsive=True)
        else:
            st.write("A coluna 'Qual o meio de transporte você usa para vir à escola?' não foi encontrada nos dados.")