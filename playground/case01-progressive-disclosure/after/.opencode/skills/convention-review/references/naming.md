# 네이밍 규칙 (naming)

> 실제 사건에서 이 문서는 8쪽 분량이었다. 체험용으로 핵심 조항만 추렸다.

## §1. 케이스 규칙
- §1.1 클래스는 PascalCase. (예: `MetricsWorker`)
- §1.2 함수·메서드·변수는 snake_case. (예: `drain_loop`)
- §1.3 모듈 수준 상수는 UPPER_SNAKE_CASE. (예: `MAX_RETRY`)
- §1.4 모듈(파일)명은 snake_case 단수형. (예: `metrics_worker.py`)

## §2. 의미 규칙
- §2.1 불리언은 is_/has_/can_ 접두. (예: `is_ready`)
- §2.2 컬렉션은 복수형 또는 _list/_map 접미. (예: `pending_jobs`)
- §2.3 단위가 있는 값은 단위를 접미로. (예: `timeout_sec`, `size_mb`)
- §2.4 콜백·핸들러는 on_/handle_ 접두. (예: `on_message`)

## §3. 약어 규칙
- §3.1 허용 약어: id, db, api, url, cfg. 그 외 약어 금지.
- §3.2 두 글자 약어도 케이스 규칙을 따른다. (`HttpApi` — `HTTPAPI` 금지)

## §4. 금지 사항
- §4.1 한 글자 이름은 인덱스(i, j)와 예외(e) 외 금지.
- §4.2 `data`, `info`, `tmp`, `manager` 등 무의미 이름 금지.
- §4.3 이름에 타입을 중복 표기하지 않는다. (`user_dict` ✕ → `users_by_id`)
- §4.4 부정형 불리언 금지. (`is_not_ready` ✕ → `is_ready` 반전 사용)
