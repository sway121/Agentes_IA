"""Herramientas para generar links de pago y gestionar pedidos."""

import json
import re
import uuid
from datetime import datetime
from typing import Dict, List, Optional
from agno.tools import tool


@tool
def generar_link_pago(
    order_id: str, 
    total: float, 
    datos_envio: Optional[Dict] = None,
    items: Optional[List[Dict]] = None
) -> str:
    """
    Genera un link de pago simulado para un pedido.
    
    ⚠️ IMPORTANTE: Esta función DEBE ser llamada DESPUÉS de:
    1. calcular_total_pedido() - para obtener el total
    2. validar_datos_envio() - para obtener los datos de envío validados
    
    Los datos de envío son OBLIGATORIOS antes de generar el link de pago.
    
    Args:
        order_id: ID único del pedido (obtenido con crear_order_id())
        total: Monto total del pedido (obtenido del resultado de calcular_total_pedido(), usar el campo "total")
        datos_envio: Datos de envío validados (obtenidos del resultado de validar_datos_envio())
                     Debe ser un diccionario con: nombre_completo, direccion, ciudad, codigo_postal, telefono, email
        items: (Opcional) Lista de items del pedido. Si no se proporciona, se usa una lista vacía.
               Formato: [{"id": int, "nombre": str, "cantidad": int, "precio": float}, ...]
    
    Returns:
        Información del link de pago en formato JSON con el link de pago incluido.
        El campo "payment_link" contiene el link correcto que DEBES usar exactamente como está.
        NO modifiques, inventes o cambies el link. Usa exactamente el valor de "payment_link".
    
    ⚠️ IMPORTANTE SOBRE EL LINK:
    - El link siempre será: http://localhost:7777/payment/{order_id}
    - NO agregues https://, NO cambies el dominio, NO agregues caracteres extra
    - Usa EXACTAMENTE el link que devuelve esta función en el campo "payment_link"
    - NO inventes otros links como "pagos.tienda.com" o similares
    
    Ejemplo de uso:
        1. Llama crear_order_id() para obtener un order_id
        2. Llama calcular_total_pedido(items) para obtener el total
        3. Solicita y valida los datos de envío con validar_datos_envio()
        4. Finalmente llama generar_link_pago(order_id, total, datos_envio, items)
        5. Usa EXACTAMENTE el campo "payment_link" del resultado
    """
    # Validar y limpiar order_id primero
    if not order_id or not isinstance(order_id, str):
        return json.dumps({
            "error": "order_id inválido",
            "mensaje": "El order_id debe ser un string válido"
        }, indent=2, ensure_ascii=False)
    
    # Limpiar order_id de caracteres extra (espacios, guiones adicionales, etc.)
    order_id = order_id.strip()
    # Remover cualquier caracter que no sea alfanumérico o guión
    order_id = re.sub(r'[^A-Za-z0-9\-]', '', order_id)
    
    # Si items no se proporciona, usar lista vacía
    if items is None:
        items = []
    
    # Validar que datos_envio esté presente
    if not datos_envio:
        return json.dumps({
            "error": "Los datos de envío son requeridos. Debes llamar validar_datos_envio() primero.",
            "mensaje": "No se puede generar el link de pago sin datos de envío validados",
            "instrucciones": "1. Solicita los datos de envío al cliente (nombre, dirección, ciudad, código postal, teléfono, email). 2. Llama validar_datos_envio() con esos datos. 3. Luego llama generar_link_pago() con el resultado."
        }, indent=2, ensure_ascii=False)
    
    # Si datos_envio es un string JSON, parsearlo
    if isinstance(datos_envio, str):
        try:
            datos_envio = json.loads(datos_envio)
        except json.JSONDecodeError:
            return json.dumps({
                "error": "El formato de datos_envio no es válido. Debe ser un diccionario o JSON válido.",
                "mensaje": "Asegúrate de pasar el resultado de validar_datos_envio() correctamente"
            }, indent=2, ensure_ascii=False)
    
    # Validar que sea un diccionario
    if not isinstance(datos_envio, dict):
        return json.dumps({
            "error": "datos_envio debe ser un diccionario. Usa el resultado de validar_datos_envio().",
            "mensaje": "El resultado de validar_datos_envio() es un JSON que debes parsear o pasar directamente"
        }, indent=2, ensure_ascii=False)
    
    # Validar que tenga los campos requeridos
    campos_requeridos = ["nombre_completo", "direccion", "ciudad", "codigo_postal", "telefono"]
    campos_faltantes = [campo for campo in campos_requeridos if campo not in datos_envio]
    if campos_faltantes:
        return json.dumps({
            "error": f"Faltan campos requeridos en datos_envio: {', '.join(campos_faltantes)}",
            "mensaje": "Asegúrate de que validar_datos_envio() haya validado correctamente todos los datos"
        }, indent=2, ensure_ascii=False)
    
    # Generar link de pago - SIEMPRE usar este formato exacto
    # Obtener configuración del servidor
    try:
        from config.settings import HOST, PORT
        # Si HOST es 0.0.0.0, usar localhost para el link
        if HOST == "0.0.0.0":
            host_for_link = "localhost"
        else:
            host_for_link = HOST
        payment_link = f"http://{host_for_link}:{PORT}/payment/{order_id}"
    except Exception:
        # Fallback a localhost:7777 si no se puede obtener la configuración
        payment_link = f"http://localhost:7777/payment/{order_id}"
    
    # Crear resumen del pedido
    resumen = {
        "order_id": order_id,
        "fecha": datetime.now().isoformat(),
        "total": total,
        "items": items,
        "datos_envio": datos_envio,
        "payment_link": payment_link,  # ⚠️ USA EXACTAMENTE ESTE LINK - NO LO MODIFIQUES
        "estado": "pendiente_pago",
        "mensaje": f"Pedido generado exitosamente. Total: ${total:.2f}",
        "⚠️ INSTRUCCIONES CRÍTICAS": {
            "link_de_pago": f"El link de pago es: {payment_link}",
            "uso_obligatorio": "DEBES usar EXACTAMENTE este link sin modificaciones",
            "no_inventar": "NO inventes otros links como 'pagos.tienda.com' o cualquier otro dominio",
            "no_modificar": "NO agregues sufijos al order_id (como '-MNO', '-XYZ', etc.)",
            "copiar_pegar": "Copia y pega EXACTAMENTE el valor del campo 'payment_link'",
            "formato_correcto": f"El link correcto es: {payment_link}"
        }
    }
    
    # Almacenar el pedido en un módulo compartido para que la API pueda acceder
    try:
        from api.routes import almacenar_pedido
        almacenar_pedido(resumen)
    except Exception as e:
        # Si falla, no es crítico pero lo registramos
        print(f"Warning: No se pudo almacenar el pedido: {e}")
    
    return json.dumps(resumen, indent=2, ensure_ascii=False)


