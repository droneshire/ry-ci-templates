import unittest

from ry_ci_templates import __doc__


class BasicTest(unittest.TestCase):
    def test_module_imports(self) -> None:
        self.assertIsNotNone(__doc__)
