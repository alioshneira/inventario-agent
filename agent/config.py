import os

def str2bool(v):
    return str(v).lower() in ("1", "true", "yes", "on")

class Config:
    API_URL = os.getenv("API_URL", "http://localhost:8000")
    API_ENDPOINT = os.getenv("API_ENDPOINT", "/api/inventario/")
    SERVER_ID = int(os.getenv("SERVER_ID", "1"))
    INTERVAL_SECONDS = int(os.getenv("INTERVAL_SECONDS", "300"))
    API_TOKEN = os.getenv("API_TOKEN")  # opcional
    ENABLE_DOCKER = str2bool(os.getenv("ENABLE_DOCKER", "true"))
    ENABLE_APACHE = str2bool(os.getenv("ENABLE_APACHE", "true"))
    ENABLE_NGINX = str2bool(os.getenv("ENABLE_NGINX", "true"))
    TIMEOUT_CMD = int(os.getenv("TIMEOUT_CMD", "10"))
    VERIFY_TLS = str2bool(os.getenv("VERIFY_TLS", "true"))
