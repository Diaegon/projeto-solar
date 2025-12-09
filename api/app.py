from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
 
from io import BytesIO

from src.buildingdocuments.memorialdescritivo import MemorialDescritivo
from src.factorys.datas.createobject import ProjectFactory
from src.schemas.schemas import Cliente, EnderecoCliente, EnderecoObra, Projeto, ProjetoTeste, ConfiguracaoSistema
from src.factorys.datas.documentbuilder import ObjetosCalculados
from src.config import INPUTS_DIR
import json 



def gerar_documentos():

    file2 = INPUTS_DIR / "input_necessario.json"
    inputs_projeto = json.loads(file2.read_text(encoding="utf-8"))

    projeto = ProjectFactory.factory(inputs=None, inputs_projeto=inputs_projeto)
    retorno = ObjetosCalculados(projeto).construtor_dados_memorial()
    return retorno

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/input")
def post_data(projeto: ProjetoTeste, sistema_instalado: ConfiguracaoSistema):
    projeto_retorno = ProjectFactory.factory(inputs=None, inputs_projeto=projeto.dict(),
                                              config_sistema=sistema_instalado.dict())
    retorno = ObjetosCalculados(projeto_retorno).construtor_dados_memorial()
    
    pdf = MemorialDescritivo(retorno)
    pdf.gerar_memorial()

    buffer = BytesIO(pdf.to_bytes())

    return StreamingResponse(
        buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=memorial.pdf"}
    )


@app.get("/pdf-memorial")
def get_pdf_memorial(
    
):
    pdf_path = "output/diagrama.pdf"
    
    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename="resultado.pdf"
    )

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

