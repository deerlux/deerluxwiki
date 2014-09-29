git用法笔记
=========================

GIT stash命令的用法
--------------------
``git stash`` 用于将当前的修改暂存，主要应用在当你pull一些修改的时候，有些合并
工作可能会比较麻烦，暂时先不处理，后续再处理，然后过后便可以用 ``git stash
pop`` 命令将当时stash起来的东西再pop出来以便于进行合并处理。

.gitconfig 的一些有用的设置
------------------------------
.. code-block:: ini

    [user]
        email = deerlux@gmail.com
        username = deerlux
    [color]
        ui = true
    [alias]
        ci = commit
        co = checkout
        st = status
        br = branch

第一段是定义的用户一些基本信息，第二段设置了GIT的UI color后，输出的结果将更好看
。第三段定义了一些常用的 alias。


