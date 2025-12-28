from ..utils import run_cmd

def collect_apache_vhosts():
    # Lee archivos habilitados (Debian/Ubuntu). Ajusta rutas según distro.
    out = run_cmd("bash -c \"cat /etc/apache2/sites-enabled/*.conf\"")
    return out or ""

def collect_nginx_servers():
    out = run_cmd("bash -c \"cat /etc/nginx/sites-enabled/*.conf\"")
    return out or ""
