"""catalog_client — v1 API 스타일 (마이그레이션 대상 08)."""
from legacy.http import client, LegacyError


def fetch(payload):
    try:
        resp = client.call("/v1/catalog", payload)
    except LegacyError as e:
        raise RuntimeError(f"catalog_client 실패: {e}")
    return resp.data
