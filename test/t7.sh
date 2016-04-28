#!/bin/bash

# 设置静态IP
IFACE='eth0'
IPADDR='192.168.1.2'
NETMASK='255.255.255.0'
GATEWAY='192.168.1.1'

echo '
DEVICE='${IFACE}'
IPADDR='${IPADDR}'
NETMASK='${NETMASK}'
GATEWAY='${GATEWAY}'
ONBOOT=yes
NAME='${IFACE}'
' > /etc/sysconfig/network-scripts/ifcfg-${IFACE}





# 改成dhcp
IFACE='eth0'

echo '
DEVICE='${IFACE}'
NM_CONTROLLED=NO
ONBOOT=yes
NAME='${IFACE}'
BOOTPROTO=DHCP
' > /etc/sysconfig/network-scripts/ifcfg-${IFACE}



DNS=172.16.191.2
echo 'nameserver '${DNS} > /etc/resolv.conf;echo 'search localdomain' >> /etc/resolv.conf;
