from ..utils import run_cmd

def collect_os():
    # /etc/os-release tiene pares clave=valor
    content = run_cmd("cat /etc/os-release")
    data = {}
    if content:
        for line in content.splitlines():
            if "=" in line:
                k, v = line.split("=", 1)
                data[k] = v.strip().strip('"')
    return data

def collect_cpu():
    # Model name (Linux)
    model = run_cmd("bash -c \"lscpu | grep 'Model name' | awk -F: '{print $2}'\"")
    cores = run_cmd("bash -c \"lscpu | grep '^CPU(s):' | awk -F: '{print $2}'\"")
    return {
        "model": (model or "").strip(),
        "cores": int(cores.strip()) if cores and cores.strip().isdigit() else None,
    }

def collect_ram():
    line = run_cmd("bash -c \"free -m | awk '/Mem:/ {print $2\" \"$3\" \"$4}'\"")
    total = used = free = None
    if line:
        parts = line.split()
        if len(parts) >= 3:
            total, used, free = parts[:3]
    return {
        "total_mb": int(total) if total and total.isdigit() else None,
        "used_mb": int(used) if used and used.isdigit() else None,
        "free_mb": int(free) if free and free.isdigit() else None,
    }
