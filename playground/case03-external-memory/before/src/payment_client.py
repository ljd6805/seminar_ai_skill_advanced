"""payment_client — v1 API 스타일 (마이그레이션 대상 03)."""
from legacy.http import client, LegacyError


def charge(payload):
    try:
        resp = client.call("/v1/payments", payload)
    except LegacyError as e:
        raise RuntimeError(f"payment_client 실패: {e}")
    return resp.data
