# Projeto EasyPSE

O EasyPSE é um projeto de dashboard de dados desenvolvido para análise e visualização de informações coletadas em pesquisas socioeconômicas. O objetivo do projeto é fornecer uma interface amigável e interativa para explorar e compreender os dados de forma mais eficiente.

### Arquitetura do Projeto

O projeto EasyPSE segue uma arquitetura simples, composta por diferentes módulos e componentes que trabalham juntos para criar o dashboard de dados. A estrutura básica do projeto é a seguinte:

-   **app.py**: O arquivo principal do aplicativo, que contém a lógica de inicialização e configuração do Streamlit, bem como a definição das diferentes páginas e funcionalidades do dashboard.
-   **dashboard.py**: Módulo responsável por renderizar as diferentes páginas do dashboard, cada uma focada em uma área específica de análise.
-   **src/**: Diretório contendo os módulos individuais para cada página do dashboard, onde a lógica de renderização dos gráficos e visualizações é implementada.
-   **public/**: Diretório para armazenar recursos estáticos, como imagens e ícones utilizados no dashboard.


### Ferramentas Utilizadas

O projeto EasyPSE foi desenvolvido utilizando as seguintes ferramentas e tecnologias:

-   **Streamlit**: Framework de código aberto para a criação de aplicativos web interativos com Python.
-   **Pandas**: Biblioteca de análise de dados para manipulação e processamento de conjuntos de dados.
-   **Plotly Express**: Biblioteca de visualização de dados para criação de gráficos interativos e dinâmicos.
-   **HTML e CSS**: Linguagens de marcação e estilização utilizadas para personalizar a aparência e o layout do dashboard.

### Como Rodar o Projeto

Para rodar o projeto EasyPSE localmente, siga estas etapas:

1.  Certifique-se de ter o Python instalado em seu computador.
2.  Clone este repositório para o seu ambiente local.
3.  Instale as dependências do projeto executando `pip install -r requirements.txt`.
4.  Navegue até o diretório raiz do projeto e execute `streamlit run app.py` no terminal.
5.  O dashboard será iniciado e estará disponível em seu navegador padrão.

### Para que Serve o Projeto

O projeto EasyPSE serve como uma ferramenta poderosa para análise e visualização de dados, especialmente em pesquisas socioeconômicas. Ele permite aos usuários explorar e compreender melhor os padrões e tendências nos dados coletados, facilitando a tomada de decisões informadas e a identificação de insights valiosos.
