import matplotlib.pyplot as plt
from reportlab.platypus import Image
from src.utils.helpers import projeto


print(projeto)


#dados importantes para os calculos
carga_cliente = projeto.carga_instalada_kw * 1000
consumo_energia = projeto.energia_media_mensal_kwh
classeconsumo = projeto.classe_consumo

resultado = consumo_energia / 720
fatordecarga = resultado / carga_cliente


#EQ. QUEDA DE TENSÃO
equacao4 = fr"$\Delta V \% = \frac{{200*\rho*L_c*I_c*cos\varphi}}{{S_c*V_f}}$"


def render_equation_to_image(equation, filename):
    fig = plt.figure(figsize=(3, 1))
    plt.text(0.5, 0.5, f"${equation}$", fontsize=20, ha='center', va='center')
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.1, dpi=200)
    plt.close()

def insert_equation(equation, story, img_filename):
    render_equation_to_image(equation, img_filename)
    img = Image(img_filename)
    img.drawHeight = 50
    img.drawWidth = 250
    story.append(img)


#EQUACOES
def numero_de_fases(numero_fases):
    if numero_fases == "monofasico":
        multiplicador = 1
        inversor_tensao = 220
    elif numero_fases == "trifasico":
        multiplicador = 1.732
        inversor_tensao = 380    
    return multiplicador, inversor_tensao

def corrente_saida_calc(inversor_potencia, multiplicador, inversor_tensao):
    corrente_saida = inversor_potencia / (multiplicador * inversor_tensao)
    return corrente_saida
def disjuntor_protecao_inversores(corrente_saida):
    if  corrente_saida < 15.9:
        cabo_inversor = 2.5
        disjuntor_protecao = 16
        corrente_max_cabo = 21
    elif 15.9 <= corrente_saida < 20:
        cabo_inversor = 2.5
        disjuntor_protecao = 20
        corrente_max_cabo = 21    
    elif 20 <= corrente_saida < 25:
        cabo_inversor = 4
        disjuntor_protecao = 25
        corrente_max_cabo = 28
    elif 25 <= corrente_saida < 28:
        cabo_inversor = 4
        disjuntor_protecao = 32
        corrente_max_cabo = 28     
    elif 28 <= corrente_saida < 32:
        cabo_inversor = 6
        disjuntor_protecao = 32
        corrente_max_cabo = 36
    elif 32 <= corrente_saida < 50:
        cabo_inversor = 10
        disjuntor_protecao = 40
        corrente_max_cabo = 50     
    elif 50 <= corrente_saida < 63:
        cabo_inversor = 16
        disjuntor_protecao = 63
        corrente_max_cabo = 68
    elif 63 <= corrente_saida < 80:
        cabo_inversor = 25
        disjuntor_protecao = 80
        corrente_max_cabo = 89
    return cabo_inversor, corrente_max_cabo, disjuntor_protecao

def quantidade_string(inversor_potencia):
    if inversor_potencia <= 7000:
        quantidade_stringsinversor1 = 2
    elif  7000 < inversor_potencia <= 10000:
        quantidade_stringsinversor1 = 3
    elif 10000 < inversor_potencia <= 17000:
        quantidade_stringsinversor1 = 4    
    elif 17000 < inversor_potencia <= 40000:
        quantidade_stringsinversor1 = 6 
    return quantidade_stringsinversor1

def get_classe_codigo(classe_cliente: str) -> str:
    classe_codigo = ""
    if classe_cliente == "residencial":
        classe_codigo = "B1"
    elif classe_cliente == "rural":
        classe_codigo = "B2"
    elif classe_cliente == "comercial":
        classe_codigo = "B3"

    return classe_codigo


#INPUTS IMPORTANTES
disjuntor_geral = projeto.disjuntor_geral_amperes
print( type(disjuntor_geral))
print( disjuntor_geral)
breakpoint()

def escreve_texto_unifilar():
    pass
#transferir para um fazedor de texto.
disjuntor_geral = str(disjuntor_geral)
fornecimento = inputs['dados_cliente']['fornecimento']
tensao_local = inputs['dados_cliente']['tensao_residencia']

