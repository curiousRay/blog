==============
LaTeX踩坑笔记
==============

正确渲染汉字
-------------

在文档头部加入以下控制序列：

.. code-block:: latex

    \documentclass[12pt, a4paper]{ctexart}

插入MATLAB代码块
-----------------

将 `mcode.sty <https://github.com/nasa/nasa-latex-docs/blob/master/support/packages/mcode/mcode.sty>`_ 文件置于文档根目录，再通过 ``\usepackage{mcode}`` 调用。

将section的标题由默认的居中改为左对齐
--------------------------------------

.. code-block:: latex

    \CTEXsetup[format={\Large\bfseries}]{section}

将section的序号设置为从0开始而不是1
-------------------------------------

.. code-block:: latex

    \setcounter{section}{-1}

插入矩阵
----------

.. code-block:: latex

    \usepackage{amsmath}
    $$
      \begin{matrix}
        A & B \\
        C & D
      \end{matrix}
     $$

将 ``matrix`` 替换为 ``bmatrix`` 可为矩阵加中括号；替换为 ``pmatrix`` 可加小括号。

插入来自MATLAB的图片
--------------------

1. MATLAB将图片保存为eps格式。

2. 在文档头部加入：

.. code-block:: latex

    \usepackage{graphicx}
    \usepackage{epstopdf}
    \usepackage{float}

3. 在需要插入图片的地方加入:

.. code-block:: latex

  \begin{figure}[H]
    %H表示将图形放置在文中给出该图形环境的地方，如果塞不下就自动放置在下一页顶部。
    \centering
    \includegraphics[height=2cm,width=3cm]{path/to/fig.eps}
    %中括号及其中的内容可省略
    \caption{这是图片的描述}
    \label{1}
  \end{figure}

4. 其实还有更简单的方法：仅在文档开头 ``\usepackage{graphicx}`` ，在想要插入图片的地方 ``\includegraphics{...}``，但是这种方法不支持插入caption。虽然可以在图片下方手动添加一行作为图片描述，但对于强迫症患者不友好。

调节页边距
----------

.. code-block:: latex

  \usepackage{geometry}
  \geometry{left=3.18cm,right=3.18cm,top=3.18cm,bottom=3.18cm}
  %A4纸页边距默认为3.18cm（上下左右都相等）

