=======
BinFile
=======

A simple Python module for reading and writing "normal" datatypes (such as
``U8``, ``S64``, null terminated strings etc.) from or to a file.

Install
-------

.. code-block:: bash

    pip install git+git://github.com/mheden/BinFile


Example
-------

.. code-block:: python
    from binfile import BinFile

    filename = 'file.bin'
    with open(filename, mode='wb') as f:
        bf = BinFile(f)
        bf.write_u8(77)
        bf.write_u16(1234)
        bf.write_s64(-56487132)
        bf.write_asciiz("hello world")
        bf.write_s16(-5678)

    with open(filename, mode='rb') as f:
        bf = BinFile(f)
        print(bf.read_u8())
        print(bf.read_u16())
        print(bf.read_s64())
        print(bf.read_asciiz())
        print(bf.read_s16())


Run unittest
------------

.. code-block:: bash

    python -m unittest