texto_disjuntorgeral_unifilar = f"DISJUNTOR\nMONOFÁSICO\n \n{disjuntor_geral} A - 220V" 
texto2_disjuntorgeral_unifilar = f"DISJUNTOR\nTRIFÁSICO\n \n{disjuntor_geral} A - 380/220V" 

#inicio da logica dos inversores e paineis
quantidade_inversor2 = 0
quantidade_inversor3 = 0

inversor_potencia = inputs['inversor']['potencia']
inversores_potencia = [f"{str(inversor_potencia)}"]
inversor_marca = inputs['inversor']['marca']
inversor_modelo = inputs['inversor']['modelo']
numero_fases = inputs['inversor']['numero_fases']
quantidade_inversor = inputs['dados_cliente']['quantidade_inversor']

multiplicador, inversor_tensao = numero_de_fases(numero_fases)
corrente_saida = corrente_saida_calc(inversor_potencia, multiplicador, inversor_tensao)

equacao3 = fr"$I_{{\mathrm{{AG}}}} = \frac{{\mathrm{{potencia\ nominal }}}}{{\mathrm{{Tensao\ nominal * {multiplicador}}}}} = \frac{{{inversor_potencia}}}{{{inversor_tensao * multiplicador}}} = {corrente_saida:.2f}\ A$"
cabo_inversor1, corrente_max_cabo1, disjuntor_protecao1 = disjuntor_protecao_inversores(corrente_saida)
inversor = f"{quantidade_inversor} " + "inversor" + f" {inversor_marca} {inversor_modelo}"
texto_disjuntor1_unifilar = f"DISJUNTOR\nMONOFÁSICO\n{disjuntor_protecao1} A - 220V"
texto2_disjuntor1_unifilar = f"DISJUNTOR\nTRIFÁSICO\n{disjuntor_protecao1} A - 380V"
inversor_diagrama = f"{quantidade_inversor}x " + f" {inversor_marca} \n {inversor_modelo}"
texto_inversor = [f"{inversor}"]
quantidade_stringsinversor1 = quantidade_string(inversor_potencia)
quantidade_total_string = quantidade_stringsinversor1*quantidade_inversor
texto_disjuntores_protecao = [f"{quantidade_inversor} disjuntor de {disjuntor_protecao1} A"]
texto_cabos = [f"{cabo_inversor1}"]
corrente_max_cabos = [f"{corrente_max_cabo1}"]
texto_corrente_saida = [f"{corrente_saida:.2f} A"]
inversores_tensao = [f"{inversor_tensao}"]
tensao_queda = (200 * 0.0173 * 10 * corrente_saida) / (inversor_tensao * cabo_inversor1)
texto_tensao_queda = [f"{tensao_queda:.2f} %"]  
inversor_total_unifilar = inversor_potencia * quantidade_inversor
if inputs['dados_cliente']['quantidade_inversor2'] not in [None, 0]: # not in [none,0] 
    inversor2_potencia = inputs['inversor2']['potencia']
    inversores_potencia.append(str(inversor2_potencia))
    inversor2_marca = inputs['inversor2']['marca']
    inversor2_modelo = inputs['inversor2']['modelo']
    quantidade_inversor2 = inputs['dados_cliente']['quantidade_inversor2']
    numero_fases2 = inputs['inversor2']['numero_fases']
    multiplicador2, inversor_tensao2 = numero_de_fases(numero_fases2)
    corrente_saida2 = corrente_saida_calc(inversor2_potencia, multiplicador2, inversor_tensao2)
    cabo_inversor2, corrente_max_cabo2, disjuntor_protecao2 = disjuntor_protecao_inversores(corrente_saida2)
    equacao3_2 = fr"$I_{{\mathrm{{AG}}}} = \frac{{\mathrm{{potencia\ nominal}}}}{{\mathrm{{Tensao\ nominal * {multiplicador2}}}}} = \frac{{{inversor2_potencia}}}{{{inversor_tensao2 * multiplicador2}}} = {corrente_saida2:.2f}\ A$"
    inversor2 = f"{quantidade_inversor2} " + "inversor" + f" {inversor2_marca} {inversor2_modelo}"
    texto_disjuntor2_unifilar = f"DISJUNTOR\nMONOFÁSICO\n{disjuntor_protecao2} A - 220V"
    texto2_disjuntor2_unifilar = f"DISJUNTOR\nTRIFÁSICO\n{disjuntor_protecao2} A - 380V"
    inversor2_diagrama = f"{quantidade_inversor2}x " + f" {inversor2_marca} \n {inversor2_modelo}"
    texto_inversor.append(f"{inversor2}")
    quantidade_total_string_inversor2 = quantidade_string(inversor2_potencia)
    quantidade_total_string += quantidade_total_string_inversor2
    texto_disjuntores_protecao.append(f"{quantidade_inversor2} disjuntor de {disjuntor_protecao2} A")   
    texto_cabos.append(f"{cabo_inversor2}")
    corrente_max_cabos.append(f"{corrente_max_cabo2}")
    texto_corrente_saida.append(f"{corrente_saida2:.2f} A")
    inversores_tensao.append(f"{inversor_tensao2}")
    tensao_queda2 = (200 * 0.0173 * 10 * corrente_saida2) / (inversor_tensao2 * cabo_inversor2)
    texto_tensao_queda.append(f"{tensao_queda2:.2f} %")
    inversor_total_unifilar += inversor2_potencia * quantidade_inversor2
