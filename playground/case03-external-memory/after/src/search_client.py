"""search_client — v1 API 스타일 (마이그레이션 대상 07)."""
from legacy.http import client, LegacyError


def query(payload):
    try:
        resp = client.call("/v1/search", payload)
    except LegacyError as e:
        raise RuntimeError(f"search_client 실패: {e}")
    return resp.data
