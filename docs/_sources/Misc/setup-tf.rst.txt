======================
Windows搭建tf2.0环境
======================

软硬件配置
-----------

- Python 3.7
- Nvidia GTX950m，驱动程序版本441.22

搭建过程
-----------

1. Pycharm创建项目，配置好虚拟环境。

2. 参照以下链接安装gpu版本的tf而非cpu版本的。执行 ``pip install tensorflow-gpu``

3. 仔细阅读 https://tensorflow.google.cn/install/gpu#software_requirements 标明的安装需求。如本文撰写时要求的CUDA版本为10.0，而英伟达官网最新版本为10.2。需要按tf标明版本来下载。

4. 安装CUDA，尽量装在C盘。

5. 下载cudnn [#]_ 。此模块是必须的，但不用安装，可存放在任意目录下。将其地址加到 :guilabel:`环境变量→系统变量→path` 中即可。

6. 编辑path如下。

.. figure:: https://cdn.raysky.net/p/setup-tf1.png
   :align: center

7. 可以执行 ``pip install —upgrade tensorflow`` 更新一下。

FAQ
----------

1. 提示找不到 :guilabel:`cudart64_100.dll`

    CUDA必须为10.0版本，且正确设置了环境变量。正确设置后应有如下输出：

.. figure:: https://cdn.raysky.net/p/setup-tf2.png
   :align: center

2. Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2是什么意思

    AVX2需要通过编译安装才能使用。它可以提高代码编译性能，但也可不用。忽略即可。

3. 输出栏有太多的红色字体信息

    tensorflow的log输出是红色的。可以修改代码文件，将无用的信息滤除。见下文示例代码的注释。

4. 找不到类的某个属性。如报错：

.. code-block::

    module 'tensorflow' has no attribute 'placeholder'

原因：旧版数据结构的锅。tensorflow 1.x与2.0版本差异过大，兼容性差。不过有迁移工具可将旧版代码转换为新版代码。可参考：

Example
----------------

.. code-block:: python

    from __future__ import absolute_import, division, print_function

    # 忽略警告
    import os
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    import tensorflow as tf
    import numpy as np

    # 输入的摄氏温度以及其对应的华氏温度，前面两个故意写错了
    celsius_q = np.array([-40, -10,  0,  8, 15, 22,  38],  dtype=float)
    fahrenheit_a = np.array([-40,  14, 32, 46, 59, 72, 100],  dtype=float)
    for i,c in enumerate(celsius_q):
        print("{} degrees Celsius = {} degrees Fahrenheit".format(c, fahrenheit_a[i]))

    # 输入后连接了只有一个神经单元的隐藏层
    l0 = tf.keras.layers.Dense(units=1, input_shape=[1])

    # 将网络层添加到序列模型中
    model = tf.keras.Sequential([l0])

    # 编译神经网络模型
    model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))

    # 训练模型
    history = model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)
    print("Finished training the model")

References
----------------

.. [#] https://developer.nvidia.com/cudnn
.. [#] https://cloud.tencent.com/developer/article/1519704