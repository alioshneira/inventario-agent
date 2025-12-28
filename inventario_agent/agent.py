import os
import sys

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from inventario_agent.config import Config
from inventario_agent.api import ApiClient
from inventario_agent.scheduler import Scheduler
from inventario_agent.net import get_hostname, get_ips
from inventario_agent.collectors.system import collect_os, collect_cpu, collect_ram
from inventario_agent.collectors.services import collect_running_services
from inventario_agent.collectors.docker import collect_containers, collect_images
from inventario_agent.collectors.web import collect_apache_vhosts, collect_nginx_servers
from inventario_agent.utils import run_cmd

def collect_snapshot():
    snapshot = {
        "host": {
            "hostname": get_hostname(),
            "ips": get_ips(),
        },
        "system": {
            "os": collect_os(),
            "cpu": collect_cpu(),
            "ram": collect_ram(),
            "kernel": run_cmd("uname -r") or "",
        },
        "services": collect_running_services(),
        "docker": {},
        "web": {}
    }

    if Config.ENABLE_DOCKER:
        snapshot["docker"]["containers"] = collect_containers()
        snapshot["docker"]["images"] = collect_images()

    if Config.ENABLE_APACHE:
        snapshot["web"]["apache_vhosts"] = collect_apache_vhosts()

    if Config.ENABLE_NGINX:
        snapshot["web"]["nginx_servers"] = collect_nginx_servers()

    return snapshot

def tick(api: ApiClient):
    datos = collect_snapshot()
    status, text = api.post_inventory(Config.SERVER_ID, datos)
    if status == 201:
        print("[agent] snapshot enviado OK")
    else:
        print(f"[agent] envío fallo ({status}): {text}")

def main():
    api = ApiClient(
        base_url=Config.API_URL,
        endpoint=Config.API_ENDPOINT,
        token=Config.API_TOKEN,
        verify_tls=Config.VERIFY_TLS
    )
    sched = Scheduler(interval_seconds=Config.INTERVAL_SECONDS)
    print("[agent] iniciando agente de inventario...")
    sched.run_forever(lambda: tick(api))

if __name__ == "__main__":
    main()
