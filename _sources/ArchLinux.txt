ArchLinux安装与配置
===================

.. toctree::
    
    

中文化
------

字体
~~~~

字体其实挺简单，把wqy相关的字体都装上，效果已经差不多了，不满意的话，慢慢调吧。


fcitx输入法安装与配置
~~~~~~~~~~~~~~~~~~~~

#. fcitx下要安装fcitx-gtk2等与界面相关的包，才可以在相应的界面下输入。
#. fcitx如果是用GDM、KDM等登录，需要修改 ``~/.xprofile`` 文件才可以正常使用：

.. code-block:: sh
    :linenos:
    
    export GTK_IM_MODULE=fcitx
    export QT_IM_MODULE=fcitx
    export XMODIFIERS="@im=fcitx"

在字符终端下显示中文
~~~~~~~~~~~~~~~~~~~~

异常简单，只需要安装 ``fbterm`` 即可。


系统管理
---------

网络的安装与配置
~~~~~~~~~~~~~~~~

一般情况下网卡都能够自动安装，并且如果是DHCP的话，基本不用配置自动就可以连网。
如果没有相关的驱动可能要自己找一些驱动了。对于无线网在控制台下用要安装wifi-menu
依赖的dialog等库。在图形界面下用的话，要安装networkmanager以有相应的applet，然
后将本地用户加入到networkmanager组中，用 ``system enable NetworkManage`` 自启动
相关的服务。

系统服务
~~~~~~~~

系统服务可以用 ``systemctl`` 来进行管理，系统服务开启用命令： ``systemctl
enable <servicename>`` ，系统服务启动用 ``systemctl start <servicename>`` 。

移动存储自动挂载、光驱使用等
~~~~~~~~~~~~~~~~~~~~~~~~~~~

udev目前是linux内核的设备管理器，包括对硬件的自动检测和热插拨设备的管理等。udev
的使用靠的是一堆rules，在/etc/udev/rules.d目录下，但是archlinux默认的情况下这些
rules都没有自动写上。系统的rules存储在/usr/lib/udev/rules.d目录下，最懒的办法，
把此目录下的东西都链接到/etc/udev/rules.d目录下即可。

此外，要使用移动存储设备，还需要安装udisks、udiskie、udisks2几个包。udisks2是
udisks的升级版，但是目录一些文件管理器还不支持，比如lxde所用的pcmanfm。

最后记得要把用户加入到storage组中。

postgresql
----------

postgresql 安装后要对进行数据库的初始化，否则数据库服务启动不起来，运行：

.. code-block:: sh

    sudo -u postgres initdb --locale=en_US.UTF-8 -D /var/lib/postgresql/data
    
然后便可以用 ``systemctl enable postgresql`` 将系统服务自动启动。

