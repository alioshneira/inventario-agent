import subprocess
import shlex

def run_cmd(cmd, timeout=10):
    try:
        # Usa shell=False con shlex.split para mayor seguridad
        proc = subprocess.run(shlex.split(cmd), capture_output=True, text=True, timeout=timeout)
        if proc.returncode == 0:
            return proc.stdout.strip()
        return None
    except Exception:
        return None
