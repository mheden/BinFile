import contextlib
import os
import tempfile
import unittest
import binfile


class TestRead(unittest.TestCase):

    fd = None

    def setUp(self):
        self.fd = tempfile.TemporaryFile(mode="w+b")
        self.fd.write(
            bytes([130, 104, 101, 0, 108, 108, 111, 32, 119, 111, 114, 108, 100, 0])
        )
        self.fd.seek(0)

    def tearDown(self):
        self.fd.close()
        self.fd = None

    def test_u8(self):
        bf = binfile.BinFile(self.fd)
        self.assertEqual(bf.read_u8(), 130)
        self.assertEqual(bf.read_u8(), 104)
        self.assertEqual(bf.read_u8(), 101)
        self.assertEqual(bf.read_u8(), 0)
        self.assertEqual(self.fd.tell(), 4)

    def test_s8(self):
        bf = binfile.BinFile(self.fd)
        self.assertEqual(bf.read_s8(), -126)
        self.assertEqual(bf.read_s8(), 104)
        self.assertEqual(bf.read_s8(), 101)
        self.assertEqual(bf.read_s8(), 0)
        self.assertEqual(self.fd.tell(), 4)

    def test_u16_le(self):
        bf = binfile.BinFile(self.fd, little=True)
        self.assertEqual(bf.read_u16(), 26754)
        self.assertEqual(bf.read_u16(), 101)
        self.assertEqual(self.fd.tell(), 4)

    def test_u16_be(self):
        bf = binfile.BinFile(self.fd, little=False)
        self.assertEqual(bf.read_u16(), 33384)
        self.assertEqual(bf.read_u16(), 25856)
        self.assertEqual(self.fd.tell(), 4)

    def test_s16_le(self):
        bf = binfile.BinFile(self.fd, little=True)
        self.assertEqual(bf.read_s16(), 26754)
        self.assertEqual(bf.read_s16(), 101)
        self.assertEqual(self.fd.tell(), 4)

    def test_s16_be(self):
        bf = binfile.BinFile(self.fd, little=False)
        self.assertEqual(bf.read_s16(), -32152)
        self.assertEqual(bf.read_s16(), 25856)
        self.assertEqual(self.fd.tell(), 4)

    def test_u32_le(self):
        bf = binfile.BinFile(self.fd, little=True)
        self.assertEqual(bf.read_u32(), 6645890)
        self.assertEqual(bf.read_u32(), 544173164)
        self.assertEqual(self.fd.tell(), 8)

    def test_u32_be(self):
        bf = binfile.BinFile(self.fd, little=False)
        self.assertEqual(bf.read_u32(), 2187879680)
        self.assertEqual(bf.read_u32(), 1819045664)
        self.assertEqual(self.fd.tell(), 8)

    def test_s32_le(self):
        bf = binfile.BinFile(self.fd, little=True)
        self.assertEqual(bf.read_s32(), 6645890)
        self.assertEqual(bf.read_s32(), 544173164)
        self.assertEqual(self.fd.tell(), 8)

    def test_s32_be(self):
        bf = binfile.BinFile(self.fd, little=False)
        self.assertEqual(bf.read_s32(), -2107087616)
        self.assertEqual(bf.read_s32(), 1819045664)
        self.assertEqual(self.fd.tell(), 8)

    def test_u64_le(self):
        bf = binfile.BinFile(self.fd, little=True)
        self.assertEqual(bf.read_u64(), 2337205942747490434)
        self.assertEqual(self.fd.tell(), 8)

    def test_u64_be(self):
        bf = binfile.BinFile(self.fd, little=False)
        self.assertEqual(bf.read_u64(), 9396871675001990944)
        self.assertEqual(self.fd.tell(), 8)

    def test_s64_le(self):
        bf = binfile.BinFile(self.fd, little=True)
        self.assertEqual(bf.read_s64(), 2337205942747490434)
        self.assertEqual(self.fd.tell(), 8)

    def test_s64_be(self):
        bf = binfile.BinFile(self.fd, little=False)
        self.assertEqual(bf.read_s64(), -9049872398707560672)
        self.assertEqual(self.fd.tell(), 8)

    def test_float_le(self):
        bf = binfile.BinFile(self.fd, little=True)
        self.assertAlmostEqual(bf.read_float(), 9.312875451071659e-39)
        self.assertEqual(self.fd.tell(), 4)

    def test_float_be(self):
        bf = binfile.BinFile(self.fd, little=False)
        self.assertAlmostEqual(bf.read_float(), -1.7073653665398035e-37)
        self.assertEqual(self.fd.tell(), 4)

    def test_double_le(self):
        bf = binfile.BinFile(self.fd, little=True)
        self.assertAlmostEqual(bf.read_double(), 1.874938730448489e-152)
        self.assertEqual(self.fd.tell(), 8)

    def test_double_be(self):
        bf = binfile.BinFile(self.fd, little=False)
        self.assertAlmostEqual(bf.read_double(), -4.662586273244399e-297)
        self.assertEqual(self.fd.tell(), 8)

    def test_ascii(self):
        bf = binfile.BinFile(self.fd)
        self.fd.seek(4)
        self.assertEqual(bf.read_ascii(5), "llo w")
        self.assertEqual(self.fd.tell(), 9)

    def test_ascii_with_null(self):
        bf = binfile.BinFile(self.fd)
        self.fd.seek(1)
        self.assertEqual(bf.read_ascii(8), "he\0llo w")
        self.assertEqual(self.fd.tell(), 9)

    def test_asciiz(self):
        bf = binfile.BinFile(self.fd)
        self.fd.seek(1)
        self.assertEqual(bf.read_asciiz(), "he")
        self.assertEqual(self.fd.tell(), 4)
        self.assertEqual(bf.read_asciiz(), "llo world")
        self.assertEqual(self.fd.tell(), 14)


class TestReadWrite(unittest.TestCase):

    filename = "__test_mixed__.bin"

    def tearDown(self):
        with contextlib.suppress(FileNotFoundError):
            os.remove(self.filename)

    def test_mixed(self):
        data = [77, 1234, -5648715644887832, "hello world", -5678]
        with open(self.filename, mode="wb") as f:
            bf = binfile.BinFile(f)
            bf.write_u8(data[0])
            bf.write_u16(data[1])
            bf.write_s64(data[2])
            bf.write_asciiz(data[3])
            bf.write_s16(data[4])

        with open(self.filename, mode="rb") as f:
            bf = binfile.BinFile(f)
            self.assertEqual(bf.read_u8(), data[0])
            self.assertEqual(bf.read_u16(), data[1])
            self.assertEqual(bf.read_s64(), data[2])
            self.assertEqual(bf.read_asciiz(), data[3])
            self.assertEqual(bf.read_s16(), data[4])


class TestSkip(unittest.TestCase):

    tmpfile_ = None

    def setUp(self):
        self.fd = tempfile.TemporaryFile(mode="w+b")
        self.fd.write(
            bytes([130, 104, 101, 0, 108, 108, 111, 32, 119, 111, 114, 108, 100, 0])
        )
        self.fd.seek(0)

    def tearDown(self):
        self.fd.close()
        self.fd = None

    def test_skip(self):
        bf = binfile.BinFile(self.fd)
        self.assertEqual(bf.read_u8(), 130)
        self.assertEqual(self.fd.tell(), 1)
        bf.skip(5)
        self.assertEqual(self.fd.tell(), 6)
        self.assertEqual(bf.read_u8(), 111)


class TestException(unittest.TestCase):
    def test_exception(self):
        try:
            binfile.BinFile(None)
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
