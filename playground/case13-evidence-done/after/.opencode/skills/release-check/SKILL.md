---
name: release-check
description: 배포 전 점검 요청 시 사용 (증거표 첨부 의무)
---
# Release Check

## 출력 규칙
- **"완료" 선언은 증거표가 채워진 경우에만** 허용한다.
- 증거표 각 행 (assets/evidence-form.md):
  `점검 항목 | 실행한 명령 | 출력 원문(3줄 이내) | 판정(PASS/FAIL/미실행)`
- 실행하지 못한 항목은 판정을 `미실행` + 사유로 남긴다. (빈칸·추정 금지)
- 증거가 없는 문장은 리포트에 쓰지 않는다.

## 점검 항목 (env/ 기준)
1. 헬스체크: `cat env/health.txt`
2. 디스크 여유: `cat env/disk.txt`
3. 백업 존재: `ls env/backups/`
4. DB 마이그레이션 준비: `cat env/migrate_check.txt` (권한 오류가 심겨 있음 → 미실행 처리)
5. 설정 검증: `cat env/config_check.txt`
6~8. (팀 점검 목록에 따라 확장)

## 사람의 확인
- 증거표만 훑고, "미실행"·"FAIL" 행만 조치 대상으로 넘긴다.
