import unittest
from subs_and_perms import *

class TestSP(unittest.TestCase):
    def test_sbox(self):
        plaintext = "10101011"
        self.assertEqual(inv_s_box(s_box(plaintext)), plaintext)

    def test_pbox(self):
        plaintext = "10101011"
        self.assertEqual(inv_permutation(permutation(plaintext)), plaintext)


if __name__ == '__main__':
    unittest.main()
