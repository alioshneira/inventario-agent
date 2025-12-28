from ..utils import run_cmd

def collect_running_services():
    # Lista servicios activos (systemd)
    out = run_cmd("systemctl list-units --type=service --state=running --no-pager --no-legend")
    services = []
    if out:
        for line in out.splitlines():
            # Formato: UNIT LOAD ACTIVE SUB DESCRIPTION
            # Tomamos el UNIT y DESCRIPTION
            parts = line.split(None, 4)
            if len(parts) >= 5:
                services.append({"unit": parts[0], "description": parts[4]})
    return services
