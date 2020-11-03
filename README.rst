=================
LindenmayerSystem
=================

A simple Python module for generating Lindenmayer Systems.

Install
-------

.. code-block:: bash

    pip install git+git://github.com/mheden/LindenmayerSystem


Operations
----------

+-----------+------------+----------------------------------------------------+
| operation | symbols    | description                                        |
+===========+============+====================================================+
| draw      | ``[ABFG]`` | Move forward by line length drawing a line         |
+-----------+------------+----------------------------------------------------+
| move      | ``[abfg]`` | Move forward by line length without drawing a line |
+-----------+------------+----------------------------------------------------+
| turnleft  | ``-``      | Turn left by turning angle                         |
+-----------+------------+----------------------------------------------------+
| turnright | ``+``      | Turn right by turning angle                        |
+-----------+------------+----------------------------------------------------+
| push      | ``[``      | Push current drawing state onto stack              |
+-----------+------------+----------------------------------------------------+
| pop       | ``]``      | Pop current drawing state from the stack           |
+-----------+------------+----------------------------------------------------+


Example
-------

.. literalinclude:: example.py
  :language: python


References
----------

- https://en.wikipedia.org/wiki/L-system
