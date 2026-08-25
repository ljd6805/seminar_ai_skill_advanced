"""shipping_client — v1 API 스타일 (마이그레이션 대상 04)."""
from legacy.http import client, LegacyError


def quote(payload):
    try:
        resp = client.call("/v1/shipping/quote", payload)
    except LegacyError as e:
        raise RuntimeError(f"shipping_client 실패: {e}")
    return resp.data
