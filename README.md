# Projeto Solar Automático

Sistema para automatização de projetos de energia solar residenciais e comerciais.  
O programa recebe os dados do cliente e gera automaticamente toda a documentação necessária, poupando tempo com preenchimentos repetitivos e cálculos simples.

## Funcionalidades previstas

- Geração automática de documentos:  
  - Memorial descritivo  (gerado com a biblioteca ReportLab)
  - Diagrama unifilar  (feito com a biblioteca PyMuPDF a partir de um template existente)
  - Diagrama de situação (se necessário)  
  - Formulário de entrada (modelo ENEL-CE)  (feito com a biblioteca PyMuPDF a partir de um template existente)
  - Procuração particular  (gerado com a biblioteca ReportLab)
  - PDF com dados para TRT/ART  (em produção)
- Criação de banco de dados de equipamentos (inversores, placas etc.)  (em produção)
- Interface para entrada de dados e gerenciamento do banco  (TKinter)
- Organização automática dos documentos em pastas por cliente  (em produção)

## Fases do projeto

1. **Memorial descritivo e definição de inputs**  
   - Entrada dos dados via arquivo JSON  
   - Suporte a múltiplos modelos de inversores e placas  

2. **Geração da documentação complementar**  
   - Diagrama unifilar  (arquivos bases com edição utilizando a biblioteca pymupdf)
   - Preenchimento automático dos formulários  (biblioteca pymupdf)
   - Geração de procuração e PDF FICHA DO CLIENTE  

3. **Banco de dados dinâmico**  (projeto do banco de dados vai correr em paralelo com o da geração de projetos)
   - Cadastro e atualização de novos modelos de equipamentos  
   - Geração automática de pastas organizadas por cliente  

4. **Desenvolvimento da interface gráfica**  
   - Interface para entrada de dados, execução do programa e edição do banco  

5. **Geração do diagrama de situação**  
   - Desenho automático da localização da residência e sistema a partir de coordenadas geográficas  

6. **Atualizações para melhoria do código**
   - Cadastrar os inversores com a quantidade de string de cada modelo para que se possa fazer uma lógica adaptativa para que o texto se modifique de acordo com o inversor.
   - Diminuir o código "equacoes.py" para que o programa adicione uma quantidade ilimitada de inversores/placas de acordo com o input, sem a limitação de 3 tipos de inversores diferentes. 

## Como usar (em desenvolvimento)
 DADOS DE ENTRADA:
 -Inicialmente os dados de entradas estão em formato .json, eles tem que ser preenchidos com strings, inteiros ou null-format. inteiros para valores de potencia, quantidade, etc. e string para o restante.
 -os dados de entrada são os dados pessoais do cliente juntamente com os dados do projetista, procurador/homologador, material utilizado e o padrão elétrico residencial do cliente.
 MEMORIAL DESCRITIVO / PROCURAÇÃO:
 -O memorial e procuração serão criados rodando no terminal o script gerar_pdf.py, ele vai pegar os dados de input, organizar e realizar os cálculos necessários para criar um memorial descritivo do sistema instalado
 de acordo com as normas vigentes.
 DIAGRAMA UNIFILAR:
 -O diagrama unifilar usa uma lógica de template, onde temos modelos pré-estabelecidos com 1, 2 ou 3 inversores e o programa vai decidir em qual desenhar a partir dos dados de entrada utilizando a biblioteca PyMuPDF.
 FORMULARIO ENEL-CE:
 -A mesma lógica de template aplicada no diagrama unifilar é aplicada aqui, tomando como base os formularios da ENEL-CE o programa escreve os dados do cliente no formulário correto de acordo com o projeto.

 para gerar todos os documentos basta instalar o poetry e dependências e na pasta raiz do arquivo rodar o script main.py.

 
