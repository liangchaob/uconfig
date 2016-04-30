# uconfig
一个只包含2%常用的linux系统命令的统一平台配置工具。

为了解决很多新手系统工程师，由于对linux系统的不熟悉和发行版众多以至于配置难的问题，而构建的一个中文的统一系统配置器，用于简化和统一日常linux系统的常用操作配置



## 安装
1.ssh到需要配置的主机上，将该软件包uconfig上传到需要配置的linux主机上
2.切换到root权限，执行以下命令:

    alias uconfig='python /opt/uconfig/app/main.py'
    bash ./uconfig/install.sh


*如果是linux主机是联网状态，而且安装了git，可以直接执行以下命令：

    git clone https://github.com/liangchaob/uconfig.git
    alias uconfig='python /opt/uconfig/app/main.py'
    bash ./uconfig/install.sh


## 使用

配置前需切换到root用户

    [root@localhost ~]# uconfig
    *********************************
    当前系统版本为 : centos-6.5
    *********************************
        参数如下:
            1. 用户配置-----负责用户的添加、删除、用户密码、用户权限等设置
            2. 网络配置-----负责网络接口、IP地址、防火墙、dns等网络相关设置
            3. 系统配置-----负责主机名、时间、启动脚本、程序与进程等系统相关设置
            4. 软件配置-----负责软件源、安装、更新、卸载等设置
            5. 当前版本号
            6. 退出
    输入设置项(1/2/3/4/5/6):


## 版本
v0.2
系统当前支持列表：

- ubuntu-14.04
- centos-6.5