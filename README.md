# uconfig
一个只包含2%常用的linux系统命令的统一平台配置工具。

为了解决很多新手系统工程师，由于对linux系统的不熟悉和发行版众多以至于配置难的问题，而构建的一个中文的统一系统配置器，用于简化和统一日常linux系统的常用操作配置



## 安装

1.下载该[软件包](https://github.com/liangchaob/uconfig/archive/master.zip)， 并将该软件包解压重命名为uconfig

2.ssh到需要配置的主机上，将该软件包uconfig上传到需要配置的linux主机上

3.切换到root权限，执行以下命令:

    alias uconfig='python /opt/uconfig/app/main.py'
    bash ./uconfig/install.sh

*如果是linux主机本身是联网状态，而且安装了git，可以直接执行以下命令：

    git clone https://github.com/liangchaob/uconfig.git
    alias uconfig='python /opt/uconfig/app/main.py'
    bash ./uconfig/install.sh


## 使用

配置前需切换到root用户

![屏幕快照 2016-12-07 14.48.49.png](https://ooo.0o0.ooo/2016/12/07/5847b1287246d.png)


## 版本

v0.2

系统当前支持列表：

- ubuntu-14.04
- centos-6.5

## 架构
核心文件在app下面，main.py用于设置用户交互，view.py用于向main返回shell脚本拼接函数

    + app
     + main.py
     + view.py

数据文件在dict下面，专用于存放各不同linux发行版对应的不同shell脚本命令

    + dict
     + centos-6.5.json
     + ubuntu-14.04.json 
     + ...

扩展包，用于添加第三方需要用到的辅助工具

    + package
     + rcconf


兼容性扩展通过获取其他版本linux发行版的shell脚本命令进行扩充，功能性扩展通过定义核心文件的交互与拼接设置。
