import streamlit as st
from src import authentication
import dashboard
from PIL import Image

# Configuração da Página
 
favicon = Image.open('public/favicon.png')
st.set_page_config(page_title="EasyPSE - Dashboard Facilitado", 
                   layout='wide',
                   page_icon=favicon)

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown(
            """
            <style>
            /* Importe a fonte Poppins do Google Fonts */
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

            /* Aplique a fonte Poppins a todos os elementos do Streamlit */
            body {
                font-family: 'Poppins', sans-serif;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

# Função principal
def main():

    # Inicializar a session_state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    # Executar a autenticação apenas se o usuário não estiver logado
    if not st.session_state.logged_in:
        with st.spinner('Carregando...'):
            st.session_state.logged_in = authentication.main()

    # Após o login bem-sucedido, exibir o dashboard
    if st.session_state.logged_in:
        dashboard.dashboard()

if __name__ == "__main__":
    main()
