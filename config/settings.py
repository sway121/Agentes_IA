"""Configuración centralizada del sistema."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Directorio base del proyecto
BASE_DIR = Path(__file__).parent.parent

# Configuración del Modelo LLM
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "openai")
MODEL_ID = os.getenv("MODEL_ID", "gpt-4o-mini")

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Configuración de Base de Datos
DB_FILE = os.getenv("DB_FILE", str(BASE_DIR / "data" / "agno.db"))

# Asegurar que el directorio data existe
DB_DIR = Path(DB_FILE).parent
DB_DIR.mkdir(parents=True, exist_ok=True)

# Configuración del Servidor
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 7777))

# Rutas de archivos
PRODUCTS_JSON = BASE_DIR / "data" / "products.json"

# Configuración de AgentOS
AGENTOS_CONFIG = {
    "host": HOST,
    "port": PORT,
}


