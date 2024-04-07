import streamlit as st
import pandas as pd
import plotly.express as px


def render_trabalho(df):

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)
    col7, col8 = st.columns(2)

                # Gráfico Pizza: Vamos tratar sobre trabalho agora...
    with col1:
        
        st.subheader("Vamos tratar sobre trabalho agora...")

    # Procurar a coluna que contenha o texto relevante, ignorando espaços em branco no início ou no final
        column_name = [col for col in df.columns if 'Vamos tratar sobre trabalho agora..' in col.strip()]
        if column_name:
            column_name = column_name[0]
            
            # Contar o número de ocorrências de cada valor
            work_topic_counts = df[column_name].value_counts().reset_index()
            work_topic_counts.columns = ['Tópico', 'Contagem']

            # Criar o gráfico de pizza
            fig_work_topic = px.pie(work_topic_counts, values='Contagem', names='Tópico', title='Vamos tratar sobre trabalho agora...')
            st.plotly_chart(fig_work_topic, use_container_width=True, responsive=True)
        else:
            st.write("A coluna 'Vamos tratar sobre trabalho agora...' não foi encontrada nos dados.")

                # Gráfico Barra: Qual o seu vínculo com o emprego?
    with col2:
                    st.subheader("Qual o seu vínculo com o emprego?")
                    employment_type_counts = df['Qual o seu vínculo com o emprego?'].value_counts()
                    fig_employment_type = px.bar(employment_type_counts, x=employment_type_counts.index, y=employment_type_counts.values, 
                                                title='Vínculo com o Emprego', labels={'x': 'Vínculo com o Emprego', 'y': 'Contagem'},
                                                color=employment_type_counts.index)
                    st.plotly_chart(fig_employment_type, use_container_width=True, responsive=True)

                # Gráfico Barra: Qual a área do seu trabalho?
    with col3:
                    st.subheader("Qual a área do seu trabalho?")
                    work_area_counts = df['Qual a área do seu trabalho?'].value_counts()
                    fig_work_area = px.bar(work_area_counts, x=work_area_counts.index, y=work_area_counts.values, 
                                           title='Área do Trabalho', labels={'x': 'Área do Trabalho', 'y': 'Contagem'},
                                           color=work_area_counts.index)
                    st.plotly_chart(fig_work_area, use_container_width=True, responsive=True)

                # Gráfico Barra: Qual seu horário de trabalho?
    with col4:
                    st.subheader("Qual seu horário de trabalho?")
                    work_hours_counts = df['Qual seu horário de trabalho?'].value_counts()
                    fig_work_hours = px.bar(work_hours_counts, x=work_hours_counts.index, y=work_hours_counts.values, 
                                            title='Horário de Trabalho', labels={'x': 'Horário de Trabalho', 'y': 'Contagem'},
                                            color=work_hours_counts.index)
                    st.plotly_chart(fig_work_hours, use_container_width=True, responsive=True)

                # Gráfico Barra: Qual a empresa que você está contratado agora?
    with col5:
                    st.subheader("Qual a empresa que você está contratado agora?")
                    company_counts = df['Qual a empresa que você está contratado agora?'].value_counts()
                    fig_company = px.bar(company_counts, x=company_counts.index, y=company_counts.values, 
                                         title='Empresa', labels={'x': 'Empresa', 'y': 'Contagem'})
                    st.plotly_chart(fig_company, use_container_width=True, responsive=True)

                # Gráfico Pizza: Você tem plano de saúde privado?
    with col6:
                    st.subheader("Você tem plano de saúde privado?")
                    health_insurance_counts = df['Você tem plano de saúde privado?'].value_counts()
                    fig_health_insurance = px.pie(health_insurance_counts, values=health_insurance_counts.values, 
                                                  names=health_insurance_counts.index, title='Plano de Saúde Privado',
                                                  color_discrete_sequence=px.colors.qualitative.Prism)
                    st.plotly_chart(fig_health_insurance, use_container_width=True, responsive=True)

                # Gráfico Barra: Qual o grau de escolaridade do seu pai?
    with col7:
                    st.subheader("Qual o grau de escolaridade do seu pai?")
                    father_education_counts = df['Qual o grau de escolaridade do seu pai?'].value_counts()
                    fig_father_education = px.bar(father_education_counts, x=father_education_counts.index, y=father_education_counts.values, 
                                                  title='Escolaridade do Pai', labels={'x': 'Escolaridade', 'y': 'Contagem'},
                                                  color=father_education_counts.index)
                    st.plotly_chart(fig_father_education, use_container_width=True, responsive=True)

                # Gráfico Barra: Qual o grau de escolaridade da sua mãe?
    with col8:
                    st.subheader("Qual o grau de escolaridade da sua mãe?")
                    mother_education_counts = df['Qual o grau de escolaridade da sua mãe?'].value_counts()
                    fig_mother_education = px.bar(mother_education_counts, x=mother_education_counts.index, y=mother_education_counts.values, 
                                                  title='Escolaridade da Mãe', labels={'x': 'Escolaridade', 'y': 'Contagem'},
                                                  color=mother_education_counts.index)
                    st.plotly_chart(fig_mother_education, use_container_width=True, responsive=True)            