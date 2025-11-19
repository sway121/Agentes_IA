# 🛍️ Sistema de Ventas Multi-Agente con IA

> **Sistema inteligente de ventas asistido por agentes de IA** que gestiona automáticamente todo el proceso comercial: desde la consulta de productos hasta la generación del link de pago, utilizando un equipo coordinado de agentes especializados trabajando en conjunto.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Agno](https://img.shields.io/badge/Agno-2.0+-green.svg)](https://agno.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-teal.svg)](https://fastapi.tiangolo.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991.svg)](https://openai.com)
[![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey.svg)](https://www.sqlite.org/)
[![Next.js](https://img.shields.io/badge/Next.js-18-black.svg)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue.svg)](https://www.typescriptlang.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📖 ¿Qué es este proyecto?

Este proyecto es un **sistema de ventas inteligente** que utiliza múltiples agentes de inteligencia artificial trabajando en equipo para automatizar todo el proceso de ventas. Imagina tener un equipo de vendedores virtuales, cada uno especializado en una tarea específica:

- **Un coordinador de ventas** que gestiona la conversación
- **Un experto en productos** que conoce todo el catálogo
- **Un especialista en pedidos** que arma y procesa las órdenes

Todos estos agentes trabajan juntos de forma coordinada para brindar una experiencia de compra fluida y profesional, similar a tener un equipo de ventas humano, pero disponible 24/7 y con acceso instantáneo a toda la información.

### 🎯 ¿Para quién es útil?

- **Empresas de e-commerce** que quieren automatizar su atención al cliente
- **Desarrolladores** interesados en aprender sobre sistemas multi-agente
- **Emprendedores** que buscan integrar IA en sus procesos comerciales
- **Estudiantes** de inteligencia artificial y desarrollo de software

---

## ✨ Características Principales

### 🤖 Sistema Multi-Agente
- **3 agentes especializados** trabajando en coordinación
- **Delegación inteligente** de tareas entre agentes
- **Memoria persistente** de conversaciones en base de datos SQLite
- **Historial completo** de interacciones con el cliente

### 🛠️ Herramientas Personalizadas
- **Búsqueda de productos** por nombre, categoría o características
- **Cálculo automático** de totales e impuestos
- **Validación de datos** de envío del cliente
- **Generación de links** de pago únicos y seguros

### 💻 Interfaz Moderna
- **AgentUI**: Interfaz visual moderna con Next.js/TypeScript
- **Streaming en tiempo real** de respuestas
- **Visualización de herramientas** utilizadas por los agentes
- **Historial persistente** de conversaciones

### 🔌 API RESTful
- **Endpoints FastAPI** para integración con otros sistemas
- **Documentación automática** con Swagger/OpenAPI
- **Página de pago simulada** para demostración

---

## 🏗️ Arquitectura del Sistema

### Conceptos Clave (Explicación Simple)

#### ¿Qué es un Agente de IA?
Un agente de IA es como un asistente virtual especializado. Cada agente tiene:
- **Un rol específico**: sabe qué tarea debe realizar
- **Herramientas**: funciones que puede usar para completar su trabajo
- **Memoria**: recuerda las conversaciones anteriores
- **Capacidad de razonamiento**: puede tomar decisiones basadas en el contexto

#### ¿Qué es un Team (Equipo)?
Un team es un grupo de agentes que trabajan juntos. Tiene un **líder coordinador** que decide qué agente debe realizar cada tarea. Es como un equipo de trabajo donde cada miembro tiene su especialidad, pero todos colaboran para alcanzar un objetivo común.

#### ¿Qué es AgentOS?
AgentOS es el "sistema operativo" que gestiona todos los agentes. Se encarga de:
- Coordinar las comunicaciones entre agentes
- Gestionar la base de datos y el historial
- Proporcionar una API para interactuar con el sistema
- Ejecutar las herramientas cuando los agentes las necesitan

### Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                      Cliente/Usuario                        │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                    AgentUI (Frontend)                       │
│              Interfaz visual Next.js/TypeScript             │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                    AgentOS (Backend)                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              SalesTeam (Team Coordinador)            │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌───────────┐   │   │
│  │  │ SalesAgent   │  │ ProductAgent │  │OrderAgent │   │   │
│  │  │ (Coordinador)│  │ (Productos)  │  │ (Pedidos) │   │   │
│  │  └──────┬───────┘  └──────┬───────┘  └─────┬─────┘   │   │
│  └─────────┼──────────────────┼────────────────┼───────-┘   │
│            │                  │                │            │
│            ▼                  ▼                ▼            │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Herramientas (Tools)                    │   │
│  │  • buscar_productos()  • calcular_total_pedido()     │   │
│  │  • validar_datos_envio() • generar_link_pago()       │   │
│  └──────────────────────────────────────────────────────┘   │
└───────────────────────┬─────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  SQLite DB   │ │  Products    │ │  FastAPI     │
│  (Historial) │ │  (JSON)      │ │  (API REST)  │
└──────────────┘ └──────────────┘ └──────────────┘
```

### Componentes del Sistema

#### 1. **Agentes Especializados** (`agents/`)
- **SalesAgent**: Coordinador principal que gestiona el flujo de ventas
- **ProductAgent**: Experto en búsqueda y consulta de productos
- **OrderAgent**: Especialista en armado de pedidos y generación de pagos

#### 2. **Herramientas Personalizadas** (`tools/`)
- **product_tools.py**: Funciones para buscar y consultar productos
- **payment_tools.py**: Funciones para calcular totales, validar datos y generar links de pago

#### 3. **Base de Datos** (`data/`)
- **SQLite**: Almacena el historial de conversaciones y sesiones
- **products.json**: Catálogo de productos disponible

#### 4. **API REST** (`api/`)
- Endpoints FastAPI para interactuar con el sistema
- Gestión de pedidos y consultas

#### 5. **Interfaz Web** (`web/` y `agent-ui/`)
- **payment.html**: Página simulada de pago
- **agent-ui/**: Interfaz visual moderna con Next.js

---

## 🚀 Instalación

### Requisitos Previos

- **Python 3.8 o superior**
- **Node.js 18+ y pnpm** (para AgentUI)
- **Clave API de OpenAI** (o el proveedor de LLM que prefieras)

### Paso 1: Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd Agentes_IA
```

### Paso 2: Crear Entorno Virtual (Recomendado)

```bash
python3 -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

### Paso 3: Instalar Dependencias de Python

```bash
pip install -r requirements.txt
```

### Paso 4: Configurar Variables de Entorno

```bash
cp .env.example .env
```

Edita el archivo `.env` y agrega tu clave API:

```env
MODEL_PROVIDER=openai
MODEL_ID=gpt-4o-mini
OPENAI_API_KEY=tu_clave_api_aqui
DB_FILE=data/agno.db
HOST=0.0.0.0
PORT=7777
```

### Paso 5: Instalar AgentUI (Opcional pero Recomendado)

```bash
cd agent-ui
pnpm install
```

Si no tienes `pnpm` instalado:

```bash
npm install -g pnpm
```

---

## 📱 Uso

### Opción 1: Usar con AgentUI (Recomendado)

AgentUI proporciona una interfaz visual moderna y fácil de usar.

#### 1. Iniciar el Backend (AgentOS)

En una terminal:

```bash
python main.py
```

Deberías ver:
```
🚀 Sistema de Ventas Multi-Agente iniciado
📡 Servidor corriendo en http://0.0.0.0:7777
🤖 Team de ventas listo para recibir consultas
💳 Página de pago disponible en http://0.0.0.0:7777/payment/{order_id}
```

#### 2. Iniciar AgentUI

En otra terminal:

```bash
cd agent-ui
pnpm dev
```

#### 3. Abrir en el Navegador

1. Abre [http://localhost:3000](http://localhost:3000)
2. AgentUI se conectará automáticamente a `http://localhost:7777`
3. Selecciona **"SalesTeam"** en el selector de agentes/teams
4. ¡Comienza a chatear!

#### Características de AgentUI

- 💬 **Chat en tiempo real** con streaming de respuestas
- 🧩 **Visualización de herramientas** utilizadas por los agentes
- 🧠 **Pasos de razonamiento** visibles
- 📚 **Referencias y fuentes** de información
- 🖼️ **Soporte multi-modal** (imágenes, video, audio)
- 📝 **Historial persistente** de conversaciones

### Opción 2: Usar la API Directamente

Puedes interactuar con el sistema usando la API REST:

#### Enviar un Mensaje

```bash
curl -X POST "http://localhost:7777/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Hola, busco una laptop",
    "session_id": "mi-sesion-123"
  }'
```

#### Ver Estado de la Sesión

```bash
curl "http://localhost:7777/status?session_id=mi-sesion-123"
```

---

## 🔄 Flujo de Trabajo Detallado

### 1. **Inicio de Conversación**
El cliente inicia una conversación. El **SalesAgent** (coordinador) saluda y pregunta en qué puede ayudar.

### 2. **Consulta de Productos**
Cuando el cliente busca productos:
- El **SalesAgent** delega al **ProductAgent**
- El **ProductAgent** usa sus herramientas para buscar en el catálogo
- Los resultados se presentan al cliente de forma atractiva

### 3. **Selección de Productos**
El cliente selecciona productos:
- El **SalesAgent** confirma cada selección
- Mantiene un registro mental de todos los productos elegidos
- Pregunta si desea agregar algo más

### 4. **Iteración**
El proceso se repite hasta que el cliente indica que no quiere más productos (puede decir "no quiero más", "eso es todo", "listo", etc.).

### 5. **Armado del Pedido**
Cuando el cliente termina de seleccionar:
- El **SalesAgent** delega al **OrderAgent**
- El **OrderAgent**:
  1. Recopila todos los productos seleccionados
  2. Calcula el total (incluyendo impuestos del 21%)
  3. Solicita los datos de envío (nombre, dirección, ciudad, código postal, teléfono, email)
  4. Valida los datos de envío
  5. Genera un ID único para el pedido
  6. Genera el link de pago

### 6. **Finalización**
Se presenta al cliente:
- Resumen completo del pedido
- Lista de productos con cantidades y precios
- Datos de envío confirmados
- Subtotal, impuestos y total final
- Link de pago único

### 7. **Pago**
El cliente puede hacer clic en el link de pago para acceder a la página de pago simulada.

---

## 🔌 API Endpoints

### Endpoints Principales

#### `POST /chat`
Envía un mensaje al team de ventas.

**Request:**
```json
{
  "message": "Hola, busco una laptop",
  "session_id": "opcional-session-id"
}
```

**Response:**
```json
{
  "response": "¡Hola! Con gusto te ayudo a encontrar una laptop...",
  "session_id": "generated-session-id"
}
```

#### `GET /status`
Obtiene el estado de la sesión actual.

**Query Parameters:**
- `session_id` (opcional): ID de la sesión

#### `GET /payment/{order_id}`
Muestra la página de pago simulada para un pedido específico.

**Ejemplo:**
```
http://localhost:7777/payment/ORD-ABC12345
```

### Endpoints Adicionales

#### `GET /api/health`
Verifica el estado de salud del sistema.

#### `GET /api/products`
Obtiene todos los productos disponibles.

#### `GET /api/products/{product_id}`
Obtiene un producto específico por ID.

#### `GET /api/order/{order_id}`
Obtiene información de un pedido específico.

#### `POST /api/order`
Almacena un nuevo pedido (usado internamente).

### Documentación Interactiva

Una vez que el servidor esté corriendo, puedes acceder a la documentación interactiva de la API en:
- **Swagger UI**: [http://localhost:7777/docs](http://localhost:7777/docs)
- **ReDoc**: [http://localhost:7777/redoc](http://localhost:7777/redoc)

---

## 🛠️ Configuración Avanzada

### Cambiar el Modelo LLM

Puedes usar cualquier modelo compatible con Agno. Edita `.env`:

```env
MODEL_PROVIDER=openai  # o anthropic, etc.
MODEL_ID=gpt-4o-mini   # o gpt-4, claude-3-opus, etc.
```

### Configurar la Base de Datos

Por defecto se usa SQLite. Puedes cambiar la ubicación en `.env`:

```env
DB_FILE=data/agno.db
```

### Ajustar el Servidor

```env
HOST=0.0.0.0  # Escuchar en todas las interfaces
PORT=7777     # Puerto del servidor
```

### Agregar Productos

Edita `data/products.json` para agregar o modificar productos:

```json
{
  "id": 1,
  "name": "Nombre del Producto",
  "description": "Descripción detallada",
  "price": 99.99,
  "category": "Categoría",
  "stock": 10,
  "image": "URL de la imagen"
}
```

---

## 💡 Habilidades Técnicas Demostradas

Este proyecto demuestra competencia en:

### 🤖 Desarrollo de Sistemas Multi-Agente
- **Arquitectura de agentes**: Diseño de agentes especializados con roles claros
- **Coordinación de equipos**: Implementación de teams con delegación inteligente
- **Comunicación entre agentes**: Sistema de mensajería y contexto compartido
- **Memoria persistente**: Almacenamiento y recuperación de historial de conversaciones

### 🛠️ Desarrollo de Herramientas (Tools)
- **Funciones personalizadas**: Creación de tools específicas para el dominio
- **Validación de datos**: Implementación de validaciones robustas
- **Integración con APIs**: Conexión con servicios externos
- **Manejo de errores**: Gestión de errores y casos edge

### 🏗️ Arquitectura de Software
- **Separación de responsabilidades**: Código modular y organizado
- **Configuración centralizada**: Gestión de configuración con variables de entorno
- **API RESTful**: Diseño de endpoints REST bien estructurados
- **Integración frontend-backend**: Conexión entre AgentUI y AgentOS

### 🗄️ Persistencia de Datos
- **SQLite**: Uso de base de datos relacional para historial
- **JSON**: Almacenamiento de catálogo de productos
- **Gestión de sesiones**: Manejo de sesiones de usuario

### 🎨 Desarrollo Frontend
- **Next.js/TypeScript**: Interfaz moderna con TypeScript
- **UI/UX**: Diseño de interfaz de usuario intuitiva
- **Streaming en tiempo real**: Visualización de respuestas en tiempo real

### 🔧 DevOps y Deployment
- **Gestión de dependencias**: requirements.txt y package.json
- **Variables de entorno**: Configuración segura con .env
- **Documentación**: README completo y detallado

---

## 📚 Conceptos Técnicos Explicados

### ¿Qué es Agno Framework?

Agno es un framework de código abierto para construir sistemas multi-agente. Proporciona:
- **Runtime de alto rendimiento** para ejecutar agentes
- **Sistema de herramientas** para extender capacidades
- **Gestión de memoria** y persistencia
- **API REST** integrada
- **Interfaz de control** para monitoreo

### ¿Qué es un LLM (Large Language Model)?

Un LLM es un modelo de inteligencia artificial entrenado con grandes cantidades de texto. Puede:
- Entender lenguaje natural
- Generar respuestas coherentes
- Realizar razonamiento básico
- Seguir instrucciones complejas

En este proyecto, usamos modelos como GPT-4o-mini de OpenAI, pero puedes usar cualquier modelo compatible.

### ¿Qué es FastAPI?

FastAPI es un framework moderno de Python para construir APIs REST. Ofrece:
- **Alto rendimiento**: Comparable a Node.js y Go
- **Documentación automática**: Genera Swagger/OpenAPI automáticamente
- **Validación de datos**: Con Pydantic
- **Type hints**: Soporte completo para tipos de Python

### ¿Qué es SQLite?

SQLite es una base de datos relacional ligera que almacena datos en un archivo. Es perfecta para:
- Aplicaciones pequeñas y medianas
- Prototipos y desarrollo
- Almacenamiento local
- No requiere servidor separado

### ¿Qué es AgentUI?

AgentUI es una interfaz de usuario de código abierto para interactuar con AgentOS. Proporciona:
- Interfaz visual moderna
- Visualización de herramientas y razonamiento
- Historial de conversaciones
- Soporte multi-modal

---

## 🔮 Mejoras Futuras

### Funcionalidades Planeadas

- [ ] **Integración con pasarelas de pago reales** (Stripe, PayPal, etc.)
- [ ] **Sistema de autenticación de usuarios**
- [ ] **Panel de administración** para gestionar productos
- [ ] **Análisis y reportes** de ventas
- [ ] **Soporte multi-idioma**
- [ ] **Integración con sistemas de inventario**
- [ ] **Notificaciones por email** de confirmación de pedidos
- [ ] **Sistema de recomendaciones** de productos
- [ ] **Chatbot con voz** (text-to-speech y speech-to-text)
- [ ] **Integración con CRM** existentes

### Mejoras Técnicas

- [ ] **Tests automatizados** (unitarios e integración)
- [ ] **Dockerización** del proyecto
- [ ] **CI/CD pipeline** para deployment automático
- [ ] **Monitoreo y logging** avanzado
- [ ] **Caché de respuestas** para mejorar rendimiento
- [ ] **Rate limiting** para proteger la API
- [ ] **Migración a PostgreSQL** para producción
- [ ] **Implementación de WebSockets** para actualizaciones en tiempo real

---

## 📖 Estructura del Proyecto

```
Agentes_IA/
├── agents/              # Agentes especializados
│   ├── __init__.py
│   ├── sales_agent.py   # Agente coordinador de ventas
│   ├── product_agent.py # Agente experto en productos
│   └── order_agent.py   # Agente especialista en pedidos
│
├── tools/               # Herramientas personalizadas
│   ├── __init__.py
│   ├── product_tools.py # Herramientas de búsqueda de productos
│   └── payment_tools.py # Herramientas de pago y pedidos
│
├── data/                # Datos y base de datos
│   ├── products.json    # Catálogo de productos
│   └── agno.db          # Base de datos SQLite (se crea automáticamente)
│
├── api/                 # Endpoints FastAPI adicionales
│   ├── __init__.py
│   └── routes.py        # Rutas de la API
│
├── web/                 # Interfaz web
│   └── payment.html     # Página de pago simulada
│
├── config/              # Configuración
│   ├── __init__.py
│   └── settings.py      # Configuración centralizada
│
├── agent-ui/            # Interfaz visual AgentUI (Next.js)
│   ├── src/
│   ├── package.json
│   └── ...
│
├── main.py              # Punto de entrada principal
├── requirements.txt     # Dependencias de Python
├── .env.example         # Ejemplo de variables de entorno
├── .env                 # Variables de entorno (no versionado)
└── README.md            # Este archivo
```

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 👨‍💻 Autor

**Pablo Mereles**

Desarrollador especializado en sistemas multi-agente e inteligencia artificial.

- 💼 Portfolio: [Tu portfolio aquí]
- 📧 Email: [Tu email aquí]
- 🐙 GitHub: [Tu GitHub aquí]
- 💼 LinkedIn: [Tu LinkedIn aquí]

---

## 🙏 Agradecimientos

- [Agno Framework](https://agno.com) por proporcionar una excelente plataforma para sistemas multi-agente
- [OpenAI](https://openai.com) por los modelos de lenguaje
- [FastAPI](https://fastapi.tiangolo.com) por el framework web
- [AgentUI](https://github.com/agno-agi/agent-ui) por la interfaz visual

---

## 📞 Soporte

Si tienes preguntas o necesitas ayuda:

1. Revisa la documentación de [Agno](https://docs.agno.com)
2. Abre un issue en el repositorio
3. Contacta al autor

---

**¡Gracias por usar este proyecto! 🚀**