@tool
def calcular_total_pedido(items: Optional[List[Dict]] = None) -> str:
    """
    Calcula el total de un pedido basado en los items. DEBE ser llamada antes de generar_link_pago().
    
    ⚠️ IMPORTANTE: Esta función REQUIERE una lista de items. NO la llames sin el parámetro items.
    
    Cada item debe tener:
    - id: ID del producto (número)
    - nombre: Nombre del producto (texto)
    - cantidad: Cantidad deseada (número, por defecto 1)
    - precio: Precio unitario del producto (número decimal)
    
    Args:
        items: Lista de items del pedido. Formato requerido:
               [{"id": int, "nombre": str, "cantidad": int, "precio": float}, ...]
               Ejemplo: [{"id": 1, "nombre": "Laptop Dell XPS 15", "cantidad": 1, "precio": 1299.99}]
    
    Returns:
        JSON con el resumen del pedido incluyendo:
        - items: Lista detallada de items con subtotales
        - subtotal: Suma de todos los items sin impuestos
        - impuestos: IVA del 21%
        - total: Total final con impuestos incluidos
        - cantidad_items: Número de items en el pedido
    
    Ejemplo de respuesta:
        {
          "items": [...],
          "subtotal": 1399.98,
          "impuestos": 293.99,
          "total": 1693.97,
          "cantidad_items": 2
        }
    
    ⚠️ ERROR COMÚN: Si recibes un error "Missing required argument items", significa que no pasaste la lista de items.
    Asegúrate de construir la lista primero antes de llamar esta función.
    """
    if items is None or not items:
        return json.dumps({
            "error": "La lista de items es requerida. Debes pasar una lista de productos con id, nombre, cantidad y precio.",
            "ejemplo": [
                {"id": 1, "nombre": "Laptop Dell XPS 15", "cantidad": 1, "precio": 1299.99}
            ]
        }, indent=2, ensure_ascii=False)
    
    total = 0.0
    items_detalle = []
    
    for item in items:
        cantidad = item.get("cantidad", 1)
        precio = item.get("precio", 0.0)
        subtotal = cantidad * precio
        total += subtotal
        
        items_detalle.append({
            "id": item.get("id"),
            "nombre": item.get("nombre"),
            "cantidad": cantidad,
            "precio_unitario": precio,
            "subtotal": subtotal
        })
    
    resumen = {
        "items": items_detalle,
        "subtotal": total,
        "impuestos": round(total * 0.21, 2),  # IVA 21%
        "total": round(total * 1.21, 2),
        "cantidad_items": len(items)
    }
    
    return json.dumps(resumen, indent=2, ensure_ascii=False)


