"""교육용 검사기의 실제 오통과 사례와 입력 경계를 검증한다."""
import contextlib
import importlib.util
import io
import unittest
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / 'playground/case12-script-judged/after'
GATE_CASE = ROOT / 'playground/case08-stage-gate/after'


def module_at(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


V = module_at('validator', CASE / '.opencode/skills/test-report/scripts/validate.py')
G = module_at('gate', GATE_CASE / '.opencode/skills/incident-report/scripts/gate.py')


class ReportValidation(unittest.TestCase):
    def setUp(self):
        self.good = (CASE / 'output/test-report.good.md').read_text()
        self.source = (CASE / 'data/test_results.csv').read_text()

    def test_valid_report(self):
        self.assertEqual(V.validate(self.good, self.source), [])

    def test_wrong_but_self_consistent_summary_is_rejected(self):
        wrong = self.good.replace('PASS: 12 · FAIL: 3', 'PASS: 10 · FAIL: 5')
        self.assertTrue(any('원본 CSV와 요약' in p for p in V.validate(wrong, self.source)))

    def test_wrong_suite_distribution_with_same_total_is_rejected(self):
        wrong = self.good.replace('| checkout | 2 | 1 | 0 |', '| checkout | 1 | 2 | 0 |')
        wrong = wrong.replace('| auth | 2 | 1 | 0 |', '| auth | 3 | 0 | 0 |')
        self.assertTrue(any('결과표 불일치' in p for p in V.validate(wrong, self.source)))

    def test_missing_skip_is_rejected(self):
        self.assertTrue(V.validate(self.good.replace('SKIP: 2 · ', ''), self.source))

    def test_single_empty_cell_is_rejected(self):
        self.assertTrue(V.validate(self.good.replace('| cart | 2 |', '| cart |  |'), self.source))

    def test_empty_environment_is_rejected(self):
        start, end = self.good.index('## 환경'), self.good.index('## 결과표')
        self.assertTrue(V.validate(self.good[:start] + '## 환경\n\n' + self.good[end:], self.source))

    def test_duplicate_case_is_rejected(self):
        self.assertTrue(V.validate(self.good, self.source + 'checkout,tc_place_order,PASS\n'))

    def test_invalid_status_is_rejected(self):
        self.assertTrue(V.validate(self.good, self.source.replace(',SKIP', ',UNKNOWN', 1)))

    def test_duplicate_suite_is_rejected(self):
        self.assertTrue(V.validate(self.good.replace('## 특이사항', '| cart | 2 | 0 | 1 |\n\n## 특이사항'), self.source))

    def test_duplicate_summary_number_is_rejected(self):
        self.assertTrue(V.validate(self.good.replace('## 환경', 'PASS: 12\n\n## 환경'), self.source))

    def test_negative_and_decimal_numbers_are_rejected(self):
        for value in ['-12', '12.0', '12junk']:
            with self.subTest(value=value):
                self.assertTrue(V.validate(self.good.replace('PASS: 12', 'PASS: ' + value), self.source))

    def test_appended_verdict_does_not_supply_missing_summary(self):
        text = self.good.replace('SKIP: 2 · ', '') + '\nPASS: 12 FAIL: 3 SKIP: 2 전체: 17\n'
        self.assertTrue(V.validate(text, self.source))

    def test_uncertainty_language_is_allowed(self):
        self.assertEqual(V.validate(self.good + '\n아마 원인이 다를 수 있어 추가 확인이 필요하다.\n', self.source), [])

    def test_conventional_markdown_separator_is_allowed(self):
        text = self.good.replace('| suite | PASS | FAIL | SKIP |', '| suite | PASS | FAIL | SKIP |\n|---|---:|---:|---:|')
        self.assertEqual(V.validate(text, self.source), [])

    def test_missing_source_fails_closed(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(V.main(CASE / 'output/test-report.good.md', CASE / 'data/absent.csv'), 1)

    def test_bad_example_is_rejected(self):
        self.assertTrue(V.validate((CASE / 'output/test-report.bad.md').read_text(), self.source))


class GateValidation(unittest.TestCase):
    def test_good_and_bad_examples(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(G.main(GATE_CASE / 'output/analysis.good.md'), 0)
            self.assertEqual(G.main(GATE_CASE / 'output/analysis.bad.md'), 1)

    def test_gate_has_no_semantic_truth_check(self):
        # 근거 없는 문장도 형식 검사를 통과한다는 예제 게이트의 한계를 확인한다.
        text = '\n'.join('## ' + title + '\n' + '근거를 확인하지 않은 임의의 문장입니다.' for title in G.REQUIRED)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'unsupported.md'
            path.write_text(text)
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(G.main(path), 0)


if __name__ == '__main__':
    unittest.main()
