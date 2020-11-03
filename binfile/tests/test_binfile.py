import unittest
import tempfile
import binfile


class TestBinFile(unittest.TestCase):

    tmpfile_ = None

    def setUp(self):
        self.tempfile_ = tempfile.TemporaryFile(mode="w+b")
        self.tempfile_.write(
            bytes([130, 104, 101, 0, 108, 108, 111, 32, 119, 111, 114, 108, 100, 0])
        )
        self.tempfile_.seek(0)

    def tearDown(self):
        self.tempfile_.close()
        self.tempfile_ = None

    def test_u8(self):
        b = binfile.BinFile(self.tempfile_)
        self.assertEqual(b.read_u8(), 130)
        self.assertEqual(b.read_u8(), 104)
        self.assertEqual(b.read_u8(), 101)
        self.assertEqual(b.read_u8(), 0)
        self.assertEqual(self.tempfile_.tell(), 4)

    def test_s8(self):
        b = binfile.BinFile(self.tempfile_)
        self.assertEqual(b.read_s8(), -126)
        self.assertEqual(b.read_s8(), 104)
        self.assertEqual(b.read_s8(), 101)
        self.assertEqual(b.read_s8(), 0)
        self.assertEqual(self.tempfile_.tell(), 4)

    def test_u16_le(self):
        b = binfile.BinFile(self.tempfile_, little=True)
        self.assertEqual(b.read_u16(), 26754)
        self.assertEqual(b.read_u16(), 101)
        self.assertEqual(self.tempfile_.tell(), 4)

    def test_u16_be(self):
        b = binfile.BinFile(self.tempfile_, little=False)
        self.assertEqual(b.read_u16(), 33384)
        self.assertEqual(b.read_u16(), 25856)
        self.assertEqual(self.tempfile_.tell(), 4)

    def test_s16_le(self):
        b = binfile.BinFile(self.tempfile_, little=True)
        self.assertEqual(b.read_s16(), 26754)
        self.assertEqual(b.read_s16(), 101)
        self.assertEqual(self.tempfile_.tell(), 4)

    def test_s16_be(self):
        b = binfile.BinFile(self.tempfile_, little=False)
        self.assertEqual(b.read_s16(), -32152)
        self.assertEqual(b.read_s16(), 25856)
        self.assertEqual(self.tempfile_.tell(), 4)

    def test_u32_le(self):
        b = binfile.BinFile(self.tempfile_, little=True)
        self.assertEqual(b.read_u32(), 6645890)
        self.assertEqual(b.read_u32(), 544173164)
        self.assertEqual(self.tempfile_.tell(), 8)

    def test_u32_be(self):
        b = binfile.BinFile(self.tempfile_, little=False)
        self.assertEqual(b.read_u32(), 2187879680)
        self.assertEqual(b.read_u32(), 1819045664)
        self.assertEqual(self.tempfile_.tell(), 8)

    def test_s32_le(self):
        b = binfile.BinFile(self.tempfile_, little=True)
        self.assertEqual(b.read_s32(), 6645890)
        self.assertEqual(b.read_s32(), 544173164)
        self.assertEqual(self.tempfile_.tell(), 8)

    def test_s32_be(self):
        b = binfile.BinFile(self.tempfile_, little=False)
        self.assertEqual(b.read_s32(), -2107087616)
        self.assertEqual(b.read_s32(), 1819045664)
        self.assertEqual(self.tempfile_.tell(), 8)

    def test_u64_le(self):
        b = binfile.BinFile(self.tempfile_, little=True)
        self.assertEqual(b.read_u64(), 2337205942747490434)
        self.assertEqual(self.tempfile_.tell(), 8)

    def test_u64_be(self):
        b = binfile.BinFile(self.tempfile_, little=False)
        self.assertEqual(b.read_u64(), 9396871675001990944)
        self.assertEqual(self.tempfile_.tell(), 8)

    def test_s64_le(self):
        b = binfile.BinFile(self.tempfile_, little=True)
        self.assertEqual(b.read_s64(), 2337205942747490434)
        self.assertEqual(self.tempfile_.tell(), 8)

    def test_s64_be(self):
        b = binfile.BinFile(self.tempfile_, little=False)
        self.assertEqual(b.read_s64(), -9049872398707560672)
        self.assertEqual(self.tempfile_.tell(), 8)

    def test_float_le(self):
        b = binfile.BinFile(self.tempfile_, little=True)
        self.assertAlmostEqual(b.read_float(), 9.312875451071659e-39)
        self.assertEqual(self.tempfile_.tell(), 4)

    def test_float_be(self):
        b = binfile.BinFile(self.tempfile_, little=False)
        self.assertAlmostEqual(b.read_float(), -1.7073653665398035e-37)
        self.assertEqual(self.tempfile_.tell(), 4)

    def test_double_le(self):
        b = binfile.BinFile(self.tempfile_, little=True)
        self.assertAlmostEqual(b.read_double(), 1.874938730448489e-152)
        self.assertEqual(self.tempfile_.tell(), 8)

    def test_double_be(self):
        b = binfile.BinFile(self.tempfile_, little=False)
        self.assertAlmostEqual(b.read_double(), -4.662586273244399e-297)
        self.assertEqual(self.tempfile_.tell(), 8)

    def test_ascii(self):
        b = binfile.BinFile(self.tempfile_)
        self.tempfile_.seek(4)
        self.assertEqual(b.read_ascii(5), "llo w")
        self.assertEqual(self.tempfile_.tell(), 9)

    def test_asciiz(self):
        b = binfile.BinFile(self.tempfile_)
        self.tempfile_.seek(1)
        self.assertEqual(b.read_asciiz(), "he")
        self.assertEqual(self.tempfile_.tell(), 4)
        self.assertEqual(b.read_asciiz(), "llo world")
        self.assertEqual(self.tempfile_.tell(), 14)


if __name__ == "__main__":
    unittest.main()
