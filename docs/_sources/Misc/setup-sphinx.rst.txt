.. |location_link| raw:: html

=======================
Sphinx文档框架搭建速记
=======================

本文是利用 `Sphinx <https://www.sphinx-doc.org/en/master/>`_ 建立文档框架的过程记录，使用了 `Github pages <https://pages.github.com/>`_ 提供的静态托管服务。

安装
-----

Github新建名为 ``blog`` 的项目（名字可任意）。

本地创建Python项目，搭建虚拟环境。

执行安装：

.. code-block:: sh

    pip install -U sphinx
    sphinx-quickstart

注意选择分离 :guilabel:`source` 和 :guilabel:`build` 文件夹的选项（输入Y并回车）。

构建
-----

本地建立Git仓库，添加适用于Python开发环境的 :guilabel:`.gitignore` 文件（需要注释其中的 :guilabel:`build` 文件夹）。

本地项目根目录下新建 :guilabel:`docs` 文件夹。

在 :guilabel:`make.bat` 脚本中添加 ``xcopy /y %BUILDDIR%\html\* %BUILDDIR%\..\docs /e``。此命令在执行构建指令后将生成的静态文件复制到 :guilabel:`docs` 文件夹，以供Github pages服务使用。

执行构建指令 ``make html`` ，即可在 :guilabel:`build\\html` 中找到生成的静态文件。

将本地项目push至Github。

在GitHub repo设置的pages选项处将source改为“master branch /docs folder”，即可在 ``https://username.github.io/blog`` 浏览。

自定义顶级域名
--------------

DNS服务添加A记录，记录名为 ``@`` ，记录值为以下四者任选其一：

.. parsed-literal::

    185.199.108.153
    185.199.109.153
    185.199.110.153
    185.199.111.153

本地项目的 :guilabel:`docs` 文件夹里新建名为 :guilabel:`CNAME` 的文件，内容为顶级域名。

同时以及新建一个空的 :guilabel:`.nojekyll` 文件，并push到GitHub。

.. Tip:: 这样做的原因是Github pages对jekyll框架的处理机制会排除 :guilabel:`_static` 文件夹。而我们的静态js和css等文件正是存在于此。排除它们的后果是加载非HTML文档时会报 ``404 ERR_ABORTED`` [#]_。

Github项目设置的pages选项勾选Force https，稍候即可实现http自动跳转至https。

定制
-----

自定义404页面
^^^^^^^^^^^^^

静态文件根目录手动建立 :guilabel:`404.html` 文件，在文件的最前面加上front matter后push即可 [#]_。

.. code-block:: yaml

    ---
    permalink: /404.html
    ---

安装主题
^^^^^^^^
以 `Read the Docs <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`_ 主题为例，按照 https://github.com/readthedocs/sphinx_rtd_theme 执行即可。

从外部来源加载MathJax
^^^^^^^^^^^^^^^^^^^^^

在插件列表中添加 `MathJax <https://www.mathjax.org/>`_ 并设置url。请注意其后所带的参数。

.. code-block:: python

    # file: source/conf.py
    extensions = [
        ...
        "sphinx.ext.mathjax",
    ]
    mathjax_path = 'https://cdn.bootcss.com/mathjax/2.7.6/MathJax.js?config=TeX-AMS-MML_HTMLorMML'

设置代码高亮配色
^^^^^^^^^^^^^^^

Sphinx使用 `Pygments <http://pygments.org/>`_ 作为默认高亮工具。

.. code-block:: python

    # file: source/conf.py
    pygments_style = 'trac'

其中自带样式列表可在 **Python命令行** 中执行如下代码查看

.. code-block:: python

    from pygments.styles import get_all_styles
    print(list(get_all_styles()))

添加自定义CSS [#]_
^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # file: source/conf.py
    def setup(app):
    app.add_stylesheet('style.css')

其中 :guilabel:`style.css` 位于 :guilabel:`source\\_static`。

设置favicon
^^^^^^^^^^^^^

.. code-block:: python

    # file: source/conf.py
    html_favicon = 'favicon.ico'

其中 :guilabel:`favicon.ico` 位于 :guilabel:`source` [#]_。

References
-----------

.. [#] https://github.blog/2009-12-29-bypassing-jekyll-on-github-pages/
.. [#] https://help.github.com/cn/articles/creating-a-custom-404-page-for-your-github-pages-site
.. [#] https://github.com/sphinxjp/sphinx-users.jp/blob/master/source/conf.py#L213
.. [#] https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_favicon