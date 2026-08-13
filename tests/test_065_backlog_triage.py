import unittest

from aml_case_queue.models import Record
from aml_case_queue.scoring import score_record


class DepthCheck65(unittest.TestCase):
    def test_065_backlog_triage(self):
        record = Record(id="case-065", exposure=6521, signal=0.530, urgency=4)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
