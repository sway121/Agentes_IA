"""Endpoints adicionales de la API para el sistema de ventas."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
import json

router = APIRouter(prefix="/api", tags=["sales"])

# Almacenamiento en memoria de pedidos (en producción usar base de datos)
_pedidos_almacenados: Dict[str, Dict[str, Any]] = {}


def almacenar_pedido(pedido: Dict[str, Any]) -> None:
    """
    Almacena un pedido en memoria.
    Función auxiliar para que las tools puedan almacenar pedidos.
    """
    order_id = pedido.get("order_id")
    if order_id:
        _pedidos_almacenados[order_id] = pedido


class ChatMessage(BaseModel):
    """Modelo para mensajes del chat."""
    message: str
    session_id: Optional[str] = None


class ChatResponse(BaseModel):
    """Modelo para respuestas del chat."""
    response: str
    session_id: str


@router.get("/health")
async def health_check():
    """Endpoint de salud del sistema."""
    return {
        "status": "healthy",
        "service": "Sistema de Ventas Multi-Agente",
        "version": "1.0.0"
    }


@router.get("/products")
async def get_products():
    """Obtiene todos los productos disponibles."""
    from pathlib import Path
    import json
    
    products_file = Path(__file__).parent.parent / "data" / "products.json"
    
    try:
        with open(products_file, "r", encoding="utf-8") as f:
            products = json.load(f)
        return {"products": products}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Catálogo de productos no encontrado")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error al leer el catálogo de productos")


@router.get("/products/{product_id}")
async def get_product(product_id: int):
    """Obtiene un producto específico por ID."""
    from pathlib import Path
    import json
    
    products_file = Path(__file__).parent.parent / "data" / "products.json"
    
    try:
        with open(products_file, "r", encoding="utf-8") as f:
            products = json.load(f)
        
        for product in products:
            if product.get("id") == product_id:
                return {"product": product}
        
        raise HTTPException(status_code=404, detail=f"Producto con ID {product_id} no encontrado")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Catálogo de productos no encontrado")


@router.get("/order/{order_id}")
async def get_order_info(order_id: str):
    """
    Obtiene información de un pedido.
    Busca el pedido en el almacenamiento en memoria.
    """
    # Buscar el pedido en el almacenamiento
    if order_id in _pedidos_almacenados:
        return _pedidos_almacenados[order_id]
    
    # Si no se encuentra, retornar información básica
    raise HTTPException(status_code=404, detail=f"Pedido {order_id} no encontrado")


@router.post("/order")
async def crear_pedido(pedido: Dict[str, Any]):
    """
    Almacena un pedido en memoria.
    Esta función es llamada internamente cuando se genera un pedido.
    """
    order_id = pedido.get("order_id")
    if order_id:
        _pedidos_almacenados[order_id] = pedido
        return {"status": "ok", "order_id": order_id}
    raise HTTPException(status_code=400, detail="order_id es requerido")


