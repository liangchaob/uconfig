#!/bin/sh

# 将程序放到opt下
rm -rf /opt/uconfig
cp -rf ./uconfig /opt/

# 创建快捷方式链接
alias uconfig='python /opt/uconfig/app/main.py'
echo "alias uconfig='python /opt/uconfig/app/main.py'" >> /root/.bashrc

# 附加package路径
echo "PATH='$PATH:/opt/uconfig/package/'" >> /root/.bashrc
source /root/.bashrc




# 附加软件的辅助命令
# rcconf
mkdir -p /var/lib/rcconf
touch /var/lib/rcconf/services


# 成功提示
echo "安装成功!"