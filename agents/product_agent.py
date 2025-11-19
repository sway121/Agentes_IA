"""Agente especializado en consultar y presentar productos."""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from config.settings import MODEL_ID, OPENAI_API_KEY, DB_FILE
from tools.product_tools import (
    buscar_productos,
    obtener_todos_los_productos,
    obtener_producto_por_id,
    verificar_stock,
    obtener_productos_por_categoria,
)


def create_product_agent(db: SqliteDb) -> Agent:
    """
    Crea el agente especializado en productos.
    
    Args:
        db: Instancia de base de datos SQLite
    
    Returns:
        Agente configurado para consultar productos
    """
    return Agent(
        name="ProductAgent",
        role="Eres un experto en productos. Tu función es ayudar a los clientes a encontrar productos que se ajusten a sus necesidades. Presenta los productos de manera clara, destacando características principales, precio y disponibilidad. Sé amable y proactivo en sugerir alternativas cuando sea apropiado.",
        model=OpenAIChat(id=MODEL_ID, api_key=OPENAI_API_KEY),
        db=db,
        tools=[
            buscar_productos,
            obtener_todos_los_productos,
            obtener_producto_por_id,
            verificar_stock,
            obtener_productos_por_categoria,
        ],
        add_history_to_context=True,
        markdown=True,
        description="Agente especializado en consultar y presentar productos del catálogo",
    )


