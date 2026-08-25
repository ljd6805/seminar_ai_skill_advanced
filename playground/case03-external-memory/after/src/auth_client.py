"""auth_client — v1 API 스타일 (마이그레이션 대상 01)."""
from legacy.http import client, LegacyError


def login(payload):
    try:
        resp = client.call("/v1/auth/login", payload)
    except LegacyError as e:
        raise RuntimeError(f"auth_client 실패: {e}")
    return resp.data
