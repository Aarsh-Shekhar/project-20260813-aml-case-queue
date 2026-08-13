import unittest

from aml_case_queue.models import Record
from aml_case_queue.scoring import score_record


class DepthCheck8(unittest.TestCase):
    def test_008_field_validation(self):
        record = Record(id="case-008", exposure=8050, signal=0.343, urgency=4)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