if inputs['dados_cliente']['quantidade_inversor3'] not in [None, 0]:
    inversor3_potencia = inputs['inversor3']['potencia']
    inversores_potencia.append(str(inversor3_potencia))
    inversor3_marca = inputs['inversor3']['marca']
    inversor3_modelo = inputs['inversor3']['modelo']
    quantidade_inversor3 = inputs['dados_cliente']['quantidade_inversor3']
    numero_fases3 = inputs['inversor3']['numero_fases']
    multiplicador3, inversor_tensao3 = numero_de_fases(numero_fases3)
    corrente_saida3 = corrente_saida_calc(inversor3_potencia, multiplicador3, inversor_tensao3)
    cabo_inversor3, corrente_max_cabo3, disjuntor_protecao3 = disjuntor_protecao_inversores(corrente_saida3)
    equacao3_3 = fr"$I_{{\mathrm{{AG}}}} = \frac{{\mathrm{{potencia\ nominal}}}}{{\mathrm{{Tensao\ nominal * {multiplicador3}}}}} = \frac{{{inversor3_potencia}}}{{{inversor_tensao3 * multiplicador3}}} = {corrente_saida3:.2f}\ A$"
    inversor3 = f"{quantidade_inversor3} " + "inversor" + f" {inversor3_marca} {inversor3_modelo}"
    texto_disjuntor3_unifilar = f"DISJUNTOR\nMONOFÁSICO\n{disjuntor_protecao3} A - 220V"
    texto2_disjuntor3_unifilar = f"DISJUNTOR\nTRIFÁSICO\n{disjuntor_protecao3} A - 380V"
    inversor3_diagrama = f"{quantidade_inversor3}x " + f" {inversor3_marca} \n {inversor3_modelo}"
    texto_inversor.append(f"{inversor3}")
    quantidade_total_string_inversor3 = quantidade_string(inversor3_potencia)
    quantidade_total_string += quantidade_total_string_inversor3    
    texto_disjuntores_protecao.append(f"{quantidade_inversor3} disjuntor de {disjuntor_protecao3} A")
    texto_cabos.append(f"{cabo_inversor3}")
    corrente_max_cabos.append(f"{corrente_max_cabo3}")
    texto_corrente_saida.append(f"{corrente_saida3:.2f} A") 
    inversores_tensao.append(f"{inversor_tensao3}") 
    tensao_queda3 = (200 * 0.0173 * 10 * corrente_saida3) / (inversor_tensao3 * cabo_inversor3)
    texto_tensao_queda.append(f"{tensao_queda3:.2f} %")
    inversor_total_unifilar += inversor3_potencia * quantidade_inversor3


