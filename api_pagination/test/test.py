from unittest import TestCase
from api_pagination import api_pagination


class TestRunFunction(TestCase):
    def test_run_exists(self):
        self.assertTrue(bool(api_pagination.run))
