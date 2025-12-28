import json
from ..utils import run_cmd

def collect_containers():
    out = run_cmd("docker ps --format '{{json .}}'")
    containers = []
    if out:
        for line in out.splitlines():
            try:
                containers.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return containers

def collect_images():
    out = run_cmd("docker images --format '{{json .}}'")
    images = []
    if out:
        for line in out.splitlines():
            try:
                images.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return images
