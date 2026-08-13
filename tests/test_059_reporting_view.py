import unittest

from aml_case_queue.models import Record
from aml_case_queue.scoring import score_record


class DepthCheck59(unittest.TestCase):
    def test_059_reporting_view(self):
        record = Record(id="case-059", exposure=68640, signal=0.715, urgency=5)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
