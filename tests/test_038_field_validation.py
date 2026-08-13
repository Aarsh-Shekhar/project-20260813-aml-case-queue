import unittest

from aml_case_queue.models import Record
from aml_case_queue.scoring import score_record


class DepthCheck38(unittest.TestCase):
    def test_038_field_validation(self):
        record = Record(id="case-038", exposure=22000, signal=0.593, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
