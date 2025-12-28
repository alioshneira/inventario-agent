import requests

class ApiClient:
    def __init__(self, base_url: str, endpoint: str, token: str | None, verify_tls: bool = True):
        self.base_url = base_url.rstrip("/")
        self.endpoint = endpoint
        self.token = token
        self.verify_tls = verify_tls

    def post_inventory(self, servidor_id: int, datos: dict) -> tuple[int, str]:
        url = f"{self.base_url}{self.endpoint}"
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        payload = {
            "servidor": servidor_id,
            "datos": datos
        }
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=15, verify=self.verify_tls)
            return resp.status_code, resp.text
        except Exception as e:
            return 0, f"error: {e}"
