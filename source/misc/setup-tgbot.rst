=========================
Telegram bot 开发环境搭建
=========================

本文总结了搭建Bot开发环境的基本步骤。在CentOS 7系统中使用 `python-telegram-bot <https://github.com/python-telegram-bot/python-telegram-bot>`_ 框架。

在获得自己的Bot的TOKEN后，我们需要打开服务器的外网 **443** 端口以保证数据收发正常进行。

获取python-setuptools
------------------------

.. code-block:: sh

    yum install git python-setuptools -y
    git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive

安装Python虚拟环境virtualenv
------------------------------

让bot运行在虚拟环境中能保证不与将来执行的其他脚本发生冲突。

.. code-block:: sh

    # 安装epel扩展源
    sudo yum -y install epel-release

    # 安装python-pip
    sudo yum -y install python-pip
    sudo yum clean all
    pip install --upgrade pip

    # 安装虚拟环境
    pip install virtualenv


进入到想存放虚拟环境的目录，执行：

.. code-block:: sh

    virtualenv myEnvName

这样就创建了一个名为 ``myEnvName`` 的虚拟环境，在当前目录下会生成同名的文件夹。

使用screen来保证进程常驻
-------------------------

当远程连接的会话窗口被关闭时，发送 ``logout`` 命令会导致bot的进程被杀掉。因此可以通过screen工具保留一个shell会话。

.. code-block:: sh

    # 安装screen工具
    yum install screen -y

    # 新建屏幕
    screen

开始使用框架
-------------

.. code-block:: sh

    # 激活先前创建的虚拟环境
    cd myEnvName
    source bin/activate

    # 安装python-telegram-bot框架
    cd python-telegram-bot
    python setup.py install


* 配置python程序中的TOKEN。

* 在存放程序的目录中运行：

.. code-block:: sh

   python yourScript.py &

这里的符号 ``&`` 表明程序在后台执行。查看进程显示如图（用root用户操作是不合适的行为，请引以为戒~

.. figure:: https://cdn.raysky.net/p/tgbot-setup1.png
   :align: center

其中的 ``8252`` 是python后台进程。此时我们可以安心地执行 ``deactivate`` 以退出虚拟环境，而后台进程可以一直运行。

* 输入 ``screen -ls`` ，显示窗口状态如图，数字为session id。

.. figure:: https://cdn.raysky.net/p/tgbot-setup2.png
   :align: center

* 输入 ``screen -d session_id`` 以detach窗口。

此时可放心关闭终端程序。

下次登录后只需要输入 ``screen -d session_id`` 即可重新连接到窗口。

其它
--------

.. code-block:: sh

    # kill任意进程
    kill -s 9 _pid_

    # 退出会话窗口，关闭Bot
    screen -X -S session_id quit
