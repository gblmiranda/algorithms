import unittest
from ..dynamic_programming import lcs


class TestLCS(unittest.TestCase):
    """
    Tests LCS
    """

    def setUp(self):
        self.words = (("ACTG", "ACGTG", "ACTG"),
                      ("TATACC", "ATAGGCT", "ATAC"),
                      ("GCGTG", "GAAACT", "GCT"))

    def test_lcs(self):
        for t in self.words:
            self.assertEqual(lcs.lcs(t[0], t[1]), t[2])
