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

让bot运行在虚拟环境中能保证不与将来执行的其他脚本发生冲突。首先需要安装**python-pip**

.. code-block:: sh

    # 安装epel扩展源
    sudo yum -y install epel-release

    # 安装python-pip
    sudo yum -y install python-pip
    sudo yum clean all
    pip install --upgrade pip

    # 安装虚拟环境
    pip install virtualenv


进入到想存放虚拟环境的目录，执行

.. code-block:: sh

    virtualenv myEnvName

这样就创建了一个名为 ``myEnvName`` 的虚拟环境，在当前目录下会生成同名的文件夹。

使用screen来保证进程常驻
-------------------------

当远程连接的会话窗口被关闭时，发送 ``logout`` 命令会导致bot的进程被杀掉。因此可以通过screen工具保留一个shell会话。

* 安装screen：
<pre><code class="bash">yum install screen -y
</code></pre>
输入`screen`以新建窗口，在这个窗口中我们继续进行操作。

开始使用框架
-------------

* 激活先前创建的虚拟环境：
<pre><code class="bash">cd myEnvName
source bin/activate
</code></pre>

* 安装python-telegram-bot框架：
<pre><code class="bash">cd python-telegram-bot
python setup.py install
</code></pre>

* 修改python机器人程序中的TOKEN为自己的字符串，就像：`123456789:AAGEbvjSadJcs_zFIPKnWqsPtSus_8zGHn0`（示例）

* 在存放程序的目录中运行：
<pre><code class="bash">python yourScript.py &</code></pre>

这里的符号`&`表明程序在后台执行，这样执行后我们可以继续输入其他指令。此时显示如图

<span class="image main">![tupian](https://cdn.raysky.net/p/tgbot-setup1.png)</span>

其中的`8252`是python后台进程。如果需要的话可以`kill`。此时我们可以安心地执行`deactivate`以退出虚拟环境，而后台进程可以一直运行。

* 输入 `screen -ls`，显示窗口状态如图，数字为session id。

<span class="image main">![tupian](https://cdn.raysky.net/p/tgbot-setup2.png)</span>

* 输入 `screen -d session_id`以detach窗口

此时可放心关闭终端程序。

下次登录后，如果想要回到原来的窗口，只需要输入`screen -d session_id`，重新连接到窗口。

其它
--------
* 有时在执行Bot的python脚本时会出现以下错误

`6 - __main__ - WARNING - Update \"None\" caused error \"Conflict: terminated by other long poll or webhook (409)\"`

只需查看python的pid，kill之后重试就行了。

* 如何kill进程？
`kill -s 9 _pid_`

* 想要关闭Bot？
输入：`screen -X -S session_id quit`删除会话窗口，也就意味着关闭Bot。
