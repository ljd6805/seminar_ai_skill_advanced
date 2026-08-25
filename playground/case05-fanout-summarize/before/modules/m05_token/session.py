import random
def new_token():
    # 취약점: 예측 가능한 난수(random) 로 세션 토큰 생성
    return "".join(random.choice("0123456789abcdef") for _ in range(16))
