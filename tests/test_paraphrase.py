"""paraphrase-lite 单元测试。运行：python3 -m unittest discover -s tests"""
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from paraphrase import paraphrase, paraphrase_variants, SYNONYMS  # noqa: E402


class TestZh(unittest.TestCase):
    def test_replace(self):
        out = paraphrase("我很高兴来到这美丽的地方")
        self.assertNotIn("高兴", out)
        self.assertNotIn("美丽", out)

    def test_preserve_meaning_words(self):
        out = paraphrase("他快速帮助了我")
        self.assertNotEqual(out, "他快速帮助了我")


class TestEn(unittest.TestCase):
    def test_word_boundary(self):
        out = paraphrase("I am happy and the big dog runs fast")
        self.assertNotIn("happy", out)
        self.assertNotIn("big", out)
        self.assertNotIn("fast", out)

    def test_case(self):
        out = paraphrase("Happy day")
        self.assertTrue(out.startswith("Glad") or out.startswith("Cheerful")
                        or out.startswith("Delighted"))

    def test_no_partial(self):
        out = paraphrase("The box is bigger than that")
        self.assertIn("bigger", out)


class TestVariants(unittest.TestCase):
    def test_multiple(self):
        vs = paraphrase_variants("我很高兴", n=2)
        self.assertGreaterEqual(len(vs), 1)
        self.assertEqual(len(vs), len(set(vs)))


if __name__ == "__main__":
    unittest.main()
