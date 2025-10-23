from pydantic import BaseModel, EmailStr

from src.utils.models import tensao_fase, classe_consumo, ramal_energia, tipo_inversor


class Cliente(BaseModel):
    id_cliente: int | None
    nome_cliente: str
    cpf: str 
    data_nascimento: str 
    razao_social: str | None
    nome_fantasia: str | None
    cnpj: str | None
    rg: str
    telefone_cliente: str
    email_cliente: EmailStr

class EnderecoCliente(BaseModel):
    logradouro_cliente: str
    numero_casa_cliente: str
    complemento_casa_cliente: str | None
    cep_cliente: str
    bairro_cliente: str
    cidade_cliente: str
    estado_cliente: str

class EnderecoObra(BaseModel):
    logradouro_obra: str
    numero_obra: str
    complemento_obra: str | None
    cep_obra: str
    bairro_obra: str
    cidade_obra: str
    estado_obra: str
    latitude_obra: float
    longitude_obra: float

class Inversor(BaseModel):
    id_inversor: int | None
    marca_inversor: str
    modelo_inversor: str
    potencia_inversor: float
    numero_fases: tensao_fase
    tipo_inversor: tipo_inversor
    numero_mppt: int | None #reservado para atualizações futuras

class Placa(BaseModel):
    id_placa: int | None
    marca_placa: str
    modelo_placa: str
    potencia_placa: float
    tipo_celula: str
    tensao_pico: float
    corrente_curtocircuito: float
    tensao_maxima_potencia: float
    corrente_maxima_potencia: float
    eficiencia_placa: float | None #reservado para atualizações futuras

class Projetista(BaseModel):
    id_projetista: int | None
    nome_projetista: str
    creci_projetista: str
    rubrica_projetista: str
    telefone_projetista: str
    email_projetista: EmailStr

class Procurador(BaseModel):
    id_procurador: int | None
    nome_procurador: str
    cpf_procurador: str 
    rg_procurador: str
    telefone_procurador: str
    email_procurador: EmailStr
    logradouro_procurador: str
    numero_casa_procurador: str
    complemento_procurador: str | None
    cep_procurador: str
    bairro_procurador: str
    cidade_procurador: str
    estado_procurador: str

"""
1- um projeto só pode ter um cliente
2- um projeto só pode ter um projetista
3- um projeto só pode ter um procurador
4- um projeto só pode ter um endereço de obra

5- um projeto pode ter vários tipos de inversores
6- um projeto pode ter vários tipos de placas

"""
#colocar o projeto como uma classe que seta os parametros do projeto. quantidade de inversores e placas
#e não como uma classe grande que engloba todas as outras
class Projeto(BaseModel):
    id_projeto: int | None
    
    numero_unidade_consumidora: str
    carga_instalada_kw: float
    disjuntor_geral_amperes: float
    energia_media_mensal_kwh: float
    classe_consumo:  classe_consumo #residencial, comercial, industrial, rural
    tipo_fornecimento: tensao_fase #monofasico, bifasico, trifasico
    ramal_energia: ramal_energia #aéreo, subterrâneo
    data_projeto: str
    #quantidades de placas e inversores, por enquanto definidas pelo json de entrada.
    quantidade_placas: int
    quantidade_inversores: int
    quantidade_placas2: int | None
    quantidade_inversores2: int | None
    quantidade_placas3: int | None
    quantidade_inversores3: int | None

    cliente: Cliente
    endereco_cliente: EnderecoCliente
    endereco_obra: EnderecoObra
    inversor: Inversor
    placa: Placa
    projetista: Projetista
    procurador: Procurador

