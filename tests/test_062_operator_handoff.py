import unittest

from aml_case_queue.models import Record
from aml_case_queue.scoring import score_record


class DepthCheck62(unittest.TestCase):
    def test_062_operator_handoff(self):
        record = Record(id="case-062", exposure=9694, signal=0.500, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
