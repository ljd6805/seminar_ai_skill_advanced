"""auth_client — v2 API 스타일 (마이그레이션 완료 01)."""
from api.http import client, ApiError


def login(payload):
    try:
        resp = client.request("POST", "/v2/auth/login", json=payload)
    except ApiError as e:
        raise RuntimeError(f"auth_client 실패: {e}")
    return resp.json()["data"]