#DADOS DO PAINEL PRINCIPAL

marca_painel = inputs['painel']['marca']
modelo_painel = inputs['painel']['modelo']
potencia_painel = inputs['painel']['potencia']  
quantidade_painel1 = inputs['dados_cliente']['quantidade_painel']
quantidade_total_painel = quantidade_painel1
paineis = f"{quantidade_painel1}" + " módulos fotovoltaicos " + f"{marca_painel}  {modelo_painel}" + " de " + f"{potencia_painel}" + " Wp"
paineis_diagrama = f"{quantidade_painel1} x {marca_painel}" + f"\n{modelo_painel}" +  f" {potencia_painel}" + " Wp"
texto_paineis = [f"{paineis}"]
tipo_painel = f"{inputs['painel']['tipo']}"
texto_painel_tipo = f"{inputs['painel']['tipo']}" + " " + f"{inputs['painel']['potencia']}" + " Wp"
texto_potencia_individual_paineis = [f"{potencia_painel}"] 
tensao_individual_paineis = f"{inputs['painel']['vp']}"
texto_tensao_individual_paineis = [f"{tensao_individual_paineis}"] 
potencia_totalpainel = (potencia_painel*quantidade_painel1) / 1000
potencia_total_unifilar = potencia_painel * quantidade_painel1

#CONDICIONAL CASO ENTRE UM SEGUNDO PAINEL
if inputs['dados_cliente']['quantidade_painel2'] not in [None, 0]:
    quantidade_painel2 = inputs['dados_cliente']['quantidade_painel2']
    quantidade_total_painel += quantidade_painel2
    marca_painel2 = inputs['painel2']['marca']
    modelo_painel2 = inputs['painel2']['modelo']    
    potencia_painel2 = inputs['painel2']['potencia']
    paineis2 = f" {quantidade_painel2}" + " modulos fotovoltaicos " + f"{marca_painel2} {modelo_painel2}" + " de " + f"{potencia_painel2}" + " Wp"
    paineis_diagrama2 = f"{quantidade_painel2} x {marca_painel2}" + f"\n{modelo_painel2}" +  f" {potencia_painel2}" + " Wp"
    tipo_painel2 = f"{inputs['painel2']['tipo']}"
    texto_paineis.append(f"{paineis2}")
    texto_painel_tipo = f"{tipo_painel}" + " " + f"{potencia_painel}" + " Wp" + ", " + f"{tipo_painel2}" + " " + f"{potencia_painel2}" + " Wp"
    texto_potencia_individual_paineis.append(f"{potencia_painel2}")
    tensao_individual_paineis2 = f"{inputs['painel2']['vp']}"
    texto_tensao_individual_paineis.append(f"{tensao_individual_paineis2}")
    potencia_totalpainel += (potencia_painel2*quantidade_painel2)  / 1000 
    potencia_total_unifilar += (potencia_painel2*quantidade_painel2)
        
#CONDICIONAL CASO ENTRE UM TERCEIRO PAINEL
if inputs['dados_cliente']['quantidade_painel3'] not in [None, 0]:
    quantidade_painel3 = inputs['dados_cliente']['quantidade_painel3']
    quantidade_total_painel += quantidade_painel3
    marca_painel3 = inputs['painel3']['marca']
    modelo_painel3 = inputs['painel3']['modelo']
    potencia_painel3 = inputs['painel3']['potencia'] 
    paineis3 = f" {quantidade_painel3}" + " modulos fotovoltaicos " + f"{marca_painel3} {modelo_painel3}" + " de " + f"{potencia_painel3}" + " Wp" 
    paineis_diagrama3 =  f"{quantidade_painel3} x {marca_painel3}" + f"\n{modelo_painel3}" +  f" {potencia_painel3}" + " Wp"
    tipo_painel3 = f"{inputs['painel3']['tipo']}"
    texto_paineis.append(f"{paineis3}")    
    texto_painel_tipo = f"{tipo_painel}" + " " + f"{potencia_painel}" + " Wp" + ", " + f"{tipo_painel2}" + " " + f"{potencia_painel2}" + " Wp" + ", " + f"{tipo_painel3}" + " " + f"{potencia_painel3}" + " Wp"
    texto_potencia_individual_paineis.append(f"{potencia_painel3}")
    tensao_individual_paineis3 = f"{inputs['painel3']['vp']}"
    texto_tensao_individual_paineis.append(f"{tensao_individual_paineis3}")
    potencia_totalpainel += (potencia_painel3*quantidade_painel3) / 1000 
    potencia_total_unifilar += (potencia_painel3*quantidade_painel3)
