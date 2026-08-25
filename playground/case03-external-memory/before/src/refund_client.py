"""refund_client — v1 API 스타일 (마이그레이션 대상 06)."""
from legacy.http import client, LegacyError


def issue(payload):
    try:
        resp = client.call("/v1/refunds", payload)
    except LegacyError as e:
        raise RuntimeError(f"refund_client 실패: {e}")
    return resp.data
