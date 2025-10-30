from src.utils.factoryobject import projeto
from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale
import pprint
#dados importantes para os calculos
carga_cliente = projeto.carga_instalada_kw * 1000
consumo_energia = projeto.energia_media_mensal_kwh
classeconsumo = projeto.classe_consumo

resultado = consumo_energia / 720
fatordecarga = resultado / carga_cliente

class objetos_calculados:
    def __init__(self):
        @property
        def quantidade_total_placas(self):
            self.quantidade_final_placas = 0
            for quantidade_sistemas in range(projeto.quantidade_sistemas_instalados):
                recebe = self.conta_placa_do_sistema(quantidade_sistemas)
                self.quantidade_final_placas += recebe

            return self.quantidade_final_placas
        pass
    
    @property
    def data_de_hoje(self):
        data_de_hoje = datetime.now()
        # data_futura = data_de_hoje+relativedelta(months=1)
        # locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
        # plt.rcParams['text.usetex'] = True # Ativar o uso do LaTeX real (MikTeX)
        return data_de_hoje
    
    @property
    def data_futura(data_de_hoje):
        data_futura = data_de_hoje+relativedelta(months=1)
        return data_futura
    
    @property
    def calculo_demanda(self):
        resultado = projeto.energia_media_mensal_kwh / 720
        equacao = fr"$D_{{\mathrm{{media}}}} = \frac{{\mathrm{{Energia\ media}}}}{{N^{{\circ}}\,\mathrm{{de\ horas}}}} = \frac{{{projeto.energia_media_mensal_kwh}}}{{720}} = {resultado:.2f}\ kW$"
        return equacao
    
    @property
    def calculo_fator_de_carga(self):
        fatordecarga = (projeto.energia_media_mensal_kwh / 720) / projeto.carga_instalada_kw
        equacao2 = fr"$FC = \frac{{\mathrm{{Energia}}}}{{\mathrm{{Potencia \ instalada \ x \ 720h}}}} = \frac{{{projeto.energia_media_mensal_kwh}}}{{{projeto.carga_instalada_kw} \ x  \ 720}} = {fatordecarga:.2f}\ kW$"
        return equacao2
    
    #conta a quantidade de placas do sistema em absoluto
    def conta_placa_do_sistema(self):
        sistema_instalado = projeto.sistema_instalado
        quantidade_final = []
        for i,objetos in enumerate(sistema_instalado):
            quantidade_placas_lista = list(projeto.sistema_instalado[i].quantidade_total_placas_do_sistema.values())
            quantidade_placas_diferentes = [placa for placa in quantidade_placas_lista if placa not in [None]]
            
            modelo = projeto.sistema_instalado[i].placa.modelo_placa
            marca = projeto.sistema_instalado[i].placa.marca_placa
            potencia = projeto.sistema_instalado[i].placa.potencia_placa
            #monta a lista     
            
            quantidade_ = [[modelo, marca, potencia,placa] for placa in quantidade_placas_diferentes]
            quantidade_final.append(quantidade_)

        return quantidade_final
        #retorna uma lista com uma lista para cada sistema instalado
objeto = objetos_calculados()
resultado = objeto.conta_placa_do_sistema()
print(resultado)

breakpoint()



#calcula a distribuição das placas no inversor
def distribui_placa_por_inversor(self,quantidade_sistemas):
    numero_strings = projeto.sistema_instalado[quantidade_sistemas].inversor.numero_mppt
    numero_de_inversores = projeto.sistema_instalado[quantidade_sistemas].quantidade_inversor
    
    numero_de_paineis = self.conta_placa_do_sistema(quantidade_sistemas)
    
    lista_string = []

    resto_placas_por_string = numero_de_paineis % numero_strings
    placas_por_string = numero_de_paineis // numero_strings
    for numero_mppt in range(numero_strings):
        lista_string.append(placas_por_string)
    if resto_placas_por_string != 0:
        lista_string[-1] += resto_placas_por_string
    return lista_string

