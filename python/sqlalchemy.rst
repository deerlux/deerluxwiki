python sqlalchemy的简单用法
===========================

deerlux@163.com 

2014年 10月 07日 星期二 21:56:41 CST

说实在的，至今我还没有完全理解sqlalchemy的设计思想，前几天想自己在网上抓些东西
然后存放在数据库中以便于后续的数据分析，只是不想自己用DB-API写SQL语句去操作数据
库，所以才想用ORM的方式，可是看了半天sqlalchemy的文档，都是在讲如何进行建库、建
关系等，可是问题是我们经常要操作的数据库，库表的建立并不是通过ORM的方式建，更希
望是通过原始的SQL语句去建，这种情况下有没有一种更方便的方式去访问数据库？答案当
然是肯定的。

比如我用来抓取基金数据的库中包含两个表：

.. literalinclude:: funds_value.sql
    :language: sql
    :linenos:

用来访问这两个表其实只需要简单构建两个类即可：

.. literalinclude:: test_sqlalchemy.py
    :language: pythona
    :linenos:


简单定义了两个类之后，不用关心数据表的内部实现，sqlalchemy会实现自动的映射，随
后手册上的很多操作都可以正常使用了。

