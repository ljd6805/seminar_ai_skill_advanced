"""coupon_client — v1 API 스타일 (마이그레이션 대상 05)."""
from legacy.http import client, LegacyError


def redeem(payload):
    try:
        resp = client.call("/v1/coupons/redeem", payload)
    except LegacyError as e:
        raise RuntimeError(f"coupon_client 실패: {e}")
    return resp.data
