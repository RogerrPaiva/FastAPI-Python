from fastapi import APIRouter, HTTPException
from app.modelos.cliente import Cliente

CLIENTE_LIST = [
    Cliente(id=1, nome="Roger", email="rogerpaiva1801@gmail.com",
            telefone="53991613398"),
    Cliente(id=2, nome="rafael", email="rad@dsad.com", telefone="1213213123")
]

router = APIRouter(prefix="/clientes")


@router.get("/", response_model=list[Cliente])
async def listar_clientes():
    return CLIENTE_LIST


@router.get("/{cliente_id}", response_model=Cliente | None)
async def obter_cliente(cliente_id: int):
    for cliente in CLIENTE_LIST:
        if cliente.id == cliente_id:
            return cliente

    raise HTTPException(status_code=404, detail="Cliente não encontrado")
