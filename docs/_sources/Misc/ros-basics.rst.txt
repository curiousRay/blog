===============
ROS编程基础操作
===============

本文描述了在Ubuntu 16.04环境下，使用ROS [#]_ 进行 ~~SLAM数据采集与显示~~的过程。

搭建安装环境
-------------

配置Ubuntu软件库
^^^^^^^^^^^^^^^^^

确保 ``restricted`` 、 ``universe`` 和 ``multiverse`` 的选项被勾选。

.. figure:: https://cdn.raysky.net/p/ros-1st-time1.PNG
   :align: center

执行安装
^^^^^^^^^

.. code-block:: sh

    # 更换镜像源
    sudo sh -c '. /etc/lsb-release
    echo "deb http://mirrors.ustc.edu.cn/ros/ubuntu/ $DISTRIB_CODENAME main" > /etc/apt/sources.list.d/ros-latest.list'

    # 添加密钥
    sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 0xB01FA116

    # 执行安装
    sudo apt-get update
    sudo apt-get install ros-kinetic-desktop-full
    sudo rosdep init
    sudo rosdep update
    echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
    source ~/.bashrc
    sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential

    # 检查是否将环境变量加入.bashrc
    printenv | grep ROS

创建ROS工作空间
^^^^^^^^^^^^^^^^^

.. code-block:: sh

    mkdir -p ~/catkin_ws/src
    cd ~/catkin_ws/
    catkin_make

进行简单的测试
----------------

配置环境变量
^^^^^^^^^^^^

执行 ``roscore`` 若提示无权限

.. figure:: https://cdn.raysky.net/p/ros-1st-time2.PNG
   :align: center

则执行 [#]_：

.. code-block:: sh

    sudo rosdep fix-permissions

显示如图

.. figure:: https://cdn.raysky.net/p/ros-1st-time3.PNG
   :align: center

.. code-block:: sh

    sudo rosdep fix-permissions
    cd ~/catkin_ws/
    source devel/setup.bash

执行 ``echo $ROS_PACKAGE_PATH`` 应能显示出一个路径，如：

.. code-block:: sh

    /home/ray/Desktop/catkin_ws/src:/opt/ros/kinetic/share

运行示例程序
^^^^^^^^^^^^

加载ROS核心

.. figure:: https://cdn.raysky.net/p/ros-1st-time4.PNG
   :align: center

新建新终端窗口，启动 **turtlesim** 包的 **turtlesim_node节点**。

.. code-block:: sh

    rosrun turtlesim turtlesim_node

新建新终端窗口，通过键盘控制海龟运动。此窗口必须拥有焦点，键盘控制才能生效。

.. code-block:: sh

    rosrun turtlesim turtle_teleop_key

.. figure:: https://cdn.raysky.net/p/ros-1st-time5.PNG
   :align: center

使用rqt插件查看消息传输关系
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

    # 执行安装
    sudo apt-get install ros-kinetic-rqt
    sudo apt-get install ros-kinetic-rqt-common-plugins

    # 在示例程序运行的同时，新建窗口执行
    rosrun rqt_graph rqt_graph

使用C++编写简单的功能包
------------------------

环境设置与创建功能包
^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

    mkdir -p catkin_ws/src
    catkin_make

设置环境变量（如果不这样做，每次启动终端都要执行一遍 ``source`` 命令）

.. code-block:: sh

    # 在文件 ~/.bashrc 添加
    source ~/Desktop/catkin_ws/devel/setup.bash

    # 创建功能包
    cd catkin_ws/src
    catkin_create_pkg pkg_name std_msgs roscpp

.. Attention:: ``pkg_name`` 只允许使用小写字母、数字和下划线，而且首字符必须是一个小写字母。

编写C++程序
^^^^^^^^^^^^

.. code-block:: cpp
   :caption: src/talker.cpp

    #include "ros/ros.h"
    #include "std_msgs/String.h"
    #include <sstream>

    int main(int argc, char **argv) {
      ros::init(argc, argv, "talker");
      //set node name

      ros::NodeHandle nh;
      ros::Publisher pub = nh.advertise<std_msgs::String>("message", 1000);
      //set this node as publisher

      ros::Rate loop_rate(10);
      //set publish rate as 10Hz

      while (ros::ok()) {
        std_msgs::String msg;
        std::stringstream ss;
        ss << "default string";
        msg.data = ss.str();
        ROS_INFO("%s", msg.data.c_str());
        pub.publish(msg);
        ros::spinOnce();
        //if a subscriber comes, ros will update and read all topics

        loop_rate.sleep();
        //hang on the program
      }
      return 0;
    }

.. code-block:: cpp
   :caption: src/listener.cpp

   #include "ros/ros.h"
   #include "std_msgs/String.h"

   void messageCallback(const std_msgs::String::ConstPtr& msg) {
     ROS_INFO("I heard: [%s]", msg->data.c_str());
   }

   int main(int argc, char **argv) {
     ros::init(argc, argv, "listener");
     ros::NodeHandle nh;

     ros::Subscriber sub = nh.subscribe("mTopic", 1000, messageCallback);
     //register callback function

     ros::spin();
     //loop wait for callback function

     return 0;
   }

.. code-block:: xml
   :caption: launch/mlaunch.launch

   <launch>
     <node name="listener" pkg="testcomm" type="listener" output="screen" />
     <node name="talker" pkg="testcomm" type="talker" output="screen" />
     <param name="sentence" value="hello, world!" type="str" />
   </launch>

构建与运行
^^^^^^^^^^^

修改项目文件夹下的 :guilabel:`CMakeLists.txt`。顺序不能颠倒。此处以同时编译两个程序为例。

.. code-block:: cmake

    cmake_minimum_required(VERSION 2.8.3)
    project(testcomm)

    find_package(catkin REQUIRED COMPONENTS
      roscpp
      std_msgs
    )

    catkin_package(
      INCLUDE_DIRS include
      LIBRARIES testcomm
      CATKIN_DEPENDS roscpp std_msgs
      DEPENDS system_lib
    )

    include_directories(
     include
      ${catkin_INCLUDE_DIRS}
    )

    add_executable(talker src/talker.cpp)
    add_executable(listener src/listener.cpp)

    target_link_libraries(talker ${catkin_LIBRARIES})
    target_link_libraries(listener ${catkin_LIBRARIES})

执行构建命令：

* 在 :guilabel:`catkin_ws` 目录下执行 ``catkin_make`` 即可构建此工作空间下所有的项目。
* 执行 ``catkin_make -DCATKIN_WHITELIST_PACKAGES="pkg_name"`` 可构建指定的项目。

运行功能包。有两种运行方式：

* 直接运行一个或多个节点：

   .. code-block:: sh

       rosrun mypackage mypackage_node

* 加载launch文件（推荐）：

   .. code-block:: sh

      cd catkin_ws
      roslaunch mypackage mLaunch.launch

运行结果：

.. figure:: https://cdn.raysky.net/p/ros-1st-time6.png
   :align: center

按 **Ctrl+C** 可以结束程序。

References
-----------

.. [#] https://wiki.ros.org/kinetic/Installation/Ubuntu
.. [#] https://answers.ros.org/question/60366/problem-with-roscore/