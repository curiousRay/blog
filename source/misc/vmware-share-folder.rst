===========================
VMware共享文件夹设置问题
===========================

VMware虚拟机中安装open-vm-tools后，设置的共享文件夹不显示内容。解决方法如下：

1. 在虚拟机设置中添加挂载路径；

2. 进入虚拟机，输入 ``vmware-hgfsclient`` 应能列出挂载的文件夹名；

3. 如果需要一次性挂载，执行下列命令

    .. code-block:: bash

        mkdir /mnt/hgfs
        sudo vmhgfs-fuse .host:/ mnt/hgfs

4. 如果要在每次开机后自动挂载共享文件夹，则需在 :guilabel:`/etc/fstab` 文件最后添加：

    .. code-block:: sh

        .host:/ /mnt/hgfs fuse.vmhgfs-fuse allow_other,defaults 0 0
