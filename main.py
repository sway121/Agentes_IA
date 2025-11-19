"""Punto de entrada principal del sistema de ventas multi-agente."""

import os
from agno.team import Team
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat
from agno.os import AgentOS
from fastapi.responses import FileResponse
from fastapi import Request
from config.settings import MODEL_ID, OPENAI_API_KEY, DB_FILE, HOST, PORT
from agents.sales_agent import create_sales_agent
from agents.product_agent import create_product_agent
from agents.order_agent import create_order_agent
from api.routes import router as api_router


def create_sales_team() -> Team:
    """
    Crea el team de agentes de ventas.
    
    Returns:
        Team configurado con todos los agentes
    """
    # Crear instancia de base de datos compartida
    db = SqliteDb(db_file=DB_FILE)
    
    # Crear agentes
    sales_agent = create_sales_agent(db)
    product_agent = create_product_agent(db)
    order_agent = create_order_agent(db)
    
    # Crear team con SalesAgent como líder
    team = Team(
        name="SalesTeam",
        members=[
            sales_agent,
            product_agent,
            order_agent,
        ],
        model=OpenAIChat(id=MODEL_ID, api_key=OPENAI_API_KEY),
        db=db,
        instructions="""Eres el coordinador principal del equipo de ventas. Tu función es gestionar todo el proceso de ventas desde el inicio hasta la finalización:

1. **Inicio de conversación**: Saluda al cliente y pregunta en qué puedes ayudarle.

2. **Consulta de productos**: Cuando el cliente busca productos, delega al ProductAgent para buscar y presentar opciones. El ProductAgent tiene acceso a herramientas para consultar el catálogo completo de productos.

3. **Presentación y selección**: Presenta los productos encontrados de manera atractiva. Cuando el cliente selecciona un producto, confirma la selección y pregunta si desea agregar algo más.

4. **Iteración**: Repite el proceso de consulta y selección hasta que el cliente indique claramente que no quiere más productos (puede decir "no quiero más", "eso es todo", "nada más", "listo", etc.).

5. **Armado del pedido**: Cuando el cliente termine de seleccionar productos, delega al OrderAgent para que:
   - Arme el pedido final con todos los productos seleccionados
   - Calcule el total correctamente (incluyendo impuestos)
   - Solicite y valide los datos de envío del cliente (nombre, dirección, ciudad, código postal, teléfono, email)
   - Genere un link de pago único (solo después de tener los datos de envío)

6. **Finalización**: Presenta el resumen completo del pedido y el link de pago de manera clara y profesional. Agradece al cliente y finaliza la conversación.

IMPORTANTE:
- Mantén un registro claro de todos los productos seleccionados durante la conversación
- Sé natural, amable y conversacional
- No presiones al cliente
- Confirma siempre las selecciones antes de continuar
- Cuando el cliente diga que no quiere más, procede inmediatamente a armar el pedido con el OrderAgent
- El OrderAgent tiene herramientas para calcular totales y generar links de pago""",
        add_history_to_context=True,
        markdown=True,
        description="Team de agentes especializados en ventas, productos y pedidos",
        debug_mode=True,
        debug_level=1,
    )
    
    return team


# Crear team de ventas y AgentOS a nivel de módulo
sales_team = create_sales_team()
agent_os = AgentOS(teams=[sales_team])

# Obtener app FastAPI
app = agent_os.get_app()

# Incluir router de API adicional
app.include_router(api_router)

@app.get("/payment/{order_id}")
async def payment_page(order_id: str, request: Request):
    """Sirve la página de pago simulada."""
    payment_file = os.path.join(os.path.dirname(__file__), "web", "payment.html")
    return FileResponse(payment_file)


def main():
    """Función principal que inicializa y ejecuta el sistema."""
    # Servir el sistema
    print(f"🚀 Sistema de Ventas Multi-Agente iniciado")
    print(f"📡 Servidor corriendo en http://{HOST}:{PORT}")
    print(f"🤖 Team de ventas listo para recibir consultas")
    print(f"💳 Página de pago disponible en http://{HOST}:{PORT}/payment/{{order_id}}")
    
    agent_os.serve(app="main:app", host=HOST, port=PORT, reload=False)


if __name__ == "__main__":
    main()

