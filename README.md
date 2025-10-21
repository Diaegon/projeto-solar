# Projeto Solar Automático

Sistema para automatização de projetos de energia solar residenciais e comerciais.  
O programa recebe os dados do cliente e gera automaticamente toda a documentação necessária, poupando tempo com preenchimentos repetitivos e cálculos simples.

## Funcionalidades previstas

- Geração automática de documentos:  
  - Memorial descritivo  
  - Diagrama unifilar  
  - Diagrama de situação (se necessário)  
  - Formulário de entrada (modelo ENEL-CE)  
  - Procuração particular  
  - PDF com dados para TRT/ART  
- Criação de banco de dados de equipamentos (inversores, placas etc.)  
- Interface para entrada de dados e gerenciamento do banco  
- Organização automática dos documentos em pastas por cliente  

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


 