#VALORES QUE RETORNAM PARA O TEXTO
       
texto_finalpaineis = ", ".join(texto_paineis) #.join() concatena as strings da variável.
texto_finalinversor = ", ".join(texto_inversor) #.join() concatena as strings da variável. 
texto_potencia_individual_paineis = ", ".join(texto_potencia_individual_paineis)
texto_tensao_individual_paineis = ", ".join(texto_tensao_individual_paineis)
texto_disjuntores_protecao = ", ".join(texto_disjuntores_protecao) 
inversores_tensao = ", ".join(inversores_tensao) #.join() concatena as strings da variável.
texto_tensao_queda = ", ".join(texto_tensao_queda) #.join() concatena as strings da variável.
#.join() concatena as strings da variável.

#LOGICA DOS INVERSORES  
#- inversor de 3kW até 7kw sempre vão ter duas entradas para string
#- inversor de 7.1kw até 16.9kw sempre vão ter 3 entradas para string
#- inversor de 17kw até 26.9kw sempre vão ter 4 entradas para string
#- inversor de 27kw até 40kw sempre vão ter 6 entradas para string

#LOGICA PARA O CALCULO DA DISPOSIÇÃO DOS ARRANJOS 
quantidade_sobra_painel = quantidade_total_painel % quantidade_total_string
placas_por_arranjo = quantidade_total_painel // quantidade_total_string 

if quantidade_total_painel % quantidade_total_string == 0:
    texto_disposicao = f"{quantidade_total_string} arranjos de {placas_por_arranjo} módulos, por arranjo"
elif quantidade_total_painel % quantidade_total_string != 0 and quantidade_sobra_painel >= (2 * placas_por_arranjo) :
    texto_disposicao = f"{(quantidade_total_string)-1} arranjos de {(placas_por_arranjo) +1 }  módulos e 1 arranjo de {(quantidade_sobra_painel) - (placas_por_arranjo) - 2} módulos"
elif quantidade_total_painel % quantidade_total_string != 0 and quantidade_sobra_painel < (2 * placas_por_arranjo) :
    texto_disposicao = f"{(quantidade_total_string)-1} arranjos de {placas_por_arranjo} módulos e 1 arranjo de {placas_por_arranjo + quantidade_sobra_painel} módulos"
    
    
potenciaefetiva = potencia_totalpainel * 0.745
energia_gerada = potenciaefetiva * 5.84 * 30   


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
#EQ.DEMANDA MEDIA
equacao = fr"$D_{{\mathrm{{media}}}} = \frac{{\mathrm{{Energia\ media}}}}{{N^{{\circ}}\,\mathrm{{de\ horas}}}} = \frac{{{consumo_energia}}}{{720}} = {resultado:.2f}\ kW$"
#EQ.FATOR DE CARGA
equacao2 = fr"$FC = \frac{{\mathrm{{Energia}}}}{{\mathrm{{Potencia \ instalada \ x \ 720h}}}} = \frac{{{consumo_energia}}}{{{carga_cliente} \ x  \ 720}} = {fatordecarga:.2f}\ kW$"
#EQ. DISJUNTOR PROTECAO INVERSOR

#EQ. DISJUNTOR PROTECAO INVERSOR 2
equacao3_1 = fr"$I_{{\mathrm{{AG}}}} = \frac{{\mathrm{{potencia\ nominal}}}}{{\mathrm{{Tensao\ nominal}}}} = \frac{{{inversor_potencia}}}{{{inversor_tensao}}} = {corrente_saida:.2f}\ A$"
