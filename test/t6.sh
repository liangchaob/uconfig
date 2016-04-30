#!/bin/bash

# 设置静态IP
IFACE='eth0'
IPADDR='192.168.1.2'
NETMASK='255.255.255.0'
GATEWAY='192.168.1.1'



IP='address '${IPADDR};
MASK='netmask '${NETMASK};
GATEWAY='gateway '${GATEWAY};
ETH='iface '${IFACE}' inet';
T1='auto '${IFACE};
T2=${ETH}' static';
# 先去掉不要的东西
sed -i "/$ETH/,/auto/{/auto/b;d}" /etc/network/interfaces;
# dhcp或者静态
sed -i "/$T1/a$T2" /etc/network/interfaces;
# 逐行添加变量
sed -i "/$ETH/a$GATEWAY" /etc/network/interfaces;
sed -i "/$ETH/a$MASK" /etc/network/interfaces;
sed -i "/$ETH/a$IP" /etc/network/interfaces;







# 设置成DHCP
IFACE='eth0'

ETH='iface '${IFACE}' inet';
T1='auto '${IFACE};
T2=${ETH}' dhcp';
# 先去掉不要的东西
sed -i "/$ETH/,/auto/{/auto/b;d}" /etc/network/interfaces;

# dhcp或者静态
sed -i "/$T1/a$T2" /etc/network/interfaces;


DNS=172.16.191.2
echo 'nameserver '${DNS} > /etc/resolv.conf;echo 'search localdomain' >> /etc/resolv.conf;


APP=mysql
apt-cache search $APP |grep ${APP}




mount /dev/cdrom /media/cdrom
apt-cdrom -m -d /media/cdrom/ add apt-cdrom







