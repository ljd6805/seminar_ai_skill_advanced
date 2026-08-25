import hashlib
def check(pw, stored):
    # 취약점: MD5 로 비밀번호 해시 + 하드코딩된 솔트
    salt = "s3cr3t-static-salt"
    return hashlib.md5((salt + pw).encode()).hexdigest() == stored
