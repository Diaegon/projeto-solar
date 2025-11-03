def texto_introducao():


    return f"   O presente relatório técnico tem por objetivo apresentar o memorial descritivo \
                       para implantação de um Gerador Fotovoltaico de fabricação <b>{projeto.sistema_instalado.texto_final_inversor}</b>. \
                         Este modelo e quantidade de gerador foi previamente aprovado pelo proprietário da residência.\
                             Este gerador fotovoltaico se conectará ao sistema de baixa tensão, após a medição \
                                de energia da ENEL. O mesmo terá como objetivo suprir parte das cargas desta residencia. \
                                 A previsão de ligação do sistema elétrico é para <b>{data_futura.strftime("%d de %B de %Y")}</b>."

print(projeto.sistema_instalado.texto_final_inversor)
breakpoint()

def texto_loc():
    return f"No diagrama de situação é ilustrada a planta de situação da residência onde será \
 implantado na {inputs['endereco']['logradouro']}, {inputs['endereco']['numero_casa']}  {inputs['endereco']['complemento']}, {inputs['endereco']['municipio']}, {inputs['endereco']['estado']}. A tabela 2.1 \
 mostra o georeferenciamento da localidade de instalação e do gerador."

def texto_loc2():
    return "A área de telhado da residência foi escolhida por apresentar vantagens de insolação \
 permanente durante todas as horas do dia para evitar o sombreamento dos painéis \
 fotovoltaicos e segurança dos equipamentos"

def texto_carginst():
    return f"A carga instalada é típica de um estabelecimento {classeconsumo}, constituído de iluminação e \
 eletrodomésticos diversos, sendo {carga_cliente} kW.  A energia \
 media de consumo é de  {consumo_energia} kWh."

def texto_calculo_demanda():
    return "Considerando um mês comercial com 720 horas, pode-se calcular a demanda média \
 mensal através da equação:"

def texto_calculo_demanda2():
    return "Esta demanda média está dentro do limite da potência máxima injetada no sistema \
da ENEL, de acordo com a norma NT - 010."

def texto_calculo_fc():
    return "O fator de carga médio desta residência é calculado através da equação:"

def texto_geradorfv():
    texto_retorno = f"O Gerador Fotovoltaico escolhido para compor a geração suplementar da residência \
    Alvo deste projeto é composto de {texto_finalpaineis} e {texto_finalinversor}. \
O   modulo   solar   fotovoltaico   {texto_painel_tipo}  possui   as   características \
técnicas   apresentado   na   tabela   a seguir.   Considerando   que   os   módulos   instalados   são   os   de \
({texto_potencia_individual_paineis})  Wp, e que eles tem uma tensão elétrica de máxima potência (Vmp) de ({texto_tensao_individual_paineis})Vmp. A \
solução prevista para ser instalada tem {texto_disposicao}. Tendo um sistema total \
com {quantidade_total_painel} módulos que resultam numa potência total de {potencia_totalpainel:.2f} kWp." 
    
    return f"{texto_retorno}"

def texto_potenciafv():
    return f"O georeferenciamento do local da instalação do Gerador Fotovoltaico estabelece o \
valor de 74,5% das Condições de Teste padrão (STC) do modulo Fotovoltaico. Por essa \
premissa,  terei   uma   Potencia   resultante   do  meu  Gerador  Fotovoltaico  (GF)  também   de \
74,5% da Potencia instalada ({potencia_totalpainel:.2f} kW). Assim, a Potencia efetiva do GF é de  {potenciaefetiva:.2f}kW, o\
que satisfaz a demanda média calculada."

def texto_calculo_enegiagerada():
    return f"Considerando a potência média disponível de  {potenciaefetiva:.2f} kW  e a média anual do ponto \
georeferenciado do sistema Horas de Sol a Pico (HSP) que é de 5,84 kWh/m2/dia, como \
parâmetro de medição da radiação solar em um mês comercial, pode-se calcular a energia \
média através do produto destas duas grandezas, que resulta em {energia_gerada:.0f} kWh."

def texto_diagramas():
    return "A figura a seguir apresenta o esquema básico de ligação de um Gerador Fotovoltaico. \
Nesta   figura   pode   ser   ver   todas   as   partes   que   compõem   o   sistema,   desde   o   Gerador \
Fotovoltaico até a conexão à carga e à rede."

def texto_parametrizacao():
    return "O inversor para cumprir sua função de proteção, é parametrizado com os seguintes \
valores, de modo a não exceder os limites recomendados pela norma NT – 010 Coelce."

def texto_instalacao():
    return f"A residência é alimentada através da rede de baixa tensão da ENEL em {tensao_local}V. O \
ponto de entrega se dá em um quadro instalado junto ao muro da propriedade."

def texto_diagramauni():
    return "O diagrama unifilar geral se encontra em anexo."

def texto_dimensionamento_protecao():
    return f"Este   Gerador   Fotovoltaico   será   conectado   ao   barramento   de   baixa   tensão   do \
consumidor, logo abaixo da proteção geral, que é constituída por um disjuntor {fornecimento} \
de   {disjuntor_geral}   A.   Por   sua   vez,   o   ramal   de   interligação   do   Gerador   Fotovoltaico   ao   quadro   de \
medição é feito por  {texto_disjuntores_protecao}. Esta capacidade de condução foi \
calculada através da seguinte equação."

