import streamlit as st
import pandas as pd
import plotly.express as px


def render_info_pessoais(df):
    
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)

    #Gráfico de "Qual o estado do Brasil que você nasceu?"           
    with col1:
        st.subheader("Qual o estado do Brasil que você nasceu?")
        state_birth_counts = df['Qual o estado do Brasil que você nasceu?'].value_counts()
        fig_state_birth = px.pie(values=state_birth_counts.values, names=state_birth_counts.index, title='Estado de Nascimento')
        st.plotly_chart(fig_state_birth, use_container_width=True, responsive=True)

    #Gráfico de "Qual sua cidade de residência?"
    with col2:
        st.subheader("Qual sua cidade de residência?")
        city_residence_counts = df['Qual sua cidade de residência?'].value_counts()
        fig_city_residence = px.pie(values=city_residence_counts.values, names=city_residence_counts.index, title='Cidade de Residência')
        st.plotly_chart(fig_city_residence, use_container_width=True, responsive=True)

    #Gráfico de "Qual o seu gênero?"
    with col3:
        st.subheader("Qual o seu gênero?")
        gender_counts = df['Qual o seu gênero?'].value_counts()
        fig_gender = px.pie(values=gender_counts.values, names=gender_counts.index, title='Gênero',
                            color_discrete_sequence=px.colors.qualitative.Prism)
        st.plotly_chart(fig_gender, use_container_width=True, responsive=True)

    #Gráfico de "Qual a sua data de nascimento?"
    with col4:
        st.subheader("Qual a sua data de nascimento?")
        if 'Qual a sua data de nascimento?' in df.columns:
            df['Idade'] = pd.to_datetime('today').year - pd.to_datetime(df['Qual a sua data de nascimento?']).dt.year
            age_bins = [0, 20, 25, 30, 35, 40, 45, df['Idade'].max()]
            age_labels = ['18 - 20', '21 - 25', '26 - 30', '31 - 35', '36 - 40', '41 - 45', f'{df["Idade"].max()}+']
            df['Faixa Etária'] = pd.cut(df['Idade'], bins=age_bins, labels=age_labels, right=False)
            age_counts = df['Faixa Etária'].value_counts().sort_index()

            # Criar um dicionário de cores para associar cada faixa etária a uma cor
            age_colors = px.colors.qualitative.Plotly[:len(age_counts)]

            # Criar o gráfico de barras com cores distintas para cada faixa etária
            fig_age = px.bar(x=age_counts.index, y=age_counts.values, labels={'x': 'Faixa Etária', 'y': 'Contagem'}, 
                            title='Idades', color=age_counts.index, color_discrete_map={age_labels[i]: age_colors[i] for i in range(len(age_labels))})
            st.plotly_chart(fig_age, use_container_width=True, responsive=True)
                
    #Gráfico de "Qual é o seu estado civil?"
    with col5:
        st.subheader("Qual é o seu estado civil?")
        if 'Qual é o seu estado civil?' in df.columns:
        # Contagem das categorias de estado civil
            marital_status_counts = df['Qual é o seu estado civil?'].value_counts().reset_index()
            marital_status_counts.columns = ['Estado Civil', 'Contagem']

        # Criar o gráfico de barras
            fig_marital_status = px.bar(marital_status_counts, x='Estado Civil', y='Contagem', 
                                    color='Estado Civil', labels={'Contagem': 'Contagem '}, 
                                    title='Estado Civil')
            st.plotly_chart(fig_marital_status, use_container_width=True, responsive=True)

    #Gráfico de "Você é portador de alguma deficiência?"
        st.subheader("Você é portador de alguma deficiência?")
        column_name = [col for col in df.columns if 'Você é portador de alguma deficiência?' in col.strip()]
        if column_name:
            column_name = column_name[0]
            
            # Contar o número de ocorrências de cada valor
            disability_counts = df[column_name].value_counts().reset_index()
            disability_counts.columns = ['Deficiência', 'Contagem']

            # Criar o gráfico de barras
            fig_disability = px.bar(disability_counts, x='Deficiência', y='Contagem', 
                                    title='Portador de Deficiência', color='Deficiência',
                                    labels={'Deficiência': 'Deficiência ', 'Contagem': 'Contagem '})
            st.plotly_chart(fig_disability, use_container_width=True, responsive=True)
        else:
            st.write("A coluna 'Você é portador de alguma deficiência?' não foi encontrada nos dados.")

                #Gráfico de "Quantos filhos você tem?"
        with col6:
            st.subheader("Quantos filhos você tem?")
            # Verificar se a coluna existe no DataFrame
            if 'Quantos filhos você tem?' in df.columns:
                        # Contagem das categorias de quantidade de filhos
                children_counts = df['Quantos filhos você tem?'].value_counts().reset_index()
                children_counts.columns = ['Quantidade de Filhos', 'Contagem']

                # Criar o gráfico de barras
                fig_children = px.bar(children_counts, x='Quantidade de Filhos', y='Contagem', 
                                      color='Quantidade de Filhos', labels={'Contagem': 'Contagem'}, 
                                      title='Quantidade de Filhos')
                st.plotly_chart(fig_children, use_container_width=True, responsive=True)
