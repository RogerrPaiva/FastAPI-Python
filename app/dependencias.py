
from app.banco_de_dados.cliente_repositorio import ClienteRepositorio
from app.banco_de_dados.local import BancoDeDadosLocal

from fastapi import Depends
from typing import Annotated

banco_de_dados = BancoDeDadosLocal()


def obter_banco_de_dados():
    return banco_de_dados



def obter_cliente_repositorio(
    banco_de_dados_local: Annotated[
        BancoDeDadosLocal, Depends(obter_banco_de_dados)
    ]
) -> ClienteRepositorio:
    return ClienteRepositorio(banco_de_dados_local)