def texto_dimensionamento_protecao2():
    return f"A interligação entre o Gerador Fotovoltaico ({inversores_potencia}) kW e o quadro de medição será feito através \
de um cabo de cobre flexível, isolado em PVC com uma seção reta de ({texto_cabos})mm², e sua \
proteção se dará através de um disjuntor de {texto_disjuntores_protecao} A. \
O   dimensionamento   do   condutor   de   ({texto_cabos})  mm²   atende   aos   critérios   de   máxima \
capacidade de corrente, já que o mesmo tem capacidade térmica de conduzir até ({corrente_max_cabos}) A; e \
atende também ao critério de máxima queda de tensão. \
Como trata-se da interligação de um gerador, a máxima queda de tensão permitida é \
de 3%. A equação abaixo apresenta o cálculo desta queda." 

def texto_dimensionamento_protecao3():
    return f"Introduzindo estes valores na equação anterior resulta em uma queda de tensão de {texto_tensao_queda} , o que satisfaz plenamente o limite máximo de queda que é de 3%."

def texto_disjuntores():
    return f"A proteção geral é feita através de um disjuntor {fornecimento} de {disjuntor_geral} A, com curva \
direta de atuação C, e o Gerador Fotovoltaico terá a sua proteção realizada por  \
 {texto_disjuntores_protecao}, curva de atuação B. A seletividade é garantida observando o valor \
maior de corrente nominal do disjuntor principal em relação ao disjuntor para proteção do \
cabo do inversor, e suas curvas de atuação."

def texto_sinalizacao():
    return "No padrão de entrada será instalada placa de sinalização, confeccionada em \
PVC 2,0 mm com tratamento anti-UV, conforme Figura a seguir, fixada de acordo \
com o desenho D010.01 dá NT Br-010 R-01, sem que haja a perfuração da caixa para \
fixação da sinalização. "


#texto inversores memorial
inversor = f"{quantidade_inversor} " + "inversor" + f" {inversor_marca} {inversor_modelo}"


texto_disjuntores_protecao = [f"{quantidade_inversor} disjuntor de {disjuntor_protecao1} A"]
texto_cabos = [f"{cabo_inversor1}"]
corrente_max_cabos = [f"{corrente_max_cabo1}"]
texto_corrente_saida = [f"{corrente_saida:.2f} A"]
inversores_tensao = [f"{inversor_tensao}"]



texto_tensao_queda = [f"{tensao_queda:.2f} %"]  

## texto tabelas 


#tratamento tabela dos paineis
pot1 = inputs['painel']['potencia']
potencia_modulos_tabela = [f'{pot1}']
vmp1 = inputs['painel']['vp']
vmp_modulos_tabela = [f'{vmp1}']
imp1 = inputs['painel']['imp']
imp_modulos_tabela = [f'{imp1}']
voc1 = inputs['painel']['voc']
voc_modulos_tabela = [f'{voc1}']
isc1 = inputs['painel']['isc']
isc_modulos_tabela = [f'{isc1}']
if inputs['dados_cliente']['quantidade_painel2'] not in [None,0]:
    pot2 = inputs['painel2']['potencia']
    potencia_modulos_tabela.append(f'{pot2}')
    vmp2 = inputs['painel2']['vp']
    vmp_modulos_tabela.append(f'{vmp2}')
    imp2 = inputs['painel2']['imp']
    imp_modulos_tabela.append(f'{imp2}')
    voc2 = inputs['painel2']['voc']
    voc_modulos_tabela.append(f'{voc2}')
    isc2 = inputs['painel2']['isc']
    isc_modulos_tabela.append(f'{isc2}')
if inputs['dados_cliente']['quantidade_painel3'] not in [None,0]:
    pot3 = inputs['painel3']['potencia']
    potencia_modulos_tabela.append(f'{pot3}')
    vmp3 = inputs['painel3']['vp']
    vmp_modulos_tabela.append(f'{vmp3}')
    imp3 = inputs['painel3']['imp']
    imp_modulos_tabela.append(f'{imp3}')
    voc3 = inputs['painel3']['voc']
    voc_modulos_tabela.append(f'{voc3}')
    isc3 = inputs['painel3']['isc']
    isc_modulos_tabela.append(f'{isc3}')
potencia_modulos_tabela = ', '.join(potencia_modulos_tabela)

vmp_modulos_tabela = ', '.join(vmp_modulos_tabela)
imp_modulos_tabela = ', '.join(imp_modulos_tabela)
voc_modulos_tabela = ', '.join(voc_modulos_tabela)
isc_modulos_tabela = ', '.join(isc_modulos_tabela)
inversores_potencia = ', '.join(inversores_potencia)
texto_cabos = ", ".join(texto_cabos)
corrente_max_cabos = ", ".join(corrente_max_cabos)
texto_corrente_saida = ", ".join(texto_corrente_saida)
