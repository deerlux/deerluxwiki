reStructedText 学习笔记
=======================

.. toctree::
    :maxdepth: 2

``toctree`` 定义目录结构
------------------------

``toctree`` 用来定义文档的结构， ``toctree`` 下空一行，后面的内容缩进，sphinx
系统会自动查找目录结构下对应的 ``xx.rst`` 文档作为此文档的一部分进行生成。

.. code-block:: rst
    :linenos:

    .. toctree::
        :maxdepth: 2

        content1
        content2

上述目录的定义，在生成的时候会自动找 ``content1`` 和 ``content2`` 对应的RST文件
。


代码高亮
--------

可以用 ``.. code-block:: python`` 来指定后续的代码块用python的语法进行高亮显示
（当然也可以是别的语言）。此外，在code-block指令下添加 ``:linenos:`` 用以指定显
示行号。

.. code-block:: rst
    :linenos:

    .. code-block:: python
        :linenos:

        def some_function():
            print("hello, world!")
            print("Hello, deerlux!")

上述代码的显示效果：

.. code-block:: python
    :linenos:
    :emphasize-lines: 2

     def some_function():
        print("hello, world!")
        print("Hello, deerlux!")

.. literalinclude:: test.py
    :language: python
    :linenos:
    :emphasize-lines: 3,4

