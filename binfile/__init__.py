from functools import partialmethod
import struct


class BinFile(object):

    _conv = {
        "u8": ("B", 1),
        "u16": ("H", 2),
        "u32": ("L", 4),
        "u64": ("Q", 8),
        "s8": ("b", 1),
        "s16": ("h", 2),
        "s32": ("l", 4),
        "s64": ("q", 8),
        "float": ("f", 4),
        "double": ("d", 8),
    }

    def __init__(self, fd, little=True):
        self._fd = fd
        if little:
            self._endian = "<"
        else:
            self._endian = ">"

    def _read(self, type_, length):
        fmt = "%s%s" % (self._endian, type_)
        return struct.unpack(fmt, self._fd.read(length))[0]

    def _write(self, type_, length, data):
        fmt = "%s%s" % (self._endian, type_)
        print("_write(%d) => %s" % (data, struct.pack(fmt, data)))
        self._fd.write(struct.pack(fmt, data))

    read_u8 = partialmethod(_read, *_conv["u8"])
    read_u16 = partialmethod(_read, *_conv["u16"])
    read_u32 = partialmethod(_read, *_conv["u32"])
    read_u64 = partialmethod(_read, *_conv["u64"])
    read_s8 = partialmethod(_read, *_conv["s8"])
    read_s16 = partialmethod(_read, *_conv["s16"])
    read_s32 = partialmethod(_read, *_conv["s32"])
    read_s64 = partialmethod(_read, *_conv["s64"])
    read_float = partialmethod(_read, *_conv["float"])
    read_double = partialmethod(_read, *_conv["double"])

    write_u8 = partialmethod(_write, *_conv["u8"])
    write_u16 = partialmethod(_write, *_conv["u16"])
    write_u32 = partialmethod(_write, *_conv["u32"])
    write_u64 = partialmethod(_write, *_conv["u64"])
    write_s8 = partialmethod(_write, *_conv["s8"])
    write_s16 = partialmethod(_write, *_conv["s16"])
    write_s32 = partialmethod(_write, *_conv["s32"])
    write_s64 = partialmethod(_write, *_conv["s64"])
    write_float = partialmethod(_write, *_conv["float"])
    write_double = partialmethod(_write, *_conv["double"])

    def read_ascii(self, length):
        fmt = "%ds" % length
        s = struct.unpack(fmt, self._fd.read(length))[0]
        s = s.partition(b"\0")[0]  # remove tailing NULL(s)
        return s.decode("ascii")

    def read_asciiz(self):
        s = b""
        while True:
            chr_ = struct.unpack("s", self._fd.read(1))[0]
            if chr_ == b"\x00":
                break
            s += chr_
        return s.decode("ascii")

    def read(self, length):
        return self._fd.read(length)

    def write(self, data):
        return self._fd.write(data)
