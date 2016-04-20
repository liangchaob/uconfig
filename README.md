# uconfig
一个只包含2%常用的linux系统命令的统一平台配置工具。

为了解决很多新手系统工程师，由于对linux系统的不熟悉和发行版众多以至于配置难的问题，而构建的一个中文的统一系统配置器，用于简化和统一日常linux系统的常用操作配置

## v0.1

系统支持列表：

- ubuntu-14.04


cli命令树

    - uconfig   # 使用uconfig使用该翻译器
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
            - process   # 当前运行程序与进程设置
            - init      # 系统开机启动项
        - software  # 软件设置
            - source    # 软件源设置
            - install   # 软件安装设置
        - update    # 更新uconfig


