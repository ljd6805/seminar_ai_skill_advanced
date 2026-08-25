def find_user(db, name):
    # 취약점: SQL 문자열 포매팅 (SQL 인젝션)
    return db.execute("SELECT * FROM users WHERE name = '%s'" % name)
