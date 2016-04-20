# 该文件夹用于存放各linux发行版的命令树

结构为：

    - ubuntu 14.04   # 使用uconfig使用该翻译器
        - init      # uconfig的初始化
            - show      # 显示当前的初始配置
        - user      # 用户设置
            - show      # 显示当前的用户配置
            - config    # 用户设置
        - network   # 网络设置
            - ifconfig  # 网络接口设置
            - dns       # 网络域名相关设置
            - iptable   # 防火墙相关设置
        - system    # 系统设置
            - hostname  # 主机名配置
            - process   # 当前运行程序与进程设置
            - init      # 系统开机启动项
        - software  # 软件设置
            - source    # 软件源设置
            - install   # 软件安装设置
        - update    # 更新uconfig

## 创建方式为build.sh

echo "输入操作系统名(空格以'-'代替):"
read SYSTEMNAME

mkdir "$SYSTEMNAME"
mkdir "$SYSTEMNAME/user"
mkdir "$SYSTEMNAME/network"
mkdir "$SYSTEMNAME/system"
mkdir "$SYSTEMNAME/software"
