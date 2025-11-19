"""Herramientas para consultar y gestionar productos."""

import json
from pathlib import Path
from typing import List, Dict, Optional
from agno.tools import tool

# Cargar productos desde JSON
PRODUCTS_FILE = Path(__file__).parent.parent / "data" / "products.json"


def _load_products() -> List[Dict]:
    """Carga el catálogo de productos desde el archivo JSON."""
    try:
        with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


@tool
def buscar_productos(query: str) -> str:
    """
    Busca productos en el catálogo por nombre, descripción o categoría.
    
    Args:
        query: Término de búsqueda (nombre, categoría, descripción)
    
    Returns:
        Lista de productos encontrados en formato JSON
    """
    products = _load_products()
    query_lower = query.lower()
    
    resultados = []
    for product in products:
        if (
            query_lower in product.get("name", "").lower()
            or query_lower in product.get("description", "").lower()
            or query_lower in product.get("category", "").lower()
        ):
            resultados.append(product)
    
    if not resultados:
        return json.dumps({"mensaje": f"No se encontraron productos para '{query}'", "productos": []})
    
    return json.dumps({"productos": resultados}, indent=2, ensure_ascii=False)


@tool
def obtener_todos_los_productos() -> str:
    """
    Obtiene todos los productos disponibles en el catálogo.
    
    Returns:
        Lista completa de productos en formato JSON
    """
    products = _load_products()
    return json.dumps({"productos": products}, indent=2, ensure_ascii=False)


@tool
def obtener_producto_por_id(product_id: int) -> str:
    """
    Obtiene los detalles de un producto específico por su ID.
    
    Args:
        product_id: ID del producto a buscar
    
    Returns:
        Detalles del producto en formato JSON o mensaje de error
    """
    products = _load_products()
    
    for product in products:
        if product.get("id") == product_id:
            return json.dumps(product, indent=2, ensure_ascii=False)
    
    return json.dumps({"error": f"Producto con ID {product_id} no encontrado"})


@tool
def verificar_stock(product_id: int, cantidad: int = 1) -> str:
    """
    Verifica si hay stock disponible para un producto.
    
    Args:
        product_id: ID del producto
        cantidad: Cantidad deseada (default: 1)
    
    Returns:
        Información de stock en formato JSON
    """
    products = _load_products()
    
    for product in products:
        if product.get("id") == product_id:
            stock_disponible = product.get("stock", 0)
            disponible = stock_disponible >= cantidad
            
            return json.dumps({
                "producto_id": product_id,
                "producto_nombre": product.get("name"),
                "stock_disponible": stock_disponible,
                "cantidad_solicitada": cantidad,
                "disponible": disponible,
                "mensaje": f"Stock disponible: {stock_disponible} unidades" if disponible else f"Stock insuficiente. Disponible: {stock_disponible} unidades"
            }, indent=2, ensure_ascii=False)
    
    return json.dumps({"error": f"Producto con ID {product_id} no encontrado"})


@tool
def obtener_productos_por_categoria(categoria: str) -> str:
    """
    Obtiene todos los productos de una categoría específica.
    
    Args:
        categoria: Nombre de la categoría
    
    Returns:
        Lista de productos de la categoría en formato JSON
    """
    products = _load_products()
    categoria_lower = categoria.lower()
    
    resultados = [
        product for product in products
        if categoria_lower in product.get("category", "").lower()
    ]
    
    if not resultados:
        return json.dumps({
            "mensaje": f"No se encontraron productos en la categoría '{categoria}'",
            "productos": []
        })
    
    return json.dumps({"categoria": categoria, "productos": resultados}, indent=2, ensure_ascii=False)


