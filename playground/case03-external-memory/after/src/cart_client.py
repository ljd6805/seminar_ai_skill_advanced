"""cart_client — v1 API 스타일 (마이그레이션 대상 02)."""
from legacy.http import client, LegacyError


def add_item(payload):
    try:
        resp = client.call("/v1/cart/items", payload)
    except LegacyError as e:
        raise RuntimeError(f"cart_client 실패: {e}")
    return resp.data
