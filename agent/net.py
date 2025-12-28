from .utils import run_cmd

def get_hostname():
    return run_cmd("hostname") or ""

def get_ips():
    # Devuelve IPs visibles (simple: hostname -I)
    ips = run_cmd("hostname -I") or ""
    return [ip for ip in ips.split() if ip]
