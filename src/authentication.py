import streamlit as st

def criar_conta(username, password):
    # Salvando os dados do usuário em um arquivo de texto
    with open('src/usuarios.txt', 'r') as file:
        existing_usernames = [line.strip().split(':')[0] for line in file if line.strip()]

    if username not in existing_usernames:
        with open('src/usuarios.txt', 'a') as file:
            file.write(f'{username}:{password}\n')
            st.success('Conta criada com sucesso!')
    else:
        st.error('O nome de usuário já existe. Por favor, escolha outro nome de usuário.')

def verificar_login(username, password):
    # Verificar se as credenciais do usuário existem no arquivo de texto
    with open('src/usuarios.txt', 'r') as file:
        for line in file:
            if line.strip():  # Verificar se a linha não está vazia
                user, pwd = line.strip().split(':')
                if user == username and pwd == password:
                    return True
    return False

def alterar_senha(username, new_password):
    # Alterar a senha do usuário no arquivo de texto
    with open('src/usuarios.txt', 'r') as file:
        lines = file.readlines()

    with open('src/usuarios.txt', 'w') as file:
        for line in lines:
            user_and_pwd = line.strip().split(':')
            if len(user_and_pwd) == 2:
                user, pwd = user_and_pwd
                if user == username:
                    file.write(f'{username}:{new_password}\n')
                else:
                    file.write(line)
            else:
                file.write(line)

def main():
    st.image("public/logo.png", width=200)
    st.title('Autenticação')
    page_bg_img =  f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://static.vecteezy.com/system/resources/previews/026/867/188/original/blue-wave-footer-free-png.png");
    background-size: 100% 20%;
    background-position: left bottom;
    background-repeat: no-repeat;
    background-attachment: local;
    overflow: hidden;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Seletor de opções para escolher entre criar conta, fazer login ou alterar senha
    escolha = st.selectbox("Escolha uma opção:", ["Já possui uma conta? Faça login", "Não possui conta? Criar Conta" ,"Esqueci minha senha"])

    if escolha == "Não possui conta? Criar Conta":
        # Formulário para criar conta
        with st.form(key='create_account_form'):
            st.subheader('Não possui conta? Criar Conta')
            username = st.text_input('Escolha um nome de usuário')
            password = st.text_input('Escolha uma senha', type='password')
            submit_button = st.form_submit_button(label='Criar Conta')

            if submit_button:
                if username and password:
                    criar_conta(username, password)

    elif escolha == "Já possui uma conta? Faça login":
        # Formulário para fazer login
       with st.form(key='login_form'):
            st.subheader('Já possui uma conta? Faça login')
            username_input = st.text_input('Usuário')
            password_input = st.text_input('Senha', type='password')
            submit_button = st.form_submit_button(label='Entrar')

            if submit_button:
                if verificar_login(username_input, password_input):
                    st.success('Login bem-sucedido!')
                    return True
                else:
                    st.error('Usuário ou senha incorretos.')
                    return False

    elif escolha == "Esqueci minha senha":
        # Formulário para alterar a senha
        with st.form(key='change_password_form'):
            st.subheader('Esqueci minha senha')
            username = st.text_input('Digite seu nome de usuário')
            new_password = st.text_input('Digite a nova senha', type='password')
            submit_button = st.form_submit_button(label='Alterar Senha')

            if submit_button:
                if username and new_password:
                    alterar_senha(username, new_password)
                    st.success('Senha alterada com sucesso!')

    st.markdown("---")
    st.markdown("&copy; 2024 EasyPSE - All rights reserved", unsafe_allow_html=True)

if __name__ == '__main__':
    main()