#aqui iteramos sobre cada sistema instalado
@property
def calculo_disposicao_placas(self):
    quantidade_final_de_placas_por_inversor = []
    
    for quantidade_sistemas in range(projeto.quantidade_sistemas_instalados):
        quantidade_de_placas_por_inversor = self.distribui_placa_por_inversor(quantidade_sistemas)
        quantidade_final_de_placas_por_inversor.append(quantidade_de_placas_por_inversor)
    #retornamos a quantidade final de placas caso tenha mais de um sistema instalado.
    return quantidade_final_de_placas_por_inversor




breakpoint()


@property
def calculo_potencia_efetiva(self):
    self.quantidade
    pass




def calculo_protecao_inversor():
    pass

def calculo_queda_tensao():
    pass






def get_classe_codigo(classe_cliente: str) -> str:
    classe_codigo = ""
    if classe_cliente == "residencial":
        classe_codigo = "B1"
    elif classe_cliente == "rural":
        classe_codigo = "B2"
    elif classe_cliente == "comercial":
        classe_codigo = "B3"

    return classe_codigo


def escreve_texto_unifilar():
    pass

def escreve_texto_memorial():
    pass



#transferir para um fazedor de texto.

texto_disjuntorgeral_unifilar = f"DISJUNTOR\nMONOFÁSICO\n \n{projeto.disjuntor_geral} A - 220V" 
texto2_disjuntorgeral_unifilar = f"DISJUNTOR\nTRIFÁSICO\n \n{projeto.disjuntor_geral} A - 380/220V" 


equacao3 = fr"$I_{{\mathrm{{AG}}}} = \frac{{\mathrm{{potencia\ nominal }}}}{{\mathrm{{Tensao\ nominal * {multiplicador}}}}} = \frac{{{projeto.inversor_potencia}}}{{{inversor_tensao * multiplicador}}} = {corrente_saida:.2f}\ A$"


#calculos para memorial

quantidade_total_string = quantidade_stringsinversor1*quantidade_inversor

#texto inversores memorial
inversor = f"{quantidade_inversor} " + "inversor" + f" {inversor_marca} {inversor_modelo}"


#calculos de quantidade de strings para memorial

texto_disjuntores_protecao = [f"{quantidade_inversor} disjuntor de {disjuntor_protecao1} A"]
texto_cabos = [f"{cabo_inversor1}"]
corrente_max_cabos = [f"{corrente_max_cabo1}"]
texto_corrente_saida = [f"{corrente_saida:.2f} A"]
inversores_tensao = [f"{inversor_tensao}"]
tensao_queda = (200 * 0.0173 * 10 * corrente_saida) / (inversor_tensao * cabo_inversor1)
texto_tensao_queda = [f"{tensao_queda:.2f} %"]  

inversor_total_unifilar = inversor_potencia * quantidade_inversor

#texto disjuntor unifilar
texto_disjuntor1_unifilar = f"DISJUNTOR\nMONOFÁSICO\n{disjuntor_protecao1} A - 220V"
texto2_disjuntor1_unifilar = f"DISJUNTOR\nTRIFÁSICO\n{disjuntor_protecao1} A - 380V"

#texto inversor diagrama unifilar
inversor_diagrama = f"{quantidade_inversor}x " + f" {inversor_marca} \n {inversor_modelo}"


#DADOS DO PAINEL PRINCIPAL



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

        
#CONDICIONAL CASO ENTRE UM TERCEIRO PAINEL

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

#EQ. DISJUNTOR PROTECAO INVERSOR

#EQ. DISJUNTOR PROTECAO INVERSOR 2
equacao3_1 = fr"$I_{{\mathrm{{AG}}}} = \frac{{\mathrm{{potencia\ nominal}}}}{{\mathrm{{Tensao\ nominal}}}} = \frac{{{inversor_potencia}}}{{{inversor_tensao}}} = {corrente_saida:.2f}\ A$"


#EQ. QUEDA DE TENSÃO
equacao4 = fr"$\Delta V \% = \frac{{200*\rho*L_c*I_c*cos\varphi}}{{S_c*V_f}}$"