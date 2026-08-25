"""cart_client — v2 API 스타일 (마이그레이션 완료 02)."""
from api.http import client, ApiError


def add_item(payload):
    try:
        resp = client.request("POST", "/v2/cart/items", json=payload)
    except ApiError as e:
        raise RuntimeError(f"cart_client 실패: {e}")
    return resp.json()["data"]
