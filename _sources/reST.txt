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
