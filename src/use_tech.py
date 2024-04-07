import streamlit as st
import plotly.express as px

def render_user_tech(df):
    
    col1, col2 = st.columns(2)

    with col1:

                # Gráfico Barra: Na sua vida escolar você estudou...
                    st.subheader("Na sua vida escolar você estudou...")
                    school_education_counts = df['Na sua vida escolar você estudou...'].value_counts()
                    fig_school_education = px.bar(school_education_counts, x=school_education_counts.index, y=school_education_counts.values, 
                                                title='Estudo na Vida Escolar', labels={'x': 'Opções', 'y': 'Contagem'},
                                                color=school_education_counts.index)
                    st.plotly_chart(fig_school_education, use_container_width=True, responsive=True)

                # Gráfico Barra: Com que frequência você utiliza microcomputadores?
                    st.subheader("Com que frequência você utiliza microcomputadores?")
                    computer_usage_counts = df['Com que frequência você utiliza microcomputadores?'].value_counts()
                    fig_computer_usage = px.bar(computer_usage_counts, x=computer_usage_counts.index, y=computer_usage_counts.values, 
                                                title='Frequência de Uso de Microcomputadores', labels={'x': 'Frequência', 'y': 'Contagem'}, 
                                                color=computer_usage_counts.index)
                    st.plotly_chart(fig_computer_usage, use_container_width=True, responsive=True)
                # Gráfico Pizza: Em casa
                    st.subheader("Em casa")
                    home_usage_counts = df['Em casa'].value_counts()
                    fig_home_usage = px.pie(home_usage_counts, values=home_usage_counts.values, names=home_usage_counts.index, 
                                            title='Uso de Tecnologia em Casa',color_discrete_sequence=px.colors.qualitative.Prism)
                    st.plotly_chart(fig_home_usage, use_container_width=True, responsive=True)

                # Gráfico Pizza: No trabalho
                    st.subheader("No trabalho")
                    work_usage_counts = df['No trabalho'].value_counts()
                    fig_work_usage = px.pie(work_usage_counts, values=work_usage_counts.values, names=work_usage_counts.index, 
                                            title='Uso de Tecnologia no Trabalho')
                    st.plotly_chart(fig_work_usage, use_container_width=True, responsive=True)

                # Gráfico Pizza: Na escola
                    st.subheader("Na escola")
                    school_usage_counts = df['Na escola'].value_counts()
                    fig_school_usage = px.pie(school_usage_counts, values=school_usage_counts.values, names=school_usage_counts.index, 
                                            title='Uso de Tecnologia na Escola', color_discrete_sequence=px.colors.qualitative.Prism)
                    st.plotly_chart(fig_school_usage, use_container_width=True, responsive=True)

                # Gráfico Pizza: Em outros lugares
                    st.subheader("Em outros lugares")
                    other_usage_counts = df['Em outros lugares'].value_counts()
                    fig_other_usage = px.pie(other_usage_counts, values=other_usage_counts.values, names=other_usage_counts.index, 
                                            title='Uso de Tecnologia em Outros Lugares')
                    st.plotly_chart(fig_other_usage, use_container_width=True, responsive=True)

                #Gráfico Pizza: Para trabalhos profissionais
                    st.subheader("Para trabalhos profissionais")
                    professional_work_counts = df ['Para trabalhos profissionais'].value_counts()
                    fig_professional_work = px.pie(professional_work_counts, values=professional_work_counts, names=professional_work_counts,
                                                   title='Uso de Tecnologia para Trabalhos Profissionais', color_discrete_sequence=px.colors.qualitative.Prism)
                    st.plotly_chart(fig_professional_work, use_container_width=True, responsive=True)

                # Gráfico Pizza: Para trabalhos escolares
                    st.subheader("Para trabalhos escolares")
                    schoolwork_usage_counts = df['Para trabalhos escolares'].value_counts()
                    fig_schoolwork_usage = px.pie(schoolwork_usage_counts, values=schoolwork_usage_counts.values, names=schoolwork_usage_counts.index, 
                                                title='Uso de Tecnologia para Trabalhos Escolares')
                    st.plotly_chart(fig_schoolwork_usage, use_container_width=True, responsive=True)

                # Gráfico Pizza: Para entretenimento (músicas, vídeos, redes sociais, etc)
                    st.subheader("Para entretenimento")
                    entertainment_usage_counts = df['Para entretenimento (músicas, vídeos, redes sociais, etc)'].value_counts()
                    fig_entertainment_usage = px.pie(entertainment_usage_counts, values=entertainment_usage_counts.values, names=entertainment_usage_counts.index, 
                                                    title='Uso de Tecnologia para Entretenimento', color_discrete_sequence=px.colors.qualitative.Prism)
                    st.plotly_chart(fig_entertainment_usage, use_container_width=True, responsive=True)

                # Gráfico Pizza: Para comunicação por e-mail
                    st.subheader("Para comunicação por e-mail")
                    email_usage_counts = df['Para comunicação por e-mail'].value_counts()
                    fig_email_usage = px.pie(email_usage_counts, values=email_usage_counts.values, names=email_usage_counts.index, 
                                            title='Uso de Tecnologia para E-mails')
                    st.plotly_chart(fig_email_usage, use_container_width=True, responsive=True)

                # Gráfico Pizza: Para operações bancárias
                    st.subheader("Para operações bancárias")
                    banking_usage_counts = df['Para operações bancárias'].value_counts()
                    fig_banking_usage = px.pie(banking_usage_counts, values=banking_usage_counts.values, names=banking_usage_counts.index, 
                                                title='Uso de Tecnologia para Operações Bancárias', color_discrete_sequence=px.colors.qualitative.Prism)
                    st.plotly_chart(fig_banking_usage, use_container_width=True, responsive=True)

                
    with col2:
                    
                # Gráfico Pizza: Para compras eletrônicas
                    st.subheader("Para compras eletrônicas")
                    ecommerce_usage_counts = df['Para compras eletrônicas'].value_counts()
                    fig_ecommerce_usage = px.pie(ecommerce_usage_counts, values=ecommerce_usage_counts.values, names=ecommerce_usage_counts.index, 
                                                title='Uso de Tecnologia para Compras Online')
                    st.plotly_chart(fig_ecommerce_usage, use_container_width=True, responsive=True)

                # Gráfico Barra: Como você classifica seu conhecimento em informática?
                    st.subheader("Como você classifica seu conhecimento em informática?")
                    column_name = [col for col in df.columns if 'Como você classifica seu conhecimento em informática?' in col.strip()]
                    if column_name:
                        column_name = column_name[0]
                        
                        # Contar o número de ocorrências de cada valor
                        knowledge_counts = df[column_name].value_counts().reset_index()
                        knowledge_counts.columns = ['Nível de Conhecimento', 'Contagem']

                        # Criar o gráfico de barras
                        fig_knowledge = px.bar(knowledge_counts, x='Nível de Conhecimento', y='Contagem', 
                                            title='Nível de Conhecimento em Informática', color='Nível de Conhecimento',
                                            labels={'Nível de Conhecimento': 'Nível de Conhecimento', 'Contagem': 'Contagem'})
                        st.plotly_chart(fig_knowledge, use_container_width=True, responsive=True)
                    else:
                        st.write("A coluna 'Como você classifica seu conhecimento em informática?' não foi encontrada nos dados.")

                # Gráfico Barra: Windows
                    st.subheader("Windows")
                    windows_counts = df['Windows'].value_counts()
                    fig_windows = px.bar(windows_counts, x=windows_counts.index, y=windows_counts.values, 
                                        title='Uso de Windows', labels={'x': 'Opções', 'y': 'Contagem'},
                                        color=windows_counts.index)
                    st.plotly_chart(fig_windows, use_container_width=True, responsive=True)

                # Gráfico Barra: Linux
                    st.subheader("Linux")
                    linux_counts = df['Linux'].value_counts()
                    fig_linux = px.bar(linux_counts, x=linux_counts.index, y=linux_counts.values, 
                                    title='Uso de Linux', labels={'x': 'Opções', 'y': 'Contagem'},
                                    color=linux_counts.index)
                    st.plotly_chart(fig_linux, use_container_width=True, responsive=True)

                # Gráfico Barra: Editores de textos (Word, Writer, etc.)
                    st.subheader("Editores de textos")
                    text_editors_counts = df['Editores de textos (Word, Writer, etc.)'].value_counts()
                    fig_text_editors = px.bar(text_editors_counts, x=text_editors_counts.index, y=text_editors_counts.values, 
                                            title='Uso de Editores de Texto', labels={'x': 'Opções', 'y': 'Contagem'},
                                            color=text_editors_counts.index)
                    st.plotly_chart(fig_text_editors, use_container_width=True, responsive=True)

                # Gráfico Barra: Planilhas eletrônicas (Excel, Calc, etc.)
                    st.subheader("Planilhas eletrônicas")
                    spreadsheets_counts = df['Planilhas eletrônicas (Excel, Calc, etc.)'].value_counts()
                    fig_spreadsheets = px.bar(spreadsheets_counts, x=spreadsheets_counts.index, y=spreadsheets_counts.values, 
                                            title='Uso de Planilhas Eletrônicas', labels={'x': 'Opções', 'y': 'Contagem'},
                                            color=spreadsheets_counts.index)
                    st.plotly_chart(fig_spreadsheets, use_container_width=True, responsive=True)

                # Gráfico Barra: Apresentadores (Powerpoint, Impress, Prezzi, etc.)
                    st.subheader("Apresentadores")
                    presenters_counts = df['Apresentadores (Powerpoint, Impress, Prezzi, etc.)'].value_counts()
                    fig_presenters = px.bar(presenters_counts, x=presenters_counts.index, y=presenters_counts.values, 
                                            title='Uso de Apresentadores', labels={'x': 'Opções', 'y': 'Contagem'}, 
                                            color=presenters_counts.index)
                    st.plotly_chart(fig_presenters, use_container_width=True, responsive=True)

                # Gráfico Barra: Sistemas de Gestão Empresarial
                    st.subheader("Sistemas de Gestão Empresarial")
                    erp_counts = df['Sistemas de Gestão Empresarial'].value_counts()
                    fig_erp = px.bar(erp_counts, x=erp_counts.index, y=erp_counts.values, 
                                    title='Uso de Sistemas de Gestão Empresarial', labels={'x': 'Opções', 'y': 'Contagem'},
                                    color=erp_counts.index)
                    st.plotly_chart(fig_erp, use_container_width=True, responsive=True)

                # Gráfico Barra: Inglês
                    st.subheader("Inglês")
                    english_counts = df['Inglês'].value_counts()
                    fig_english = px.bar(english_counts, x=english_counts.index, y=english_counts.values, 
                                        title='Uso do Inglês', labels={'x': 'Opções', 'y': 'Contagem'},
                                        color=english_counts.index)
                    st.plotly_chart(fig_english, use_container_width=True, responsive=True)

                # Gráfico Barra: Espanhol
                    st.subheader("Espanhol")
                    spanish_counts = df['Espanhol'].value_counts()
                    fig_spanish = px.bar(spanish_counts, x=spanish_counts.index, y=spanish_counts.values, 
                                        title='Uso do Espanhol', labels={'x': 'Opções', 'y': 'Contagem'},
                                        color=spanish_counts.index)
                    st.plotly_chart(fig_spanish, use_container_width=True, responsive=True)

                # Gráfico Barra: Outros Idiomas
                    st.subheader("Outros Idiomas")
                    other_languages_counts = df['Outros Idiomas'].value_counts()
                    fig_other_languages = px.bar(other_languages_counts, x=other_languages_counts.index, y=other_languages_counts.values, 
                                                title='Uso de Outros Idiomas', labels={'x': 'Opções', 'y': 'Contagem'}, 
                                                color=other_languages_counts.index)
                    st.plotly_chart(fig_other_languages, use_container_width=True, responsive=True)