@tool
def crear_order_id() -> str:
    """
    Genera un ID único para un nuevo pedido.
    
    Returns:
        ID único del pedido
    """
    return f"ORD-{uuid.uuid4().hex[:8].upper()}"


@tool
def validar_datos_envio(
    nombre_completo: str,
    direccion: str,
    ciudad: str,
    codigo_postal: str,
    telefono: str,
    email: Optional[str] = None
) -> str:
    """
    Valida y almacena los datos de envío del cliente.
    
    ⚠️ IMPORTANTE: Esta función DEBE ser llamada ANTES de generar_link_pago().
    Los datos de envío son obligatorios para procesar el pedido.
    
    Args:
        nombre_completo: Nombre completo del cliente (requerido)
        direccion: Dirección de envío completa (requerido)
        ciudad: Ciudad de envío (requerido)
        codigo_postal: Código postal (requerido)
        telefono: Número de teléfono de contacto (requerido)
        email: Email del cliente (opcional)
    
    Returns:
        JSON con confirmación de los datos de envío validados
    
    Ejemplo:
        validar_datos_envio(
            nombre_completo="Juan Pérez",
            direccion="Av. Corrientes 1234",
            ciudad="Buenos Aires",
            codigo_postal="C1043AAX",
            telefono="+54 11 1234-5678",
            email="juan@example.com"
        )
    """
    # Validar que los campos requeridos no estén vacíos
    if not nombre_completo or not nombre_completo.strip():
        return json.dumps({
            "error": "El nombre completo es requerido",
            "valido": False
        }, indent=2, ensure_ascii=False)
    
    if not direccion or not direccion.strip():
        return json.dumps({
            "error": "La dirección es requerida",
            "valido": False
        }, indent=2, ensure_ascii=False)
    
    if not ciudad or not ciudad.strip():
        return json.dumps({
            "error": "La ciudad es requerida",
            "valido": False
        }, indent=2, ensure_ascii=False)
    
    if not codigo_postal or not codigo_postal.strip():
        return json.dumps({
            "error": "El código postal es requerido",
            "valido": False
        }, indent=2, ensure_ascii=False)
    
    if not telefono or not telefono.strip():
        return json.dumps({
            "error": "El teléfono es requerido",
            "valido": False
        }, indent=2, ensure_ascii=False)
    
    # Crear objeto con los datos de envío
    datos_envio = {
        "nombre_completo": nombre_completo.strip(),
        "direccion": direccion.strip(),
        "ciudad": ciudad.strip(),
        "codigo_postal": codigo_postal.strip(),
        "telefono": telefono.strip(),
        "email": email.strip() if email else None,
        "valido": True,
        "mensaje": "Datos de envío validados correctamente"
    }
    
    return json.dumps(datos_envio, indent=2, ensure_ascii=False)


