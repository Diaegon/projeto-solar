from src.schemas.schemas import (Projeto, Cliente, EnderecoCliente, EnderecoObra,
Inversor, Placa, Projetista, Procurador, ConfiguracaoSistema)

#criação das classes de sistema isntalado
class SistemaInstaladoFactory:
    @staticmethod
    def instanciar_sistema_instalado_do_json(inputs: dict, a: int) -> ConfiguracaoSistema:
        dados_sistema = inputs[f'sistema_instalado{a}']
        qtd_total_placas = dados_sistema['quantidade_total_placas_do_sistema']
        #o (a) é o número do sistema instalado no json de entrada.
        # Monta o dicionário de dados
        dados = {
            'inversor': Inversor(**dados_sistema['inversor']),
            'quantidade_inversor': dados_sistema['quantidade_inversor'],
            'placa': Placa(**dados_sistema['placa']),
            'quantidade_placas': qtd_total_placas['quantidade_placas'],
            'quantidade_total_placas_do_sistema': qtd_total_placas
        }
        
        # Adiciona placa2 se existir
        if qtd_total_placas.get('quantidade_placas2'):
            dados['placa2'] = Placa(**dados_sistema['placa2'])
            dados['quantidade_placas2'] = qtd_total_placas.get('quantidade_placas2')
        
        return ConfiguracaoSistema(**dados)
    
    @staticmethod
    def build_sistema_instalado_list(inputs: dict) -> list[ConfiguracaoSistema]:
        sistemas = []
        for i in range(1, inputs['projeto']['quantidade_sistemas_instalados'] + 1):
            sistema = SistemaInstaladoFactory.instanciar_sistema_instalado_do_json(inputs, i)
            sistemas.append(sistema)
        return sistemas

#Criação da classe final dos dados iniciais do projeto. 
class ProjectFactory:

    @staticmethod
    def factory(inputs: dict) -> Projeto:
        sistema_instalado = SistemaInstaladoFactory.build_sistema_instalado_list(inputs)
        cliente = Cliente(**inputs['cliente'])
        endereco_cliente = EnderecoCliente(**inputs['endereco_cliente'])
        endereco_obra = EnderecoObra(**inputs['endereco_obra'])
        projetista = Projetista(**inputs['projetista'])
        procurador = Procurador(**inputs['dados_procurador'])

        return Projeto(
            **inputs["projeto"],
            cliente=cliente,
            endereco_cliente=endereco_cliente,
            endereco_obra=endereco_obra,
            projetista=projetista,
            procurador=procurador,
            sistema_instalado=sistema_instalado
        )

if __name__ == "__main__":
    import json
    from src.config import INPUTS_DIR

    file = INPUTS_DIR / "input_solar.json"
    inputs = json.loads(file.read_text(encoding="utf-8"))

    projeto = ProjectFactory.factory(inputs)