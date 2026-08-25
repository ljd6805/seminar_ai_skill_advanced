import os
def save(upload_name, data, base="/srv/uploads"):
    # 취약점: 경로 검증 없음 (path traversal — ../ 허용)
    path = os.path.join(base, upload_name)
    with open(path, "wb") as f:
        f.write(data)
    return path
